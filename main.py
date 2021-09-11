import argparse

parser = argparse.ArgumentParser(description='Testing healthy lifestyle index.')

indexSumm = 0

parser.add_argument('Name', help = 'Your name (Optional)')
parser.add_argument('Gender', help = 'Male/Female (Optional)')
parser.add_argument('Height', help = 'Enter your height - obligatory')
parser.add_argument('Weight', help = "Enter your weight - obligatory")
parser.add_argument('SleepHours', help = 'Home many hours do you sleep per day? <7/7-8/>8')
parser.add_argument('AmmountOfMeals', help = 'Home many meals do you take a day? 1/2-3/4-5')
parser.add_argument('AmmountFreshFruit', help = 'How many fresh fruits do you eat per day? <?> 500 g')
parser.add_argument('Steps', help = 'How many steps do you make per day? <5k/5-10k/>10k')
parser.add_argument('HealthMonitoring', help = 'Do you monitor your health? ')



args = parser.parse_args()

print(args.Name, args.Gender)


