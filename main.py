import argparse

def get_args():

    parser = argparse.ArgumentParser(description='Testing healthy lifestyle index')

    parser.add_argument('--name', 
                        metavar='-n', 
                        type=str, 
                        dest='name',
                        nargs='?',
                        help='Write your name')

    parser.add_argument('--gender', 
                        metavar='-g', 
                        choices=['male', 'female', 'other'],
                        dest='gender',
                        nargs='?',
                        help='Choose your gender')

    parser.add_argument('--height', 
                        metavar='-h', 
                        type=int, 
                        dest='height',
                        required=True,
                        nargs='?',
                        help='Write your height (cm)')

    parser.add_argument('--weight', 
                        metavar='-w', 
                        type=int, 
                        dest='weight',
                        required=True,
                        nargs='?',
                        help='Write your weight (kg)')

    parser.add_argument('--sleep',
                        metavar='-s', 
                        choices=[' Less than 7 hours', 
                                '7-8 hours',
                                'More than 8 hours'], 
                        dest='sleep',
                        required=True,
                        nargs='?',
                        help='How much do you usually sleep?')

    parser.add_argument('--meals',
                        metavar='-m',
                        choices=['1 meal',
                                '2-3 meals',
                                '4-5 meals'],
                        dest='meals',
                        required=True,
                        nargs='?',
                        help='How many meals does your daily diet include?')
                        
    parser.add_argument('--diet',
                        metavar='-d',
                        choices=['I do not eat these products regularly', 
                                'Less than 500 grams', 
                                'More than 500 grams'],
                        dest='diet',
                        required=True,
                        nargs='?',
                        help='How many fresh fruits and vegetables do you eat during the day?')

    parser.add_argument('--steps',
                        metavar='-s',
                        choices=['Less than 5 thousand steps',
                                '5-10 thousand steps',
                                'More than 10 thousand steps'],
                        dest='steps',
                        required=True,
                        nargs='?',
                        help='How many steps do you walk on average per day?')

    parser.add_argument('--checkups',
                        metavar='-c',
                        choices=['No',
                                'Yes, I have been undergoing medical examination in the last 3 years',
                                'Yes, but I do not see a doctor'],
                        dest='checkups',
                        required=True,
                        nargs='?',
                        help='Do you monitor your health?')

    parser.add_argument('--mood',
                        metavar='-m',
                        choices=['Good',
                                'Neutral',
                                'Bad'],
                        dest='mood',
                        required=True,
                        nargs='?',
                        help='What is your mood today?')

    parser.add_argument('--happiness',
                        metavar='-h',
                        choices=['During the week', 
                                'During the month', 
                                'During the year'],
                        dest='happiness',
                        required=True,
                        nargs='?',
                        help='When was the last time you had a state of happiness?')

    args = parser.parse_args()

    return args

def get_points(args):

    points = 0

    if args.sleep == '7-8 hours':
      points += 1
    if args.meals == '4-5 meals':
      points += 1
    if args.diet == 'More than 500 grams':
      points += 1
    if args.steps == 'More than 10 thousand steps':
      points += 1
    if args.checkups == 'Yes, I have been undergoing medical examination in the last 3 years':
      points += 1
    if args.mood == 'Good':
      points += 1
    if args.happiness == 'During the week' or 'During the month':
      points += 1
    if 18.5 <= args.weight / (args.height*0.01)**2 <= 24.8:
      points += 1

    return points

def get_results(points):

    if points == 8:
      print('Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!')

    elif 5 <= points <= 7:
      print(f'Your index of a healthy lifestyle is {points}/8, which means that you are on the right track!')

    elif 0 <= points <= 4:
      print(f'Your index of a healthy lifestyle is {points}/8, which means that you need to rethink your healthy lifestyle!')

if __name__ == '__main__':

    args = get_args()
    points = get_points(args)
    get_results(points)