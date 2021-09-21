import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--name", help="Write your name [optional]", type=str)
parser.add_argument("--gender", help="Choose your gender: male, female [optional]", type=str, choices=["male", "female"])

parser.add_argument("height", help="Write your height (cm)", type=float)
parser.add_argument("weight", help="Write your weight (kg)", type=float)
parser.add_argument("hsleep", help="How much do you usually sleep? (hours)", type=int)
parser.add_argument("meals", help="How many meals does your daily diet include? (meals)", type=int)
parser.add_argument("fruveg", help="How many fresh fruits and vegetables do you eat during the day? (grams)", type=int)
parser.add_argument("steps", help="How many steps do you walk on average per day? (steps)", type=int)
parser.add_argument("health_monitoring", help="Do you monitor your health? 0 - Not; 1 - Yes, I have been undergoing medical examination in the last 3 years, 2 - Yes, but I do not see a doctor", type=int)
parser.add_argument("mood", help="What is your mood today? Good, Neutral or Bad?", type=str, choices=["Good", "Neutral", "Bad"])
parser.add_argument("when_happy", help="When was the last time you had a state of happiness? 0 - During the week, 1 - During the month, 2 - During the year", type=int)

args = parser.parse_args()

res = 0

bmi = args.weight / (args.height**2)
if bmi >= 18.5 and bmi <= 24.9:
    res += 1
if args.hsleep >= 7 and args.hsleep <= 8:
    res += 1
if args.meals >= 4 and args.meals <= 5:
    res += 1
if args.steps > 10000:
    res += 1
if args.fruvegs > 500:
    res += 1
if args.health_monitoring == 1:
    res += 1
if args.mood == "Good":
    res += 1
if args.when_happy == 0 or args.when_happy == 1:
    res += 1

if res == 8:
    print("Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!")
elif res >= 5 and res <= 7:
    print("Your health index is ", res, "/8, which means that you are on the right track!")
elif res <= 4:
    print("Your healthy lifestyle index is ", res, "/8 🤢, you need to rethink your healthy lifestyle!")
