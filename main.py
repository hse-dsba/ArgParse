import argparse as arg

parser = arg.ArgumentParser()

parser.add_argument("--name", help="Write your name [optional]", type=str)
parser.add_argument("--gender", help="Choose your gender: male, female", type=str, choices=["male", "female"])

parser.add_argument("height", help="Write your height (cm)", type=int)
parser.add_argument("weight", help="Write your weight (kg)", type=int)
parser.add_argument("sleep", help="How much do you usually sleep? (hours)", type=int)
parser.add_argument("meal", help="How many meals does your daily diet include? (meals)", type=int)
parser.add_argument("fnv", help="How many fresh fruits and vegetables do you eat during the day? (grams)", type=int)
parser.add_argument("steps", help="How many steps do you walk on average per day? (steps)", type=int)
parser.add_argument("health_monitor", help="Do you monitor your health? 0 - Not; 1 - Yes, I have been undergoing medical examination in the last 3 years (1 point), 2 - Yes, but I do not see a doctor", type=int)
parser.add_argument("mood", help="What is your mood today? Good (1 point), Neutral, Bad", type=str, choices=["Good", "Neutral", "Bad"])
parser.add_argument("happy", help="When was the last time you had a state of happiness? 0 - During the week (1 point), 1 - During the month (1 point), 2 - During the year.", type=int)

args = parser.parse_args()

ans = 0

bmi = float(args.weight / (args.height ** 2))
if (bmi >= 18.5 and bmi <= 24.9):
    ans += 1

ans += args.sleep >= 7 and args.sleep <= 8
ans += 4 <= args.meal and args.meal <= 5
ans += args.fnv > 500
ans += args.steps > 10000
ans += args.health_monitor == 2
ans += args.mood == "Good"
ans += args.happy <= 1

if (ans == 8):
    print("Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle! ")
elif (ans >= 5):
    print("Your health index is " + str(ans) + "/8, which means that you are on the right track! ")
else:
    print("Your healthy lifestyle index is " + str(ans) + "/8 🤢, you need to rethink your healthy lifestyle!")
