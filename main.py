import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="Write your name", type=str)
parser.add_argument("--gender", help="Choose your gender: male, female", choices=["male", "female"], type=str)
parser.add_argument("height", help="Write your height (cm)", type=float)
parser.add_argument("weight", help="Write your weight (kg)", type=float)
parser.add_argument("sleep", help="""How much do you usually sleep?
                                      1. Less than 7 hours
                                      2. 7-8 hours
                                      3. More than 8 hours""", type=int)
parser.add_argument("meals", help="""How many meals does your daily diet include?
                                      1. 1 meal
                                      2. 2-3 meals
                                      3. 4-5 meals""", type=int)
parser.add_argument("vegetables", help="""How many fresh fruits and vegetables do you eat during the day?
                                      1. I do not eat these products regularly
                                      2. Less than 500 grams
                                      3. More than 500 grams""", type=int)
parser.add_argument("steps", help="""How many steps do you walk on average per day?
                                      1. Less than 5 thousand steps
                                      2. 5-10 thousand steps
                                      3. More than 10 thousand steps""", type=int)
parser.add_argument("health", help="""Do you monitor your health?
                                      1. Not
                                      2. Yes, I have been undergoing medical examination in the last 3 years
                                      3. Yes, but I do not see a doctor""", type=int)
parser.add_argument("mood", help="What is your mood today? Good, Neutral or Bad?", choices=["Good", "Neutral", "Bad"],
                    type=str)
parser.add_argument("happiness", help="""When was the last time you had a state of happiness?
                                      1. During the week
                                      2. During the month
                                      3. During the year""", type=int)
arg = parser.parse_args()
index_of_healthy_lifestyle = 0
BMI = arg.weight / (arg.height ** 2)
if 24.9 >= BMI >= 18.5:
    index_of_healthy_lifestyle += 1
if arg.sleep == 2:
    index_of_healthy_lifestyle += 1
if arg.meals == 3:
    index_of_healthy_lifestyle += 1
if arg.vegetables == 3:
    index_of_healthy_lifestyle += 1
if arg.steps == 3:
    index_of_healthy_lifestyle += 1
if arg.health == 2:
    index_of_healthy_lifestyle += 1
if arg.mood == "Good":
    index_of_healthy_lifestyle += 1
if arg.happiness == 1 or arg.happiness == 2:
    index_of_healthy_lifestyle += 1

if index_of_healthy_lifestyle == 8:
    print("Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!")
if 7 >= index_of_healthy_lifestyle >= 5:
    print("Your health index is", index_of_healthy_lifestyle, "/8, which means that you are on the right track!")
if 4 >= index_of_healthy_lifestyle >= 0:
    print("Your healthy lifestyle index is", index_of_healthy_lifestyle,
          "/8, you need to rethink your healthy lifestyle!")