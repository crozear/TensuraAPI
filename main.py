from flask import Flask, request, jsonify
import json
from fuzzywuzzy import process

app = Flask(__name__)

# Step 5: Load Your JSON Data
try:
    with open('Slime.json', 'r') as file:
        data = json.load(file)
    # Create a list of character names for fuzzy matching
    character_names = [character['name'] for character in data]
except FileNotFoundError:
    data = {}
    print("Data file not found.")

# Step 6: Create API Endpoints
@app.route('/characters', methods=['GET'])
def get_character_info():
    query_name = request.args.get('name')
    if not query_name:
        return jsonify({"error": "No name provided"}), 400

    # Use fuzzy matching to find the best match for the query name
    best_match, score = process.extractOne(query_name, character_names)
    if score < 75:  # You can adjust the score threshold as needed
        return jsonify({"error": "Character not found"}), 404
    
    # Find the full character info for the best match
    character_info = next((char for char in data if char['name'] == best_match), None)
    if character_info:
        return jsonify(character_info)
    else:
        return jsonify({"error": "Character not found"}), 404

if __name__ == '__main__':
    app.run()