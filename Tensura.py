from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Step 5: Load Your JSON Data
try:
    with open('slime.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    data = {}
    print("Data file not found.")

# Step 6: Create API Endpoints
@app.route('/characters', methods=['GET'])
def get_character_info():
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "No name provided"}), 400

    # Search logic to find character information
    character_info = [character for character in data if character.get('name') == name]
    if character_info:
        return jsonify(character_info)
    else:
        return jsonify({"error": "Character not found"}), 404

# Step 8: Running the Application
if __name__ == '__main__':
    app.run(debug=True)
