import json
from flask import Blueprint, request, jsonify
from database import save_workout_plan, get_latest_workout
from recommender_service import recommender

fitness_bp = Blueprint('fitness', __name__)

@fitness_bp.route("/save-workout", methods=["POST"])
def save_workout():
    data = request.json
    email = data.get('email')
    rec = data.get('recommendation')
    if not email or not rec:
        return jsonify({"status": "error", "message": "Missing info"}), 400
    success = save_workout_plan(
        email=email, 
        target=rec['target'], 
        difficulty=data.get('difficulty'), 
        exercises_json=json.dumps(rec['exercises']), 
        expected_burn=rec['expected_burn']
    )
    if success:
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "Failed to save to database"}), 500

@fitness_bp.route("/recommend-workout", methods=["POST"])
def recommend_workout():
    if recommender is None:
        return jsonify({"error": "Recommender system is not initialized"}), 500
    data = request.json
    difficulty = data.get('difficulty', 'Beginner')
    target_muscle = data.get('target_muscle', 'Full Body')
    try:
        user_weight = float(data.get('weight', 70))
    except ValueError:
        user_weight = 70.0
    weight_multiplier = user_weight / 70.0
    try:
        recommendations_df = recommender.recommend(difficulty, target_muscle)
        exercises = []
        running_total = 0
        for _, row in recommendations_df.iterrows():
            base_calories = row['Calories_Burned'] / 100
            adjusted_calories = int(base_calories * weight_multiplier)
            exercises.append({
                "name": row['Name of Exercise'],
                "sets": "3 Sets x 12 Reps",
                "calories": adjusted_calories
            })
            running_total += adjusted_calories
        return jsonify({
            "target": target_muscle,
            "exercises": exercises,
            "expected_burn": running_total
        })
    except Exception as e:
        print(f"Recommendation Error: {e}")
        return jsonify({"error": str(e)}), 500

@fitness_bp.route("/get-workout-plan", methods=["GET"])
def get_workout_plan():
    email = request.args.get('email')
    if not email:
        return jsonify({"error": "Email is required"}), 400
    workout_data = get_latest_workout(email)

    if workout_data:
        return jsonify({
            "status": "success",
            "data": workout_data
        })
    return jsonify({
        "status": "empty", 
        "message": "No workout saved for this user"
    }), 200