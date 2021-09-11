import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Calculate healthy lifestyle')
    parser.add_argument('--name', dest='name', metavar='-n', required=True, type=str, help="Your name")
    parser.add_argument('--gender', dest='gender', metavar='-g', required=True, choices=["male", "female"], help="Your gender")
    parser.add_argument('--height', dest='height', metavar='-h', required=True, type=int, help="Your height in cm")
    parser.add_argument('--weight', dest='weight', metavar='-w', required=True, type=int, help="Your weight in kg")
    parser.add_argument('--sleep', dest='sleep', metavar='-s', required=True, type=int, help="Your average sleep in hours")
    parser.add_argument('--meals', dest='meals', metavar='-m', required=True, type=int, help="Your average number of meals")
    parser.add_argument('--fruits', dest='fruits', metavar='-f', required=True, choices=["no", "less", "more"], help="Average amount of fruits [no | less than 500g | more than 500g]")
    parser.add_argument('--steps', dest='steps', metavar='-S', required=True, choices=["less", "average", "more"], help="Your average amount of steps [less 5k | average of 5-10K | more 10K]")
    parser.add_argument('--health', dest='health', metavar='-H', required=True, choices=["no", "examination", "yes"], help="Do you monitor your health [no | medical examination in last 3 years | yes]")
    parser.add_argument('--mood', dest='mood', metavar='-M', required=True, choices=["good", "neutral", "bad"], help="What is your mood today")
    parser.add_argument('--excitement', dest='excitement', required=True, metavar='-e', choices=["week", "month", "year"], help="When was the last time when you were happy")
    
    args = parser.parse_args()

    return args

def process_args(args):
    pts = 0

    bmi = args.weight / ((args.height / 100) ** 2)
    if bmi >= 18.5 and bmi <= 24.9:
        pts += 1
    if args.sleep == 7 or args.sleep == 8:
        pts += 1
    if args.meals == 4 or args.meals == 5:
        pts += 1
    if args.fruits == "more":
        pts += 1
    if args.steps == "more":
        pts += 1
    if args.health == "examination":
        pts += 1
    if args.mood == "good":
        pts += 1
    if args.excitement in ["week", "month"]:
        pts += 1

    return pts

def print_result(pts):
    if pts == 8:
        print("Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!")
    elif pts >= 5:
        print("Your health index is ", pts, "/8, which means that you are on the right track!", sep="")
    else:
        print("Your healthy lifestyle index is ", pts, "/8, you need to rethink your healthy lifestyle!", sep="")

def main():
    args = parse_args()
    pts = process_args(args)
    print_result(pts)


if __name__ == "__main__":
    main()

