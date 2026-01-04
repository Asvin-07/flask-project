from flask import Flask, jsonify, request
import os
import argparse

app = Flask(__name__)

# In-memory "database"
items = {}

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Flask REST API!",
        "status": "active",
        "endpoints": ["/items (GET, POST)", "/items/<id> (DELETE)"]
    })

# GET endpoint
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# POST endpoint
@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data:
        return jsonify({"error": "Missing 'id' or 'name'"}), 400
    item_id = str(data['id']) # Ensure ID is string
    if item_id in items:
        return jsonify({"error": "Item already exists"}), 400
    items[item_id] = data['name']
    return jsonify({"message": f"Item {item_id} added.", "item": {item_id: data['name']}}), 201

# DELETE endpoint
@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in items:
        return jsonify({"error": "Item not found"}), 404
    del items[item_id]
    return jsonify({"message": f"Item {item_id} deleted."}), 200

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the Flask REST API server.")
    # Defaults to env var PORT or 5000
    parser.add_argument('--port', type=int, default=int(os.getenv("PORT", 5000)))
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()

    app.run(host='0.0.0.0', port=args.port, debug=args.debug)