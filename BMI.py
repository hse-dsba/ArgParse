import argparse

# a = first answer, b = second answer, c = third answer

parser = argparse.ArgumentParser(description='Calculate and test your BMI (Body Mass Index)')
parser.add_argument('-n', '--name', type=str, metavar = '', required=False, help='Your name')
parser.add_argument('-g', '--gender', type=str, metavar = '', choices=['male', 'female', 'other'], required=False, help='Your gender')
parser.add_argument('-H', '--height', type=float, metavar = '', required=True, help='Your height in cm')
parser.add_argument('-w', '--weight', type=float, metavar = '', required=True, help='Your weight in kg')
parser.add_argument('-s', '--sleep', type=str, metavar = '', choices=['a', 'b', 'c'], required=True, help='How much do you usually sleep? a - Less than 7 hours; b - 7-8 hours; c - More than 8 hours;')
parser.add_argument('-m', '--meals', type=str, metavar = '', choices=['a', 'b', 'c'], required=True, help='How many meals does your daily diet include? a - 1 meal; b - 2-3 meals; c - 4-5 meals;')
parser.add_argument('-f', '--fruits', type=str, metavar = '', choices=['a', 'b', 'c'], required=True, help='How many fresh fruits and vegetables do you eat during the day? a - I do not eat these products regularly; b - Less than 500 grams; c - More than 500 grams;')
parser.add_argument('-st', '--steps', type=str, metavar = '', choices=['a', 'b', 'c'], required=True, help='How many steps do you walk on average per day? a - Less than 5 thousand steps; b - 5-10 thousand steps; c - More than 10 thousand steps;')
parser.add_argument('-e', '--health', type=str, metavar = '', choices=['a', 'b', 'c'], required=True, help='Do you monitor your health? a - Not; b - Yes, I have been undergoing medical examination in the last 3 years; c - Yes, but I do not see a doctor;')
parser.add_argument('-mo', '--mood', type=str, metavar = '', choices=['a', 'b', 'c'], required=True, help='What is your mood today? a - Good, b - Neutral, c - Bad;')
parser.add_argument('-a', '--happiness', type=str, metavar = '', choices=['a', 'b', 'c'], required=True, help='When was the last time you had a state of happiness? a - During the week; b - During the month; c - During the year.')
args = parser.parse_args()

def BMI(name, gender, height, weight, sleep, meals, fruits, steps, health, mood, happiness):
    #print("Hey, it is correct till this point :)")
    counter = 0
    if sleep == 'b':
        counter += 1
    if meals == 'c':
        counter += 1
    if fruits == 'c':
        counter += 1
    if steps == 'c':
        counter += 1
    if health == 'b':
        counter += 1
    if mood == 'a':
        counter += 1
    if happiness == 'a'or happiness == 'b':
        counter += 1
    bmi = weight / height**2
    if 18.5 <= bmi <= 24.9:
        counter += 1
    if counter == 8: 
        print("Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!")
    if 5 <= counter <= 7: 
        print("Your health index is %s/8, which means that you are on the right track!" % counter)
    if 0 <= counter <= 4:
        print("Your healthy lifestyle index is %s/8 🤢, you need to rethink your healthy lifestyle!" % counter)
    
    
if __name__ == '__main__':
    BMI(args.name, args.gender, args.height, args.weight, args.sleep, args.meals, args.fruits, args.steps, args.health, args.mood, args.happiness)