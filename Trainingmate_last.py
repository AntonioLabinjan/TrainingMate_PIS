from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:AN1246A301JA@localhost/TRAININGMATE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Exercise(db.Model):
    exercise_identificator = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(200))
    exercise_calories = db.Column(db.Integer)
    exercise_duration = db.Column(db.Integer)
    exercise_intensity = db.Column(db.String(200))


    def __init__(self, exercise_identificator, exercise_name, exercise_calories, exercise_duration, exercise_intensity):

        self.exercise_identificator = exercise_identificator
        self.exercise_name = exercise_name
        self.exercise_calories = exercise_calories
        self.exercise_duration = exercise_duration
        self.exercise_intensity = exercise_intensity

class Meal(db.Model):
    meal_identificator = db.Column(db.Integer, primary_key=True)
    meal_name = db.Column(db.String(200))
    meal_calories = db.Column(db.Integer)
    meal_number = db.Column(db.Integer)
    meal_category = db.Column(db.String(200))
    meal_location = db.Column(db.String(200))

    def __init__(self, meal_identificator, meal_name, meal_calories, meal_number, meal_category, meal_location):

        self.meal_identificator = meal_identificator
        self.meal_name = meal_name
        self.meal_calories = meal_calories
        self.meal_number = meal_number
        self.meal_category = meal_category
        self.meal_location = meal_location


@app.route('/')
def Index():
    all_exercises = Exercise.query.all()
    all_meals = Meal.query.all()
    return render_template("index.html", exercises = all_exercises, meals = all_meals)



@app.route('/insert_exercise', methods = ['POST'])
def insert_exercise():

    if request.method == 'POST':

        exercise_identificator = request.form['exercise_identificator'] 
        exercise_name = request.form['exercise_name']
        exercise_calories = request.form['exercise_calories']
        exercise_duration = request.form['exercise_duration']
        exercise_intensity = request.form['exercise_intensity']


        my_exercise = Exercise(exercise_identificator, exercise_name, exercise_calories, exercise_duration, exercise_intensity)
        db.session.add(my_exercise)
        db.session.commit()

        flash("EXERCISE HAS BEEN INSERTED SUCCESSFULLY AT: "+ datetime.now().strftime("%H:%M"))

        return redirect(url_for('Index'))

@app.route('/insert_meal', methods = ['POST'])
def insert_meal():

    if request.method == 'POST':

        meal_identificator = request.form['meal_identificator']
        meal_name = request.form['meal_name']
        meal_calories = request.form['meal_calories']
        meal_number = request.form['meal_number']
        meal_category = request.form['meal_category']
        meal_location = request.form['meal_location']

        my_meal = Meal(meal_identificator,meal_name, meal_calories, meal_number, meal_category, meal_location)
        db.session.add(my_meal)
        db.session.commit()

        flash("MEAL HAS BEEN INSERTED SUCCESSFULLY AT:"+ datetime.now().strftime("%H:%M"))

        return redirect(url_for('Index'))

@app.route('/update_exercise', methods = ['GET', 'POST'])
def update_exercise():

    if request.method == 'POST':
        my_exercise = Exercise.query.get(request.form.get('exercise_identificator'))

        my_exercise.exercise_name = request.form['exercise_name']
        my_exercise.exercise_calories = request.form['exercise_calories']
        my_exercise.exercise_duration = request.form['exercise_duration']
        my_exercise.exercise_intensity = request.form['exercise_intensity']

        db.session.commit()
        flash("Exercise Updated Successfully")

        return redirect(url_for('Index'))

@app.route('/update_meal', methods = ['GET','POST'])
def update_meal():

    if request.method == 'POST':
        my_meal = Meal.query.get(request.form.get('meal_identificator'))

        my_meal.meal_name = request.form['meal_name']
        my_meal.meal_calories = request.form['meal_calories']
        my_meal.meal_number = request.form['meal_number']
        my_meal.meal_category = request.form['meal_category']
        my_meal.meal_location = request.form['meal_location']

        db.session.commit()
        flash("Meal Updated Successfully")

        return redirect(url_for('Index'))

@app.route('/delete_exercise/<exercise_identificator>/', methods = ['GET', 'POST'])
def delete_exercise(exercise_identificator):
    my_exercise = Exercise.query.get(exercise_identificator)
    db.session.delete(my_exercise)
    db.session.commit()
    flash("Exercise Deleted Successfully")

    return redirect(url_for('Index'))

@app.route('/delete_meal/<meal_identificator>/', methods = ['GET', 'POST'])
def delete_meal(meal_identificator):
    my_meal = Meal.query.get(meal_identificator)
    db.session.delete(my_meal)
    db.session.commit()
    flash ("Meal Deleted Successfully")

    return redirect(url_for('Index'))

@app.route('/calculate_total_duration')
def calculate_total_duration():
    total_duration = 0  

    all_exercises = Exercise.query.all() 

    for exercise in all_exercises:
        total_duration += exercise.exercise_duration  

    flash("Total duration of workout is: " + str(total_duration)) 

    return redirect(url_for('Index'))

@app.route('/calculate_exercise_calories')
def calculate_exercise_calories():
    total_calories_spent = 0

    all_exercises = Exercise.query.all()

    for exercise in all_exercises:
        total_calories_spent += exercise.exercise_calories

    flash("Total calories spent training: " + str(total_calories_spent))

    return redirect(url_for('Index'))

@app.route('/calculate_meal_calories')
def calculate_meal_calories():
    total_calories_consumed = 0

    all_meals = Meal.query.all()

    for meal in all_meals:
        total_calories_consumed += meal.meal_calories

    flash("Total calories consumed by eating: " + str(total_calories_consumed))

    return redirect(url_for('Index'))

@app.route('/sort_exercises_by_duration')
def sort_exercises_by_duration():
    all_exercises = Exercise.query.order_by(Exercise.exercise_duration.desc()).all()
    return render_template("index.html", exercises=all_exercises)

@app.route('/sort_meals_by_calories')
def sort_meals_by_calories():
    all_meals = Meal.query.order_by(Meal.meal_calories.desc()).all()
    return render_template("index.html", meals=all_meals)

@app.route('/calculate_caloric_balance')
def calculate_caloric_balance():
    total_calories_consumed = 0
    total_calories_spent = 0

    all_exercises = Exercise.query.all()
    all_meals = Meal.query.all()

    for exercise in all_exercises:
        total_calories_spent += exercise.exercise_calories

    for meal in all_meals:
        total_calories_consumed += meal.meal_calories

    if total_calories_consumed > total_calories_spent:
        message = "Person is in caloric surplus."
    elif total_calories_consumed < total_calories_spent:
        message = "Person is in caloric deficit."
    else:
        message = "Person is in caloric balance."

    flash("Total calories consumed: " + str(total_calories_consumed))
    flash("Total calories spent: " + str(total_calories_spent))
    flash(message)

    return redirect(url_for('Index'))

#OVO JE GRAF KOJI ĆE POKAZAT SVE VJEŽBE I NJIHOVE KALORIJE

@app.route('/chart_data')
def chart_data():
    all_exercises = Exercise.query.all()

    exercise_names = [exercise.exercise_name for exercise in all_exercises]
    exercise_calories = [exercise.exercise_calories for exercise in all_exercises]

    chart_data = {
        'labels': exercise_names,
        'data': exercise_calories
    }

    return render_template('chart.html', chart_data=chart_data)

@app.route('/chart_data2')
def chart_data2():
    all_meals = Meal.query.all()

    meal_names = [meal.meal_name for meal in all_meals]
    meal_calories = [meal.meal_calories for meal in all_meals]

    chart_data = {
        'labels' : meal_names,
        'data' : meal_calories
    }

    return render_template('chart2.html', chart_data=chart_data)

@app.route('/chart_data3')
def chart_data3():
    all_exercises = Exercise.query.all()

    exercise_intensities = [exercise.exercise_intensity for exercise in all_exercises]
    intensity_counts = {category: exercise_intensities.count(category) for category in set(exercise_intensities)}

    chart_data = {
        'labels' : list(intensity_counts.keys()),
        'data': list(intensity_counts.values())
    }

    return render_template('chart3.html', chart_data=chart_data)

@app.route('/chart_data4')
def chart_data4():
    all_meals = Meal.query.all()

    meal_categories = [meal.meal_category for meal in all_meals]
    category_counts = {category: meal_categories.count(category) for category in set(meal_categories)}

    chart_data = {
        'labels': list(category_counts.keys()),
        'data': list(category_counts.values())
    }

    return render_template('chart4.html', chart_data=chart_data)

if (__name__ == "__main__"):
    app.run(debug=True)