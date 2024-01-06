from art import logo 
from game_data import data
from art import vs
import random
import os
import sys 

final_score =0
compare_A = data[random.randint(0,len(data)-1)]

def compare(dic_a, dic_b):
    """Expect 2 dictionary, to compare their follower_count, return the dictionary which has bigger counts, 0 if equal"""
    if dic_a["follower_count"]< dic_b["follower_count"]:
        return dic_b
    elif dic_a["follower_count"]> dic_b["follower_count"]:
        return dic_a
    else:
        return 0

os.system('clear')
print(logo)

def process():

    victory = True
    while victory == True:
        global compare_A
        global final_score
        compare_B = data[random.randint(0,len(data)-1)]
        while compare_B == compare_A: 
            compare_B = data[random.randint(0,len(data)-1)]

        #Compare A: David Beckham, a Footballer, from United Kingdom.
        print(f"Compare A: {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}")
        print(vs)

        #Against B: Instagram, a Social media platform, from United States.
        #Who has more followers? Type 'A' or 'B': 
        print(f"Aganist B: {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}")
        choose = input("Who has more followers? Type 'A' or 'B': ").lower()

        larger_follower_count =0
        if compare(compare_A,compare_B) == compare_A:
            larger_follower_count = "a"
        elif compare(compare_A,compare_B) == compare_B:
            larger_follower_count = "b"

        if larger_follower_count==0:
            print(logo)
            print("it's a tie")
            victory = True
            process()
            compare_A = compare_B
        elif larger_follower_count == choose:
            #won, 
            victory = True
            final_score+=1
            compare_A = compare_B
            os.system('clear')
            print(logo)
            print(f"You're right! Current score: {final_score}.") 
            process()
        else:
            victory = False
            print(f"Sorry, that's wrong. Final score: {final_score}")
            sys.exit() 


process()