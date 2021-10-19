import argparse


def main():
    pars = argparse.ArgumentParser()
    points = 0
    pars.add_argument("--name", help="Write your name", type=str)
    pars.add_argument("--gender", help="Choose your gender: male, female", type=str, choices=["male", "female"])
    pars.add_argument("height", help="Write your height (cm)", type=float)
    pars.add_argument("weight", help="Write your weight (kg)", type=float)
    pars.add_argument("sleeping_hours", help="How much do you usually sleep?", type=int)
    pars.add_argument("number_meals", help="How many meals does your daily diet include?", type=int)
    pars.add_argument("fruits_vegetables", help="""How many fresh fruits and vegetables do you eat during the day?
                          1 - I do not eat these products regularly;
                          2 - Less than 500 grams;
                          3 - More than 500 grams""",
                      type=int)
    pars.add_argument("steps", help="""How many steps do you walk on average per day?
                          1 - Less than 5 thousand steps;
                          2 - 5-10 thousand steps;
                          3 - More than 10 thousand steps""", type=int)
    pars.add_argument("health",
                      help="""Do you monitor your health? 
                          1 - No; 
                          2 - Yes, I have been undergoing medical examination in the last 3 years; 
                          3 - Yes, but I do not see a doctor""",
                      type=int)
    pars.add_argument("mood", help="What is your mood today? Good, Neutral or Bad?", type=str,
                      choices=["Good", "Neutral", "Bad"])
    pars.add_argument("lt_state_happiness",
                      help="""When was the last time you had a state of happiness? 
                          1 - During the week, 
                          2 - During the month, 
                          3 - During the year""",
                      type=int)
    args = pars.parse_args()
    if 7 <= args.sleeping_hours <= 8:
        points += 1
    if args.number_meals == 4 or args.number_meals == 5:
        points += 1
    if args.fruits_vegetables == 3:
        points += 1
    if args.steps == 3:
        points += 1
    if args.health == 2:
        points += 1
    if args.mood == 1:
        points += 1
    if args.lt_state_happiness == 1:
        points += 1
    BMI = args.weight/(args.height*args.height)

    if 18.5 <= BMI <= 24.9:
        points += 1
    if points == 8:
        print('Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!')
    if 5 <= points <= 7:
        print('Your health index is [5-7]/8, which means that you are on the right track!')
    if 0 <= points <= 4:
        print('Your healthy lifestyle index is [0-4]/8, you need to rethink your healthy lifestyle!')


if __name__ == '__main__':
    main()