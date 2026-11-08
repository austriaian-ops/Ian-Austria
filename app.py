from flask import Flask, jsonify, request
app = Flask(__name__)
# Home Endpoint
@app.route('/')
def home():
    return "Welcome to Ian Austria's Flask API!"
# Student Endpoint
@app.route('/student')
def get_student():
    return jsonify({
        "student_id": "24-00193",
        "name": "Ian Austriaa",
        "program": "BSIT",
        "year": 3,
        "section": "A"
    })
# Hello Endpoint
@app.route('/hello')
def say_hello():
    name = request.args.get('name', 'Student')
    return jsonify({
        "message": f"Hello, {name}!"
    })
# NEW ENDPOINT 1: About Me
@app.route('/about')
def about():
    return jsonify({
        "name": "Ian Austria",
        "program": "BSIT",
        "year": 3,
        "section": "A",
        "interest": "Army"
    })

    {
  "courses": [
    {
      "code": "BSIT",
      "name": "Bachelor of Science in Information Technology",
      "department": "Information Technology"
    },
    {
      "code": "BSCS",
      "name": "Bachelor of Science in Computer Science",
      "department": "Computer Studies"
    }
  ]
}

{
  "code": "BSIT",
  "name": "Bachelor of Science in Information Technology",
  "duration": "4 years",
  "description": "A program focused on computer systems, programming, and technology."
}

# NEW ENDPOINT 2: Greeting with Input
@app.route('/greet')
def greet():
    name = request.args.get('name', 'Friend')
    return jsonify({
        "message": f"Hello {name}! Welcome to Austrria's API.",
        "creator": "Iann Austria"
    })
# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)