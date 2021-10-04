import argparse as a
parser = a.ArgumentParser()
parser.add_argument("--name", help="Write your name [optional]", type=str)
parser.add_argument("--gender", help="Choose your gender:", type=str, choices=["male", "female"])
parser.add_argument("height", help="Write your height (in cm)", type=int)
parser.add_argument("weight", help="Write your weight (in kg)", type=int)
parser.add_argument("sleep", help="How many hours do you usually sleep?", type=int)
parser.add_argument("meals", help="How many meals does your daily diet include?", type=int)
parser.add_argument("f_v", help="How many grams of fresh fruits and vegetables do you eat per day?", type=int)
parser.add_argument("steps", help="How many steps do you walk on average per day? (in thousands)", type=int)
parser.add_argument("health_m", help="Do you monitor your health? 1 - Not; 2 - Yes, I have been undergoing medical examination in the last 3 years; 3 - Yes, but I do not see a doctor", type=int)
parser.add_argument("mood", help="What is your mood today?", type=str, choices=["Good", "Neutral", "Bad"])
parser.add_argument("happiness", help="When was the last time you had a state of happiness? 1 - During the week; 2 - During the month; 3 - During the year", type=int)
arg = parser.parse_args()
k = 0
BMI = (arg.weight/(arg.height**2*0.0001))
if BMI>=18.5 and BMI<=24.9:
    k += 1
if arg.sleep>=7 and arg.sleep<=8:
    k += 1
if arg.meals==4 or arg.meals==5:
    k +=1
if arg.f_v >= 500:
    k += 1
if arg.steps >= 10:
    k += 1
if arg.health_m==2:
    k += 1
if arg.mood=="Good":
    k += 1
if arg.happiness!=3:
    k += 1
if k==8:
    print("Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!")
elif k>4:
    print("Your health index is " + str(k) + "/8, which means that you are on the right track!")
else:
    print("Your healthy lifestyle index is " + str(k) + "/8 (((, you need to rethink your healthy lifestyle!")