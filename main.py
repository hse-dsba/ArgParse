import argparse

parser = argparse.ArgumentParser(description='Testing healthy lifestyle index.')

indexSumm = 0

parser.add_argument('Name', help = 'Your name (Optional). Very Important to answer directly like the answers are written!!')
parser.add_argument('Gender', help = 'Male/Female (Optional)')
parser.add_argument('Height', help = 'Enter your height - obligatory')
parser.add_argument('Weight', help = "Enter your weight - obligatory")
parser.add_argument('SleepHours', help = 'Home many hours do you sleep per day? -7/8/9')
parser.add_argument('AmmountOfMeals', help = 'Home many meals do you take a day? 1/3/5')
parser.add_argument('AmmountFreshFruit', help = 'How many fresh fruits do you eat per day? 300/500 ')
parser.add_argument('Steps', help = 'How many steps do you make per day? 5/7/10')
parser.add_argument('HealthMonitoring', help = 'Do you monitor your health? 0/1/0.5')
parser.add_argument('Mood', help = 'Which mood? 1/0/-1')
parser.add_argument('LastTimeHappy', help = 'Week/Month/Year')

args = parser.parse_args()

BMI = int(args.Weight) / int((args.Height)) ** 2

if BMI >= 18.5 and BMI <= 24.9:
    indexSumm += 1
if args.SleepHours == '8':
    indexSumm += 1
if args.AmmountOfMeals == '5':
    indexSumm += 1
if args.AmmountOfMeals == '500':
    indexSumm += 1
if args.Steps == '10':
    indexSumm += 1
if args.HealthMonitoring == '1':
    indexSumm += 1
if args.Mood == '1':
    indexSumm += 1
if args.LastTimeHappy == 'Week':
    indexSumm += 1


print('Yours healthy lifestyle Index is', indexSumm)


