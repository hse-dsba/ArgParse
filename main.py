import argparse
pars = argparse.ArgumentParser()
ans = 0
pars.add_argument('--name', help='Write your name', type=str)
pars.add_argument('--gender', help='Choose your gender: male, female', type=str, choices=['male', 'female'])
pars.add_argument('height', help='Write your height (m)', type=float)
pars.add_argument('weight', help='Write your weight (kg)', type=float)
pars.add_argument('SleepingHours', help='How much do you usually sleep?', type=int)
pars.add_argument('MealsAmount', help='How many meals does your daily diet include?', type=int)
pars.add_argument('FrVegAmount', help='''How many fresh fruits and vegetables do you eat during the day?
                          1 - I do not eat these products regularly;
                          2 - Less than 500 grams;
                          3 - More than 500 grams''', type=int)
pars.add_argument('steps', help='''How many steps do you walk on average per day?
                          1 - Less than 5 thousand steps;
                          2 - 5-10 thousand steps;
                          3 - More than 10 thousand steps''', type=int)
pars.add_argument('health', help='''Do you monitor your health? 
                          1 - No;
                          2 - Yes, I have been undergoing medical examination in the last 3 years; 
                          3 - Yes, but I do not see a doctor''', type=int)
pars.add_argument('mood', help='What is your mood today? Good, Neutral or Bad?', type=str, choices=['Good', 'Neutral', 
                                                                                                    'Bad'])
pars.add_argument('lt_state_happiness', help='''When was the last time you had a state of happiness? 
                          1 - During the week, 
                          2 - During the month, 
                          3 - During the year''', type=int)
args = pars.parse_args()
if 7 <= args.SleepingHours <= 8:
    ans += 1
if args.MealsAmount == 4 or args.MealsAmount == 5:
    ans += 1
if args.FrVegAmount == 3:
    ans += 1
if args.steps == 3:
    ans += 1
if args.health == 2:
    ans += 1
if args.mood == 1:
    ans += 1
if args.lt_state_happiness == 1:
    ans += 1
BMI = args.weight/(args.height*100*args.height)

if 18.5 <= BMI <= 24.9:
    ans += 1
if ans == 8:
    print('Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!')
if 5 <= ans <= 7:
    print('Your health index is', ans, '/8, which means that you are on the right track!')
if 0 <= ans <= 4:
    print('Your healthy lifestyle index is ', ans, '/8, you need to rethink your healthy lifestyle!')
