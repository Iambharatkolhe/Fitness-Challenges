#Fitness_challenge
import csv
import os
import time

from tabulate import tabulate

# Define the data for the tables
increase_weight_table = [
   
    ["Brown Rice", 200],
    ["Avocado", 160],
    ["Almonds", 200],
    ["Peanut Butter", 190],
    ["Whole Milk", 150],
    ["Sweet Potato", 180],
    ["Pasta (Cooked)", 200],
    ["Cheese", 110],
    ["Olive Oil", 120],
    ["Granola", 120],
    ["Banana", 100],
    ["Beef", 250],
    ["Potatoes (Boiled)", 130],
    ["Hummus", 180],
    ["Cashews", 155],
    ["Sunflower Seeds", 165],
    ["Dates", 280]
]


decrease_weight_table = [
    ["Spinach", 23],
    ["Kale", 35],
    ["Broccoli", 34],
    ["Cucumber", 15],
    ["Tomato", 18],
    ["Carrots", 41],
    ["Lettuce", 15],
    ["Strawberries", 32],
    ["Grapefruit", 42],
    ["Lemon", 29],
    ["Greek Yogurt", 59],
    ["Salmon", 208],
    ["Tuna", 184],
    ["Chicken Breast (Skinless)", 165],
    ["Turkey Breast (Skinless)", 135],
    ["Eggs", 155],
    ["Quinoa", 120],
    ["Black Beans", 114]
]

mental_relief_table = [
    ["Dark Chocolate", 170],
    ["Berries (Blueberries, Strawberries)", 50],
    ["Nuts (Almonds, Walnuts)", 160],
    ["Fatty Fish (Salmon, Trout)", 200],
    ["Whole Grains (Oats, Quinoa)", 110],
    ["Yogurt", 50],
    ["Leafy Greens (Spinach, Kale)", 25],
    ["Bananas", 105],
    ["Turmeric", 24],
    ["Green Tea", 0],
    ["Oranges", 62],
    ["Pumpkin Seeds", 125],
    ["Chamomile Tea", 0],
    ["Broccoli", 55],
    ["Eggs", 155],
    ["Sweet Potatoes", 86],
    ["Avocado", 160],
    ["Seaweed", 45]
]
# Function to authenticate user
def authenticate(username, password):
    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                print("Login successful!")
                return True
    print("Invalid username or password. Please try again.")
    return False

# Function to register a new user
def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    with open("users.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    print("Registration successful!")

# Main login process
def login():
    while True:
        choice = input("Do you have an account? (y/n): ").lower()
        if choice == "y":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if authenticate(username, password):
                return username
        elif choice == "n":
            register()
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

# Function to get user's progress
def check_progress(username):
    if not os.path.exists(f"{username}_challenge.csv"):
        print("No challenge data found.")
        return

    total_time = 0
    total_challenges = 00
    
    total_weight_change = 0

    with open(f"{username}_challenge.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            total_time += int(row[2])
            total_challenges += 1
            if purpose == "1":  # Increase weight
                total_weight_change += 1
            elif purpose == "2":  # Decrease weight
                total_weight_change -= 1

    print("\nProgress Summary:")
    print(f"Total time spent: {total_time} seconds")
    print(f"Total challenges completed: {total_challenges}")
    print(f"Total weight change: {total_weight_change} pound")

# Function to get user's purpose
def get_purpose():
    while True:
        print("Choose your purpose:")
        print("1. Increase weight")
        print("2. Decrease weight")
        print("3. Mental relief")
        purpose = input("Enter your choice (1/2/3): ")
        global pur
        pur=purpose
        if purpose in ["1", "2", "3"]:
            return purpose
        else:
            print("Invalid option. Please enter 1, 2, or 3.")

# Function to get user's preferred exercises
def get_preferred_exercises():
    while True:
        print("Choose your preferred exercises (select one or more options):")
        print("1. Cycling")
        print("2. Running")
        print("3. Weightlifting")
        print("4. Swimming")
        print("5. Yoga")
        choices = input("Enter your choices separated by commas (e.g., '1,3'): ")
        choices = choices.split(",")
        exercises = {
            "1": "Cycling",
            "2": "Running",
            "3": "Weightlifting",
            "4": "Swimming",
            "5": "Yoga"
        }
        preferred_exercises = [exercises[choice] for choice in choices if choice in exercises]
        if preferred_exercises:
            return preferred_exercises
        else:
            print("Invalid option. Please select at least one exercise.")

# Function to get weightlifting exercises
def get_weightlifting_exercises():
    while True:
        print("Choose your weightlifting exercises (select one or more options):")
        print("1. Bench Press")
        print("2. Dumbbell Press")
        print("3. Squats")
        print("4. Punching Bag")
        print("5. Bench Rows")
        choices = input("Enter your choices separated by commas (e.g., '1,3'): ")
        exercises = {
            "1": "Bench Press",
            "2": "Dumbbell Press",
            "3": "Squats",
            "4": "Punching Bag",
            "5": "Bench Rows"
        }
        selected_exercises = [exercises[choice] for choice in choices.split(",") if choice in exercises]
        if selected_exercises:
            return selected_exercises
        else:
            print("Invalid option. Please select at least one exercise.")

# Function to get yoga asanas
def get_yoga_asanas():
    while True:
        print("Choose your yoga asanas (select one or more options):")
        print("1. Sukhasana (Easy Pose)")
        print("2. Surya Namaskar (Sun Salutation)")
        print("3. Viparita Karani (Legs-Up-the-Wall Pose)")
        print("4. Balasana (Child's Pose)")
        print("5. Anulom Vilom (Alternate Nostril Breathing)")
        choices = input("Enter your choices separated by commas (e.g., '1,3'): ")
        asanas = {
            "1": "Sukhasana",
            "2": "Surya Namaskar",
            "3": "Viparita Karani",
            "4": "Balasana",
            "5": "Anulom Vilom"
        }
        selected_asanas = [asanas[choice] for choice in choices.split(",") if choice in asanas]
        if selected_asanas:
            return selected_asanas
        else:
            print("Invalid option. Please select at least one asana.")

# Function to start exercise timer
def start_exercise_timer(duration):
    print("Starting exercise timer...")
    for seconds in range(duration, 0, -1):
        print(seconds, end=" ")
        time.sleep(1)
    print("Exercise complete!")

# Function to calculate BMI
def calculate_bmi(weight, height):
    return (weight / (height ** 2)) * 10000

# Function to get BMI category
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 25:
        return "normal weight"
    else:
        return "overweight"
# Login process
print("Welcome to the Fitness Challenge App!")
print("Disclaimer: This app provides general information and is for educational purposes only. It is not intended to be a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition. Never disregard professional medical advice or delay in seeking it because of something you have read in this app.")

username = login()
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
bmi = calculate_bmi(weight, height)
print(f"Your BMI is {bmi:.2f}.")
category = get_bmi_category(bmi)
print(f"You are categorized as {category}.")



# Check Progress option
check_choice = input("Do you want to check your progress? (y/n): ").lower()
if check_choice == "y":
    check_progress(username)
else:
    purpose = get_purpose()
    preferred_exercises = get_preferred_exercises()

    # Save user information
    with open(f"{username}_info.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Purpose", "Preferred Exercises"])
        writer.writerow([purpose, ", ".join(preferred_exercises)])

    # Prompt user to select challenge duration
    challenge_duration = int(input("Select challenge duration (in days): "))

    # Start challenge
    print(f"\nStarting {challenge_duration}-day challenge!")
    with open(f"{username}_challenge.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Day", "Exercise", "Duration"])
        for day in range(1, challenge_duration + 1):
            print(f"\nDay {day} of {challenge_duration}")
            ready = input("Are you ready for today's exercises? (yes/no): ").lower()
            if ready == "yes":
                for exercise in preferred_exercises:
                    if exercise == "Weightlifting":
                        selected_exercises = get_weightlifting_exercises()
                        for specific_exercise in selected_exercises:
                            if specific_exercise in ["Bench Press", "Dumbbell Press", "Squats"]:
                                duration = 60  # Example duration for common weightlifting exercises
                            else:
                                duration = 45  # Example duration for additional weightlifting exercises
                            print(f"\nGet ready for {specific_exercise} session!")
                            start_exercise_timer(duration)
                            writer.writerow([day, specific_exercise, duration])
                    elif exercise == "Yoga":
                        selected_asanas = get_yoga_asanas()
                        for specific_asana in selected_asanas:
                            if specific_asana in ["Sukhasana", "Surya Namaskar"]:
                                duration = 30  # Example duration for common yoga asanas
                            else:
                                duration = 20  # Example duration for additional yoga asanas
                            print(f"\nGet ready for {specific_asana} session!")
                            start_exercise_timer(duration)
                            writer.writerow([day, specific_asana, duration])
                    else:
                        if exercise in ["Cycling", "Running", "Swimming"]:
                            duration = 45  # Example duration for common cardio exercises
                        print(f"\nGet ready for {exercise} session!")
                        start_exercise_timer(duration)
                        writer.writerow([day, exercise, duration])
            else:
                print("Okay, let's start when you're ready.")
                input("Press Enter when you're ready to start the day.")
                
diet=int(input('You want to check Diet as Well?(1/0)'))
if diet==1:
         if int(pur)==1:  # Convert pur to integer
              print("### Goal: Increase Weight")
              print(tabulate(increase_weight_table, headers=["Food", "Calories"], tablefmt="pipe"))
         elif int(pur)==2:
              print("### Goal: Decrease Weight")
              print(tabulate(decrease_weight_table, headers=["Food", "Calories"], tablefmt="pipe"))
         else:
              print("### Goal: Mental Relief")
              print(tabulate(mental_relief_table, headers=["Food", "Calories"], tablefmt="pipe"))
             
             
             


print("\nThank you for using the Fitness Challenge App!")