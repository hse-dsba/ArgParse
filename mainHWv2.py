import argparse

parser = argparse.ArgumentParser(description='Some random Index calc')

parser.add_argument('-n','--name', type=str,default='Nameless',help='What is your name?')
parser.add_argument('-g','--gender', type=str,default='genderless',
                    help='What is your gender?',choices=['male','female'])
parser.add_argument('height',type=int,default=1,help='What is your height?')
parser.add_argument('weight',type=int,default=0,help='What is your weight?')
parser.add_argument('sleepTime',type=int,default=0,help='How long is your usual sleep?')
parser.add_argument('meals', type=int,default=0,help='How many meals do you take per day?')
parser.add_argument('fruit', type=str,default='No',help='Fruits per day?',
                    choices=['I do not eat these products regularly', 'Less than 500 grams', 'More than 500 grams'])
parser.add_argument('steps',type=int,default=0,help='Steps(thousands per day?')
parser.add_argument('health',type=str,default='No',help='Do you monitor your health?',
                    choices=['No','Yes, I have been undergoing medical examination in the last 3 years',
                             'Yes, but I do not see a doctor'])
parser.add_argument('mood',type=str,default='Bad',choices=['Good','Neutral','Bad'])
parser.add_argument('happiness',type=str,default='During the year',help='When was the last time you felt happy?',
                    choices=['During the week','During the Month','During the year'])

args = parser.parse_args()

index = 0

if args.weight != 0:
    BMI = args.weight / args.height**2
    if BMI >= 18.5 and BMI <= 24.9:
        index += 1

if args.sleepTime >=7 and args.sleepTime <=8:
    index += 1
if args.meals >=4 and args.meals <=5:
    index += 1
if args.fruit == 'More than 500 grams':
    index += 1
if args.steps >=10:
    index += 1
if args.health == 'Yes, I have been undergoing medical examination in the last 3 years':
    index += 1
if args.mood == 'Good':
    index += 1
if args.happiness == 'During the week':
    index += 1


if index == 8:
    print('Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!')
elif index >=5 and index <=7:
    print('Your health index is [5-7]/8, which means that you are on the right track!')
else: print('Your healthy lifestyle index is [0-4]/8 🤢, you need to rethink your healthy lifestyle!')


