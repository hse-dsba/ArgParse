import argparse

parser = argparse.ArgumentParser(description='Testing healthy lifestyle index')

parser.add_argument('--name', type=str, default="Bob", help='Write your name (default: Bob)')
parser.add_argument('--gender', type=str, default="male", choices=['male', 'female'], help='Choose your gender')
parser.add_argument('height', type=float, help='Write your height')
parser.add_argument('weight', type=float, help='Write your weight')
parser.add_argument('sleep', type=int, help='How much do you usually sleep?')
parser.add_argument('food', type=int, help='How many meals does your daily diet include?')
parser.add_argument('fruits', type=int, help='How many fresh fruits and vegetables do you eat during the day?(grams)')
parser.add_argument('steps', type=float, help='How many steps do you walk on average per day?')
parser.add_argument('health', type=str,
                    choices=['Not', 'Yes, I have been undergoing medical examination in the last 3 years',
                             'Yes, but I do not see a doctor'], help='Do you monitor your health?')
parser.add_argument('mood', choices=['Good', 'Neutral', 'Bad'], type=str, help='What is your mood today?')
args = parser.parse_args()

result = 0
if 7 <= args.sleep <= 8:
    result += 1
if 4 <= args.food <= 5:
    result += 1
if args.fruits >= 500:
    result += 1
if args.steps > 10000:
    result += 1
if args.health == 'Yes, I have been undergoing medical examination in the last 3 years':
    result += 1
BIM = args.weight / (args.height / 100) ** 2
if 18.5 <= BIM <= 24.9:
    result += 1
if result == 8:
    print("Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!")
elif result >= 5:
    print("Your health index is [5-7]/8, which means that you are on the right track!")
else:
    print("Your healthy lifestyle index is [0-4]/8 🤢, you need to rethink your healthy lifestyle!")
print(args.indir)
