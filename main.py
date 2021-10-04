import argparse

pars = argparse.ArgumentParser()
pars.add_argument("--name", help="Write your name", type=str)
pars.add_argument("--gender", help="Choose your gender: male, female", type=str,
                  choices=["male", "female"])
pars.add_argument("h", help="Write your height (cm)", type=float)
pars.add_argument("w", help="Write your weight (kg)", type=float)
pars.add_argument("s", help="How much do you usually sleep?", type=int)
pars.add_argument("f", help="How many meals does your daily diet include?", type=int)
pars.add_argument("hf", help="""How many fresh fruits and vegetables do you eat during the day?
                       1 - I do not eat these products regularly;
                       2 - Less than 500 grams;
                       3 - More than 500 grams""",
                  type=int)
pars.add_argument("st", help="""How many steps do you walk on average per day?
                       1 - Less than 5 thousand steps;
                       2 - 5-10 thousand steps;
                       3 - More than 10 thousand steps""", type=int)
pars.add_argument("hl",
                  help="""Do you monitor your health? 
                       1 - No; 
                       2 - Yes, I have been undergoing medical examination in the last 3 years; 
                       3 - Yes, but I do not see a doctor""",
                  type=int)
pars.add_argument("mood", help="What is your mood today? Good, Neutral or Bad?", type=str,
                  choices=["Good", "Neutral", "Bad"])
pars.add_argument("happy",
                  help="""When was the last time you had a state of happiness? 
                       1 - During the week, 
                       2 - During the month, 
                       3 - During the year""",
                  type=int)
arg = pars.parse_args()

count = 0
BMI = arg.w / arg.h * arg.h
if BMI >= 18.5 and BMI <= 24.9:
    count += 1
if arg.s <= 7 and arg.s >= 8:
    count += 1
if arg.f == 4 or arg.f == 5:
    count += 1
if arg.hf > 500:
    count += 1
if arg.st >= 10:
    count += 1
if arg.hl == 2:
    count += 1
if arg.mood == 'Good':
    count += 1
if arg.happy != 3:
    count += 1
if count == 8:
    print('Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!')
elif count == 5:
    print('Your health index is 5/8, which means that you are on the right track!')
elif count == 6:
    print('Your health index is 6/8, which means that you are on the right track!')
elif count == 7:
    print('Your health index is 7/8, which means that you are on the right track!')
elif count == 4:
    print('Your healthy lifestyle index is 4/8, you need to rethink your healthy lifestyle!')
elif count == 3:
    print('Your healthy lifestyle index is 3/8, you need to rethink your healthy lifestyle!')
elif count == 2:
    print('Your healthy lifestyle index is 2/8, you need to rethink your healthy lifestyle!')
elif count == 1:
    print('Your healthy lifestyle index is 1/8, you need to rethink your healthy lifestyle!')
elif count == 0:
    print('Your healthy lifestyle index is 0/8, you need to rethink your healthy lifestyle!')