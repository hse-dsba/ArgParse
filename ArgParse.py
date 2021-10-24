import argparse
index=0
#Setting up Argparse
parser = argparse.ArgumentParser(prog='HLI', description='Healthy Lifestyle Index')
parser.add_argument('Name', help='Write your name',default='Person')
parser.add_argument('Gender',help='Choose your gender: male, female',choices=['male','female', 'Person'], default='Person')
parser.add_argument('Height', type=int, help='Write your height (cm):')
parser.add_argument('Weight', type=int, help='Write your weight (kg)')

parser.add_argument('Sleeping_time', help='How much do you usually sleep? A:Less than 7 hours. B:7-8 hours. C:More than 8 hours.')
parser.add_argument('Number_of_daily_meals',help='How many meals does your daily diet include? A:1 meal. B:2-3 meals. C:4-5 meals.')
parser.add_argument('Daily_FruitVeg', help='How many fresh fruits and vegetables do you eat during the day? A:I do not eat those products regularly. B:Less than 500 grams. C:More than 500 grams')
parser.add_argument('Daily_Steps', help='How many steps do you walk on average per day? A:Less than 5000 steps. B:5-10 thousand steps. C:More than 10 thousand steps.')
parser.add_argument('Monitor_Health', help='Do you monitor your health? A:Not B:Yes, I have been undergoing medical examination in the last 3 years C:Yes, but I do not see a doctor')
parser.add_argument('Mood_Today', help='What is your mood today? A:Good (1 point) B:Neutral C:Bad [choices]',choices=['A','B','C'])
parser.add_argument('State_of_Happiness',help='When was the last time you had a state of happiness? A:During the week  B:During the month, C:During the year.')

#Data processing
var = parser.parse_args()
BMI = 100*(var.Weight/(var.Height*2))
if BMI>=18.5 and BMI<=24.9:
    index = index+1
if var.Sleeping_time =='B':
    index = index + 1
if var.Number_of_daily_meals =='C':
    index = index + 1
if var.Daily_FruitVeg == 'C':
    index = index + 1
if var.Daily_Steps == 'C':
    index = index + 1
if var.Monitor_Health == 'B':
    index = index + 1
if var.Mood_Today =='A':
    index = index + 1
if var.State_of_Happiness =='A' or 'B':
    index = index + 1
#Result
if index == 8:
    print("Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!")
if 4<index<8:
    print("Your health index is [5-7]/8, which means that you are on the right track! ")
if index<=4:
    print("Your healthy lifestyle index is [0-4]/8 🤢, you need to rethink your healthy lifestyle!")