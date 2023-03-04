#verison 2
#The ROI (return on investment) is defined as (earnings - expenses)/expenses. 
#Calculate your ROI, print it out along with your earnings and expenses.

import random

winning_numbers = random.sample(range(0,20),6)

def num_matches(winning_numbers, user_numbers):
    matches = 0
    for i in range(6):
        if winning_numbers[i] == user_numbers[i]:
            matches += 1
    return matches

winnings = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 5000,
    5: 1000000,
    6: 25000000

}

expenses = 0
earnings = 0

for pick6 in range(100000):
    user_numbers = random.sample(range(1,99),6) 
    match_count = num_matches(winning_numbers, user_numbers) 
    earnings += winnings.get(match_count) 
    expenses += 2


final_total = earnings - expenses  
print(f'Your balance is {final_total}')



return_on_investment = (earnings - expenses)/expenses

print(f"Your ROI is $ {return_on_investment} per ticket")