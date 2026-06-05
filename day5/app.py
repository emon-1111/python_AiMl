from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open('../simple-student_model_multi.pkl', 'rb') as f:
    model = pickle.load(f)


def get_grade(score):
    if score >= 90:
        return ("A", "Excellent! Keep up the great work!", "#27ae60", "🌟")
    elif score >= 80:
        return ("B", "Good job! You're doing well!", "#3498db", "👍")
    elif score >= 70:
        return ("C", "Good! With a little more effort, you can do even better!", "#f39c12", "📚")
    elif score >= 60:
        return ("D", "You're passing, but try to study more!", "#e67e22", "⚠️")
    else:
        return ("F", "Don't give up! Try increasing your study hours!", "#e74c3c", "💪")


def get_study_tip(hours, score):
    if score < 60:
        recommended = max(5, hours + 2)
        return f"💡 Tip: Try studying {recommended:.1f} hours per day to improve your score!"
    elif score < 75:
        return "💡 Tip: You're on the right track! Stay consistent with your studies."
    elif score < 90:
        return "💡 Tip: Great work! Consider helping other students who are struggling."
    else:
        return "🎯 Tip: Excellent! Keep challenging yourself with advanced topics."


@app.route('/')
def home():
    return render_template('index.html', prediction=None, grade=None, message=None, tip=None, color=None, emoji=None)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['hours_studied']),
            float(request.form['attendance']),
            float(request.form['sleep_hours']),
            float(request.form['previous_score']),
            float(request.form['parent_education_encoded']),
            float(request.form['extracurricular_encoded']),
        ]

        prediction = model.predict([features])[0]
        prediction = round(float(max(0, min(100, prediction))), 2)

        grade, message, color, emoji = get_grade(prediction)
        tip = get_study_tip(features[0], prediction)

        return render_template('index.html',
                               prediction=prediction,
                               grade=grade,
                               message=message,
                               tip=tip,
                               color=color,
                               emoji=emoji)
    except Exception as e:
        return render_template('index.html',
                               prediction=None,
                               error=str(e),
                               grade=None, message=None, tip=None, color=None, emoji=None)


if __name__ == '__main__':
    app.run(debug=True)