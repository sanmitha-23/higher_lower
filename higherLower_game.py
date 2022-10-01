from art import logo
from art import vs
import random
from game_data import data
from replit import clear

def description(acc_a,acc_b):
  acc_a_name = acc_a['name']
  acc_a_desc = acc_a['description']
  acc_a_country = acc_a['country']
  acc_a_followers = acc_a['follower_count']
  
  print(f"Compare A: {acc_a_name}, a {acc_a_desc}, from {acc_a_country}")
  
  print(vs)
  print('\n')
  
  acc_b_name = acc_b['name']
  acc_b_desc = acc_b['description']
  acc_b_country = acc_b['country']
  acc_b_followers = acc_b['follower_count']
  
  print(f"Against B: {acc_b_name}, a {acc_b_desc}, from {acc_b_country}")
  compare_res (acc_a,acc_a_followers,acc_b,acc_b_followers)

  
def change(acc_b,score):
  
  clear()
  acc_1 = acc_b
  acc_2 = random.choice(data)
  print(logo)
  
  print(f"You're right! Current score: {score}\n")
  
  description(acc_1,acc_2)

  
def compare_res (acc_a,acc_a_followers,acc_b,acc_b_followers):
  if acc_a_followers>acc_b_followers:
    ans = 'A'
  else:
    ans = 'B'

  res = input("\nWho has more followers? Type 'A' or 'B': ")

  score=0
  
  if ans==res:
    score += 1
    change(acc_b,score)
  else:
    print(f"\nSorry, that's wrong. Final score: {score}")
    return

  
def selection():
  print(logo)
  acc_a = random.choice(data)
  acc_b = random.choice(data)
  if acc_a==acc_b:
    acc_b = random.choice(data)
  description(acc_a,acc_b)

selection()
