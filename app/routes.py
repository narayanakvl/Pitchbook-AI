from flask import render_template, request, send_file
from app import app
from app.utils import generate_fake_data

@app.route("/")
def home():
    return render_template("generate.html")

@app.route("/generate-fake-data", methods=["POST"])
def generate_fake_data_route():
    rows = int(request.form["rows"])
    columns = request.form["columns"].split(",")
    
    # Generate fake data
    file_path = generate_fake_data(rows, columns)
    
    # Serve the file for download
    return send_file(file_path, as_attachment=True)
