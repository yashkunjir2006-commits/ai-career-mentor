"""Test AI Engine"""

import pytest
from app.ai_engine.recommender import CareerRecommender

class TestCareerRecommender:
    """Test career recommendation engine"""
    
    def test_predict_career_roles(self):
        """Test career role prediction"""
        recommender = CareerRecommender()
        
        skills = ['python', 'machine learning', 'tensorflow', 'data analysis']
        predictions = recommender.predict_career_roles(skills)
        
        assert len(predictions) <= 3
        assert all(isinstance(p, tuple) for p in predictions)
        assert all(0 <= p[1] <= 100 for p in predictions)
    
    def test_get_skill_gap(self):
        """Test skill gap detection"""
        recommender = CareerRecommender()
        
        skills = ['python', 'sql']
        gap = recommender.get_skill_gap(skills, 'Data Analyst')
        
        assert 'missing_required_skills' in gap
        assert 'missing_preferred_skills' in gap
    
    def test_calculate_placement_readiness(self):
        """Test placement readiness calculation"""
        recommender = CareerRecommender()
        
        skills = ['python', 'java', 'sql', 'react', 'docker']
        readiness = recommender.calculate_placement_readiness(skills, experience_months=6)
        
        assert 'overall_score' in readiness
        assert 0 <= readiness['overall_score'] <= 100
        assert 'readiness_level' in readiness
    
    def test_generate_learning_roadmap(self):
        """Test learning roadmap generation"""
        recommender = CareerRecommender()
        
        skills = ['python', 'sql']
        roadmap = recommender.generate_learning_roadmap(skills, 'Data Analyst')
        
        assert 'target_role' in roadmap
        assert 'phases' in roadmap
        assert len(roadmap['phases']) > 0
