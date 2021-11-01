import argparse


def main():
    parserr = argparse.ArgumentParser()
    parserr.add_argument("gender",
                         help="Choose your gender: male, female", type=str, choices=["male", "female"])
    parserr.add_argument("height",
                         help="Write your height (cm)", type=int)
    parserr.add_argument("weight",
                         help="Write your weight (kg)", type=int)
    parserr.add_argument("sleeping_time",
                         help="How much do you usually sleep?"
                              " Less than 7 hours; 7-8 hours; More than 8 hours", type=int)
    parserr.add_argument("meals",
                         help="How many meals does your daily diet include? 1 meal, 2-3 meals, 4-5 meals", type=int)
    parserr.add_argument("fruits",
                         help="How many fresh fruits"
                              " and vegetables do you eat during the day? 1) "
                              "I do not eat these products regularly 2)Less than 500 grams 3)More than 500 grams ",
                         type=int)
    parserr.add_argument("steps",
                         help="How many steps do you walk on average per day?"
                              " 1)Less than 5 thousand steps 2)5-10 thousand steps 3)More than 10 thousand steps",
                         type=int)
    parserr.add_argument("health",
                         help="Do you monitor your health?"
                              " 1)Not 2)Yes, I have been undergoing medical examination in the last 3 years"
                              " 3)Yes, but I do not see a doctor;",
                         type=int)
    parserr.add_argument("mood", help="What is your mood today?", type=str, choices=["Good", "Neutral", "Bad"])
    parserr.add_argument("happiness",
                         help="When was the last time you had a state of happiness?"
                              " 1)During the week 2)During the month 3)During the year.",
                         type=int)
    args = parserr.parse_args()
    index1 = 0
    if 7 <= args.sleeping_time <= 8:
        index1 += 1
    if args.meals == 4 or args.meals == 5:
        index1 += 1
    if args.fruits == 3:
        index1 += 1
    if args.steps == 3:
        index1 += 1
    if args.health == 2:
        index1 += 1
    if args.mood == "Good":
        index1 += 1
    if args.happiness == 1:
        index1 += 1
    BLM = args.weight / (args.height * args.height)
    if 18.5 <= BLM <= 24.9:
        index1 += 1
    if index1 == 8:
        print(
            "Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!")
    if 5 <= index1 and index1 <= 7:
        print("Your health index is (5-7)/8, which means that you are on the right track!")
    if 0 <= index1 and index1 <= 4:
        print("Your healthy lifestyle index is (0-4)/8, you need to rethink your healthy lifestyle!")


if __name__ == '__main__':
    main()
