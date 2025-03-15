from flask import request, jsonify
from ruindiv import suggest_diving_areas
from cdiving import preprocess_input, make_prediction
from seaani import predict_image_from_bytes

def suggest_diving_areas_endpoint():
    experience_level = request.args.get('experience_level')
    if not experience_level:
        return jsonify({'error': 'Experience level is required'}), 400
    
    suggestions = suggest_diving_areas(experience_level)
    if isinstance(suggestions, str):
        return jsonify({'error': suggestions}), 400
    
    return jsonify(suggestions)

def cdiving():
    try:
        data = request.json
        
        processed_data = preprocess_input(data)
        
        predicted_label = make_prediction(processed_data)
        
        return jsonify({"Predicted Record Category": predicted_label})
    
    except Exception as e:
        return jsonify({"error": str(e)})

def classify_image():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        image_file = request.files['image']
        image_bytes = image_file.read()

        predicted_label = predict_image_from_bytes(image_bytes)

        return jsonify({"Predicted Label": predicted_label})

    except Exception as e:
        return jsonify({"error": str(e)})