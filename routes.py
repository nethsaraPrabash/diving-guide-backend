from flask import request, jsonify
from model import suggest_diving_areas

def suggest_diving_areas_endpoint():
    experience_level = request.args.get('experience_level')
    if not experience_level:
        return jsonify({'error': 'Experience level is required'}), 400
    
    suggestions = suggest_diving_areas(experience_level)
    if isinstance(suggestions, str):
        return jsonify({'error': suggestions}), 400
    
    return jsonify(suggestions)