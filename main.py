import argparse
import re


def healthy_lifestyle_index(height, weight, sleep, meals, fruits, steps, monitoring_health, mood, happiness, HLI):
    monitoring_health.lower()
    mood.lower()
    happiness.lower()

    body_mass_index = weight / (height ** 2)

    if 18.5 <= body_mass_index <= 24.9:
        HLI += 1
    if sleep == 7 or sleep == 8:
        HLI += 1
    if meals == 4 or meals == 5:
        HLI += 1
    if fruits >= 500:
        HLI += 1
    if steps >= 10000:
        HLI += 1
    if 'no' in monitoring_health:
        pass
    else:
        num_years = re.findall(r'\d+', monitoring_health)
        if int(num_years[0]) <= 3:
            HLI += 1
    if mood == 'good':
        HLI += 1
    if 'month' in happiness or 'week' in happiness:
        HLI += 1
    return HLI


parser = argparse.ArgumentParser(description='Testing healthy lifestyle index')
parser.add_argument('height', type=int, help='Write your height')
parser.add_argument('weight', type=int, help='Write your weight')
parser.add_argument('sleep', type=int, help='How much do you usually sleep?')
parser.add_argument('meals', type=int, help='How many meals does your daily diet include?')
parser.add_argument('fruits', type=int, help='How many fresh fruits and vegetables do you eat during the day?')
parser.add_argument('steps', type=int, help='How many steps do you walk on average per day?')
parser.add_argument('monitoring_health', type=str, help='Do you monitor your health?'
                                                        'Have you been examined? How long ago?(years)')
parser.add_argument('mood', type=str, help='What is your mood today?(Good, Neutral, Bad)')
parser.add_argument('happiness', type=str, help='When was the last time you had a state of happiness?'
                                                '(During the week, During the month, During the year')
args = parser.parse_args()


your_index = int(healthy_lifestyle_index(args.height, args.weight, args.sleep, args.meals, args.fruits, args.steps,
                                         args.monitoring_health, args.mood,args.happiness, 0))

if your_index == 8:
    print('Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!')
elif 5 <= your_index <= 7:
    print('Your health index is [5-7]/8, which means that you are on the right track!')
else:
    print('Your healthy lifestyle index is [0-4]/8 🤢, you need to rethink your healthy lifestyle!')




