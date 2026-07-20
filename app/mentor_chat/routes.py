"""Mentor chat routes"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.auth.models import User
from app.database.models import ChatSession, ChatMessage
from app.mentor_chat.chatbot import MentorChatbot
from datetime import datetime

mentor_bp = Blueprint('mentor', __name__, url_prefix='/api/mentor')

# Initialize chatbot
chatbot = MentorChatbot()

@mentor_bp.route('/chat/start', methods=['POST'])
@jwt_required()
def start_chat():
    """Start a new chat session"""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.get_json()
    
    # Create new chat session
    session = ChatSession(
        user_id=user_id,
        title=data.get('title', f'Chat - {datetime.utcnow().strftime("%Y-%m-%d %H:%M")}')
    )
    
    db.session.add(session)
    db.session.commit()
    
    # Send initial greeting
    initial_message = "Hi! I'm your AI Career Mentor. I'm here to help you with career guidance, skill development, interview preparation, and placement strategy. What can I help you with today?"
    
    bot_msg = ChatMessage(
        session_id=session.id,
        role='assistant',
        content=initial_message
    )
    
    db.session.add(bot_msg)
    db.session.commit()
    
    return jsonify({
        'message': 'Chat session started',
        'session_id': session.id,
        'initial_message': initial_message
    }), 201

@mentor_bp.route('/chat/<int:session_id>/message', methods=['POST'])
@jwt_required()
def send_message(session_id):
    """Send message in chat"""
    user_id = get_jwt_identity()
    
    # Verify session belongs to user
    session = ChatSession.query.get(session_id)
    if not session or session.user_id != user_id:
        return jsonify({'error': 'Session not found or unauthorized'}), 404
    
    data = request.get_json()
    
    if not data.get('message'):
        return jsonify({'error': 'No message provided'}), 400
    
    user_message = data['message']
    
    # Save user message
    user_msg = ChatMessage(
        session_id=session_id,
        role='user',
        content=user_message
    )
    
    db.session.add(user_msg)
    db.session.commit()
    
    # Generate bot response
    bot_response = chatbot.chat(user_message)
    
    # Save bot message
    bot_msg = ChatMessage(
        session_id=session_id,
        role='assistant',
        content=bot_response
    )
    
    db.session.add(bot_msg)
    session.updated_at = datetime.utcnow()
    db.session.commit()
    
    return jsonify({
        'message': bot_response,
        'user_message': user_message
    }), 200

@mentor_bp.route('/interview-question', methods=['GET'])
def get_interview_question():
    """Get random interview question"""
    data = request.get_json() or {}
    role = data.get('role')
    
    question = chatbot.get_interview_question(role)
    
    return jsonify({
        'question': question,
        'role': role
    }), 200

@mentor_bp.route('/learning-tip', methods=['GET'])
def get_learning_tip():
    """Get learning tip"""
    tip = chatbot.get_learning_tip()
    
    return jsonify({
        'tip': tip
    }), 200
