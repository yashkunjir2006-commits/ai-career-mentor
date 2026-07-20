"""Admin routes"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.auth.models import User
from app.database.models import CareerRole, InterviewQuestion

admin_bp = Blueprint('admin', __name__, url_prefix='/api/admin')

def check_admin(user_id):
    """Check if user is admin"""
    user = User.query.get(user_id)
    return user and user.is_admin

@admin_bp.route('/users', methods=['GET'])
@jwt_required()
def get_all_users():
    """Get all users"""
    user_id = get_jwt_identity()
    
    if not check_admin(user_id):
        return jsonify({'error': 'Unauthorized - Admin access required'}), 403
    
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    
    users = User.query.paginate(page=page, per_page=per_page)
    
    return jsonify({
        'total': users.total,
        'pages': users.pages,
        'current_page': page,
        'users': [user.to_dict() for user in users.items]
    }), 200

@admin_bp.route('/users/<int:user_id>/toggle-status', methods=['PUT'])
@jwt_required()
def toggle_user_status(user_id):
    """Toggle user active status"""
    admin_id = get_jwt_identity()
    
    if not check_admin(admin_id):
        return jsonify({'error': 'Unauthorized - Admin access required'}), 403
    
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    user.is_active = not user.is_active
    db.session.commit()
    
    return jsonify({
        'message': f'User status updated',
        'user': user.to_dict()
    }), 200

@admin_bp.route('/career-roles', methods=['GET'])
@jwt_required()
def get_career_roles():
    """Get all career roles"""
    user_id = get_jwt_identity()
    
    if not check_admin(user_id):
        return jsonify({'error': 'Unauthorized - Admin access required'}), 403
    
    roles = CareerRole.query.all()
    
    return jsonify({
        'roles': [role.to_dict() for role in roles]
    }), 200

@admin_bp.route('/career-roles', methods=['POST'])
@jwt_required()
def create_career_role():
    """Create new career role"""
    user_id = get_jwt_identity()
    
    if not check_admin(user_id):
        return jsonify({'error': 'Unauthorized - Admin access required'}), 403
    
    data = request.get_json()
    
    if not data.get('name'):
        return jsonify({'error': 'Role name is required'}), 400
    
    # Check if role already exists
    if CareerRole.query.filter_by(name=data['name']).first():
        return jsonify({'error': 'Role already exists'}), 409
    
    role = CareerRole(
        name=data['name'],
        description=data.get('description', ''),
        required_skills=data.get('required_skills', []),
        preferred_skills=data.get('preferred_skills', []),
        job_market_demand=data.get('job_market_demand', 0)
    )
    
    db.session.add(role)
    db.session.commit()
    
    return jsonify({
        'message': 'Career role created',
        'role': role.to_dict()
    }), 201

@admin_bp.route('/interview-questions', methods=['POST'])
@jwt_required()
def add_interview_question():
    """Add interview question"""
    user_id = get_jwt_identity()
    
    if not check_admin(user_id):
        return jsonify({'error': 'Unauthorized - Admin access required'}), 403
    
    data = request.get_json()
    
    if not data.get('career_role_id') or not data.get('question'):
        return jsonify({'error': 'Missing required fields'}), 400
    
    question = InterviewQuestion(
        career_role_id=data['career_role_id'],
        question=data['question'],
        category=data.get('category', 'Technical'),
        difficulty=data.get('difficulty', 'Medium'),
        sample_answer=data.get('sample_answer', ''),
        tips=data.get('tips', [])
    )
    
    db.session.add(question)
    db.session.commit()
    
    return jsonify({
        'message': 'Interview question added',
        'question': question.to_dict()
    }), 201

@admin_bp.route('/stats', methods=['GET'])
@jwt_required()
def get_stats():
    """Get platform statistics"""
    user_id = get_jwt_identity()
    
    if not check_admin(user_id):
        return jsonify({'error': 'Unauthorized - Admin access required'}), 403
    
    total_users = User.query.count()
    active_users = User.query.filter_by(is_active=True).count()
    
    return jsonify({
        'statistics': {
            'total_users': total_users,
            'active_users': active_users,
            'career_roles': CareerRole.query.count(),
            'interview_questions': InterviewQuestion.query.count()
        }
    }), 200
