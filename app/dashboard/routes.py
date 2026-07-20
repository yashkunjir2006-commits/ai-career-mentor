"""Dashboard routes"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.auth.models import User
from app.database.models import Resume, Recommendation, CareerRole, LearningPath, ChatSession
from app.ai_engine.recommender import CareerRecommender

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/api/dashboard')

@dashboard_bp.route('/overview', methods=['GET'])
@jwt_required()
def get_overview():
    """Get dashboard overview"""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    # Get user statistics
    resumes_count = Resume.query.filter_by(user_id=user_id).count()
    recommendations_count = Recommendation.query.filter_by(user_id=user_id).count()
    learning_paths_count = LearningPath.query.filter_by(user_id=user_id).count()
    chat_sessions_count = ChatSession.query.filter_by(user_id=user_id).count()
    
    # Get latest recommendation
    latest_recommendation = Recommendation.query.filter_by(user_id=user_id).order_by(
        Recommendation.created_at.desc()
    ).first()
    
    latest_recommendation_data = None
    if latest_recommendation:
        latest_recommendation_data = {
            'career_role': latest_recommendation.career_role.name,
            'match_score': latest_recommendation.match_score,
            'placement_readiness_score': latest_recommendation.placement_readiness_score,
            'created_at': latest_recommendation.created_at.isoformat()
        }
    
    return jsonify({
        'user': user.to_dict(),
        'statistics': {
            'resumes': resumes_count,
            'recommendations': recommendations_count,
            'learning_paths': learning_paths_count,
            'chat_sessions': chat_sessions_count
        },
        'latest_recommendation': latest_recommendation_data
    }), 200

@dashboard_bp.route('/skill-analysis', methods=['GET'])
@jwt_required()
def skill_analysis():
    """Analyze user skills"""
    user_id = get_jwt_identity()
    
    resume = Resume.query.filter_by(user_id=user_id, is_active=True).first()
    
    if not resume:
        return jsonify({'error': 'No active resume found'}), 404
    
    skills = resume.parsed_data.get('skills', [])
    
    # Categorize skills
    skill_categories = {
        'programming': ['python', 'java', 'javascript', 'c++', 'c#', 'go', 'rust', 'ruby', 'php'],
        'web': ['react', 'angular', 'vue', 'html', 'css', 'node.js', 'express', 'django', 'flask'],
        'data': ['sql', 'data analysis', 'machine learning', 'deep learning', 'tableau', 'power bi', 'pandas', 'numpy'],
        'cloud': ['aws', 'gcp', 'azure', 'docker', 'kubernetes'],
        'tools': ['git', 'jenkins', 'jira', 'linux', 'docker', 'kubernetes']
    }
    
    categorized_skills = {}
    uncategorized_skills = []
    
    for skill in skills:
        found = False
        for category, category_skills in skill_categories.items():
            if skill.lower() in category_skills:
                if category not in categorized_skills:
                    categorized_skills[category] = []
                categorized_skills[category].append(skill)
                found = True
                break
        if not found:
            uncategorized_skills.append(skill)
    
    return jsonify({
        'skills': {
            'categorized': categorized_skills,
            'uncategorized': uncategorized_skills,
            'total_count': len(skills)
        }
    }), 200
