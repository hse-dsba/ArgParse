import argparse
parser = argparse.ArgumentParser(description='Testing healthy lifestyle index')
parser.add_argument('height', type=int, help='Write your height')
parser.add_argument('weight', type=int, help='Write your weight')
parser.add_argument('sleep', type=int, help='How much do you usually sleep?')
parser.add_argument('meals', type=int, help='How many meals does your daily diet include?')
parser.add_argument('fruits', type=int, help='How many fresh fruits and vegetables do you eat during the day?')
parser.add_argument('steps', type=int, help='How many steps do you walk on average per day?')
parser.add_argument('monitoring_health', type=str, help='Do you monitor your health?'
                                                        'Have you been examined? How long ago?')
parser.add_argument('mood', type=str, help='What is your mood today?(Good, Neutral, Bad)')
parser.add_argument('happiness', type=str, help='When was the last time you had a state of happiness?'
                                                '(During the week, During the month, During the year')
args = parser.parse_args()
print(args.height, args.weight, args.sleep, args.meals, args.fruits, args.steps, args.monitoring_health, args.mood,
      args.happiness)