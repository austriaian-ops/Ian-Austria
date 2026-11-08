
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
        "student_id": "24-00230",
        "name": "Ian Austria",
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


# NEW ENDPOINT 2: Courses List
@app.route('/courses')
def courses():
    return jsonify({
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
    })


# NEW ENDPOINT 3: Course Details (URL Input)
@app.route('/courses/<course_code>')
def course_details(course_code):

    course_data = {
        "BSIT": {
            "code": "BSIT",
            "name": "Bachelor of Science in Information Technology",
            "duration": "4 years",
            "description": "A program focused on computer systems, programming, and technology."
        },
        "BSCS": {
            "code": "BSCS",
            "name": "Bachelor of Science in Computer Science",
            "duration": "4 years",
            "description": "A program focused on computing and software development."
        }
    }

    course = course_data.get(course_code.upper())

    if course:
        return jsonify(course)

    return jsonify({"error": "Course not found"}), 404


# Greeting Endpoint
@app.route('/greet')
def greet():
    name = request.args.get('name', 'Friend')
    return jsonify({
        "message": f"Hello {name}! Welcome to Austria's API.",
        "creator": "Ian Austria"
    })

from flask import Flask, jsonify, request
app = Flask(__name__)
# Home Endpoint
@app.route('/')
def home():
    return "Welcome to Jorand Alipala's Flask API!"
# Student Endpoint
@app.route('/student')
def get_student():
    return jsonify({
        "student_id": "24-00193",
        "name": "Jonard Alipala",
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
        "name": "Jonard Alipala",
        "program": "BSIT",
        "year": 3,
        "section": "A",
        "interest": "Electrical Engineering"
    })
# NEW ENDPOINT 2: Greeting with Input
@app.route('/greet')
def greet():
    name = request.args.get('name', 'Friend')
    return jsonify({
        "message": f"Hello {name}! Welcome to Alipala's API.",
        "creator": "Jonard Alipala"

# Run the Flask Application
if __name__ == '__main__':
    app.run(debug=True)
