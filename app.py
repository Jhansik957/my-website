from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route for the homepage
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle gRNA design
@app.route("/design_grna", methods=["POST"])
def design_grna():
    data = request.json
    sequence = data.get("sequence", "")
    genome = data.get("genome", "")
    
    if not sequence or not genome:
        return jsonify({"error": "Sequence and genome are required"}), 400
    
    # Dummy gRNA design logic (replace with actual algorithm)
    grna = f"Designed gRNA for {genome}: {sequence[:20]}..."
    return jsonify({"grna": grna})

# Route to handle batch processing
@app.route("/process_batch", methods=["POST"])
def process_batch():
    file = request.files.get("file")
    
    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    
    # Dummy batch processing logic
    results = f"Processed {file.filename} successfully."
    return jsonify({"message": results})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
