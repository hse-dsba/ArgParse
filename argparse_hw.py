import argparse

res = 0
parser = argparse.ArgumentParser(description='Testing healthy lifestyle index')
parser.add_argument('Name', type=str, help='Write your name')
parser.add_argument('Gender', type=str, help='Male - 1; female - 0')
parser.add_argument('Height', type=int, help='Write your height(cm)')
parser.add_argument('Weight', type=int, help='Write your weight(kg)')
parser.add_argument('Sleep', type=int, help='How much do you usually sleep?(hours)')
parser.add_argument('Meals', type=int, help='How many meals does your daily diet include?')
parser.add_argument('Fruitsvegetables', type=int,
                    help='How many fresh fruits and vegetables do you eat during the day?(grams)')
parser.add_argument('Steps', type=int, help='How many steps do you walk on average per day? ')
parser.add_argument('Monitoringyourhealth', type=str,
                    help='Do you monitor your health?(Not; YesIhavebeenundergoingmedicalexaminationinthelast3years, YesbutIdonotseeadoctor)')
parser.add_argument('Mood', type=int, help='What is your mood today?(good - 1; bad - 0)')
parser.add_argument('Hapiness', type=str,
                    help='When was the last time you had a state of happiness?(Duringtheweek, duringthemonth, duringtheyear')
args = parser.parse_args()
rost = args.Height / 100
bmi = args.Weight / (rost * rost)
if args.Sleep >= 7 and args.Sleep <= 8:
    res += 1
if args.Meals >= 4 and args.Meals <= 5:
    res += 1
if args.Fruitsvegetables > 500:
    res += 1
if args.Steps > 10000:
    res += 1
if args.Monitoringyourhealth == 'YesIhavebeenundergoingmedicalexaminationinthelast3years ':
    res += 1
if args.Mood == 1:
    res += 1
if args.Hapiness == 'Duringtheweek' or args.Hapiness == 'duringthemonth':
    res += 1
if bmi >= 18.5 and bmi <= 24.9:
    res += 1
if res == 8:
    print('Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!')
if res >= 5 and res <= 7:
    print(res,'points Your health index is',res,'/8, which means that you are on the right track!')
if res >= 0 and res <= 4:
    print(res,'points Your healthy lifestyle index is',res,'/8 🤢, you need to rethink your healthy lifestyle!')
