# How much is left to finish your pass?
from datetime import *


def how_much_to_finish_pass():
    # Take the current level pass of the user.
    while True:
        try:
            level_in_pass = int(input("What's you level in the pass? "))
            break
        except ValueError:
            print("This is not a number. Try again.\n")

    # Take the quantity of experience left to finish the current level
    while True:
        try:
            xp_need_in_level = int(input("How many points you need in this level? "))
            break
        except ValueError:
            print("Invalid input. Try again.\n")

    # Calculate the total XP in the current level for further use.
    xp_in_current_level = (level_in_pass * 1000 + 2000)

    # Initialize the variable for points needed to complete Pass.
    # Calculate total of points to complete Pass.
    points_needed = 0
    for total_exp in range(xp_in_current_level, 52001):
        if total_exp % 1000 == 0:
            points_needed += total_exp

    # Deduce XP already won in the current level.
    points_needed = points_needed - (xp_in_current_level - xp_need_in_level)

    # Output Points Needed
    print(f"\nYou need {points_needed} to complete the pass.")

    # Calculate and output days left to complete.
    today = date.today()
    pass_start_date = date(2020, 10, 13)
    pass_end_date = date(2021, 1, 12)
    diff = pass_end_date - today
    print(f"You have only {diff.days} days to complete.\n")

    # Calculate Total XP you still can get from daily rewards
    total_xp_from_daily_rewards = diff.days * 4000

    # Calculate Total XP you still can get from weekly rewards
    current_week = (today - pass_start_date) // 7
    # print(current_week)
    weeks_remaining = (diff.days // 7)
    # print(weeks_remaining)

    def total_xp_from_weekly_rewards():
        total = 0
        for week in range(int(current_week.days // 7), weeks_remaining + 1):
            if current_week <= 2:
                increment = 900  # Week 1 to week 2 the increment was 900
            else:
                increment = 1500  # Week 2 to week 3 the increment was 1500
            total += (5400 + (week * increment)) * 3
        return total

    # Output XP left from rewards.
    print(f"Experience left on Daily Rewards: {total_xp_from_daily_rewards}")
    print(f"Experience left on Weekly Rewards: {(total_xp_from_weekly_rewards())}\n")

    # Calculate Total XP from all rewards
    xp_from_rewards = total_xp_from_weekly_rewards() + total_xp_from_daily_rewards
    xp_left = points_needed - xp_from_rewards

    # Even getting all the rewards you still need to.
    print(f"Besides the Weekly and Daily Rewards, you need to play approximately: "
          f"\n{int(xp_left / 1000)} Spike Disputes Or,"
          f"\n{int(xp_left / 3000)} Normal/Competitive Matches")


while True:
    how_much_to_finish_pass()
    command = input(f"Finish?(y/n)")
    if command == 'y':
        break
    else:
        how_much_to_finish_pass()
