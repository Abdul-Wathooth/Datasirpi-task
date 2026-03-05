from flask import Flask, request, jsonify

app = Flask(__name__)

notes = []

@app.route("/")
def home():
    return "Notes API Running!"

@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)

@app.route("/notes", methods=["POST"])
def add_note():
    data = request.get_json()
    notes.append({
        "id": len(notes) + 1,
        "text": data.get("text")
    })
    return jsonify({"message": "Note added!", "notes": notes}), 201

@app.route("/notes/<int:id>", methods=["DELETE"])
def delete_note(id):
    global notes
    notes = [note for note in notes if note["id"] != id]
    return jsonify({"message": "Note deleted!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
