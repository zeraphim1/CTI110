# Michael Earl
# 3/09/25
# source 1 http://fitnowtraining.com/2012/01/formula-for-calories-burned/
# source 2 https://learn.zybooks.com/zybook/CTI110FAYTECHCCCTI110Spring2025/chapter/7/section/5

print('This program will calculate your calorie expenditure for your workout!\n')

two_genders = ["male", "female"]

print('type male or female when asked for your gender\n')

# the .lower() ignores case sensitivity

while True:
    gender = input('What is your gender? ').lower()
    if gender in two_genders:
        break
    else:
        print('Invalid answer entered, please enter \"male\" or \"female\"')
   
age = float(input('\nWhat is your age? '))

weight = float(input('\nWhat is your weight in pounds? '))

Heart_bpm = float(input('\nWhat is your average heart rate during your workout? '))

Workout_length = float(input('\nHow long was your workout in minutes? '))

if gender == "male":
    calories_man = ( (age * 0.2017) + (weight * 0.09036) + (Heart_bpm * 0.6309) - 55.0969) * Workout_length / 4.184
    print(f'\nYou burned {calories_man:.2f} calories in your workout!')

elif gender == "female":
    calories_female = ( (age * 0.074) - (weight * 0.05741) + (Heart_bpm * 0.4472) - 20.4022) * Workout_length / 4.184
    print(f'\nYou burned {calories_female:.2f} calories in your workout!')

input("\nPress Enter to exit...")