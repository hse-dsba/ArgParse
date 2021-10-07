import argparse

parser = argparse.ArgumentParser()

def results(args):
    counter = 0
    userName = ''
    bmi = args.w / (args.h / 100 * args.h / 100)
    print("Your BMI is", bmi)
    if 18.5 <= bmi <= 24.9:
        counter += 1
    if args.name is not None:
        userName = args.name

    if args.sleep == 2:
        counter += 1
    if args.dailyDiet == 3:
        counter += 1
    if args.freshFruits == 3:
        counter += 1
    if args.walk == 3:
        counter += 1
    if args.healthMonitor == 2:
        counter += 1
    if args.todaysMood == 'Good':
        counter += 1
    if args.happiness == 1 or args.happiness == 2:
        counter += 1

    if counter == 8:
        print(userName,
              'Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy '
              'lifestyle!')
    elif 5 <= counter <= 7:
        print(userName, 'Your health index is {}/8, which means that you are on the right track!'.format(counter))
    elif 0 <= counter <= 4:
        print(userName,
              'Your healthy lifestyle index is {}/8 🤢, you need to rethink your healthy lifestyle!'.format(counter))
    return 0



def term():
    global parser
    parser.add_argument('-n', '--name', help="[Optional] Type your name", type=str)
    parser.add_argument('-g', '--gender', help="[Optional] Type your gender", choices=["Male", "Female"], type=str)
    parser.add_argument('h', help="Type your height", type=int)
    parser.add_argument('w', help="Type your weight", type=float)
    parser.add_argument('sleep', help="How much do you usually sleep? 1. Less than 7 hours; 2. 7-8 hours; 3. More "
                                      "than 8 hours", type=int, choices=[1, 2, 3])
    parser.add_argument('dailyDiet', help='How many meals does your daily diet include? 1. 1 meal, 2. 2-3 meals, '
                                          '3. 4-5 meals', type=int, choices=[1, 2, 3])
    parser.add_argument("freshFruits", help="How many fresh fruits and vegetables do you eat during the day? 1. I do "
                                            "not eat these products regularly; 2. Less than 500 grams; 3. More than 500"
                                            " grams", type=int, choices=[1, 2, 3])
    parser.add_argument('walk', help='How many steps do you walk on average per day? 1. Less than 5 thousand steps, '
                                     '2. 5-10 thousand steps, 3. More than 10 thousand steps', type=int,
                        choices=[1, 2, 3])
    parser.add_argument('healthMonitor', help="Do you monitor your health? 1. No; 2. Yes, I have been undergoing "
                                              "medical examination in the last 3 years, 3. Yes, but I do not see a "
                                              "doctor", type=int, choices=[1, 2, 3])
    parser.add_argument('todaysMood', help="What is your mood today? 1. Good, Neutral, Bad [choices]", type=str,
                        choices=['Bad', 'Good', 'Neutral'])
    parser.add_argument('happiness', help="When was the last time you had a state of happiness? 1. During the week, "
                                          "2. During the month, 3. During the year", type=int, choices=[1, 2, 3])
    args = parser.parse_args()
    results(args)


def PyCharm():
    global parser
    unness = []
    ness = []
    print("If something is optional, type -")

    print("Type your name [Optional]")
    parser.add_argument('-n', '--name', help="[Optional] Type your name", type=str)
    pycharm_input = input()
    if pycharm_input != '-':
        unness.append('-n')
        unness.append(pycharm_input)

    print("Type your gender: Male or Female (in the same way) [Optional]")
    parser.add_argument('-g', '--gender', choices=["Male", "Female"], type=str)
    pycharm_input = input()
    if pycharm_input != '-':
        unness.append('-g')
        unness.append(pycharm_input)

    print("Type your height (cm, integer)")
    parser.add_argument('h', type=int)
    pycharm_input = input()
    ness.append(pycharm_input)

    print("Type your weight (kg, float)")
    parser.add_argument('w', type=float)
    pycharm_input = input()
    ness.append(pycharm_input)

    print("How much do you usually sleep? (Type the number of answer)")
    print("1. Less than 7 hours")
    print("2. 7-8 hours")  # 1 point
    print("3. More than 8 hours")
    parser.add_argument('sleep', type=int, choices=[1, 2, 3])
    pycharm_input = input()
    ness.append(pycharm_input)

    print("How many meals does your daily diet include? (Type the number of answer)")
    print("1. 1 meal")
    print("2. 2-3 meals")
    print("3. 4-5 meals")  # 1 point
    parser.add_argument('dailyDiet', type=int, choices=[1, 2, 3])
    pycharm_input = input()
    ness.append(pycharm_input)

    print("How many fresh fruits and vegetables do you eat during the day? (Type the number of answer)")
    print("1. I do not eat these products regularly")
    print("2. Less than 500 grams")
    print("3. More than 500 grams")  # 1 point
    parser.add_argument('freshFruits', type=int, choices=[1, 2, 3])
    pycharm_input = input()
    ness.append(pycharm_input)

    print("How many steps do you walk on average per day? (Type the number of answer)")
    print("1. Less than 5 thousand steps")
    print("2. 5-10 thousand steps")
    print("3. More than 10 thousand steps")  # 1 point
    parser.add_argument('walk', type=int, choices=[1, 2, 3])
    pycharm_input = input()
    ness.append(pycharm_input)

    print("Do you monitor your health? (Type the number of answer)")
    print("1. No")
    print("2. Yes, I have been undergoing medical examination in the last 3 years")  # 1 point
    print("3. Yes, but I do not see a doctor")
    parser.add_argument('healthMonitor', type=int, choices=[1, 2, 3])
    pycharm_input = input()
    ness.append(pycharm_input)

    print("What is your mood today? (Type the answer)")
    print("1. Bad")
    print("2. Good")  # 1 point
    print("3. Neutral")
    parser.add_argument('todaysMood', type=str, choices=['Bad', 'Good', 'Neutral'])
    pycharm_input = input()
    ness.append(pycharm_input)

    print("When was the last time you had a state of happiness?  (Type the number of answer)")
    print("1. During the week")  # 1 point
    print("2. During the month")  # 1 point
    print("3. During the year")
    parser.add_argument('happiness', type=int, choices=[1, 2, 3])
    pycharm_input = input()
    ness.append(pycharm_input)

    print("CALCULATING YOUR BMI...")
    res = unness + ness
    args = parser.parse_args(res)
    results(args)
    return 0

if __name__ == "__main__":
    print("Choose your warrior:")
    print("1. IDE guy")
    print("2. Terminal lover (you gotta write info before this question)")
    if int(input()) == 1:
        PyCharm()
    else:
        term()