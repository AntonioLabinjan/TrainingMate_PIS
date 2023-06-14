CREATE DATABASE TRAININGMATE;
USE TRAININGMATE;
CREATE TABLE Exercise (
	exercise_identificator INT PRIMARY KEY,
    exercise_name VARCHAR(200),
    exercise_calories INT,
    exercise_duration INT,
    exercise_intensity VARCHAR(200)
    );
CREATE TABLE Meal (
	meal_identificator INT PRIMARY KEY,
	meal_name VARCHAR(200),
	meal_calories INT,
	meal_number INT,
	meal_category VARCHAR (200),
	meal_location VARCHAR (200)
	);