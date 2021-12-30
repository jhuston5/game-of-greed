import pytest
import random
from collections import Counter 
import sys

# def default_roller():
#   return ( randint(1,6), randint(1,6))

class Game: 
  current_round = 0
  def __init__(self, current_dice_count=6):
    self.current_dice_count = current_dice_count
    # Bring in an instance of the Banker Class to store scores
    self.banker = Banker()

 # roller_ex = (4,4,5,2,3,1)
  roller_str = ''

  def play(self, roller=None):  
    self._roller = roller or GameLogic.roll_dice
    print("Welcome to Game of Greed")
    print("(y)es to play or (n)o to decline")
    response = input("> ") 
    
    if response == "y": 
      self.start_game(roller)

    elif response == "n": 
      self.quit_game()
  
  def start_round(self, current_round, current_dice_count): 
      print(f"Starting round {current_round}")
      self.new_roll(current_dice_count)

      # While true here?
      print("Enter dice to keep, or (q)uit:") 
      dice_response = input("> ")
      if dice_response == "q": 
        self.end_game()

      # print(f'Round Response: {type(dice_response)}')
      unbanked = GameLogic.calculate_score(dice_response)
      # print(f'This is unbanked {unbanked}')
      dice_remaining = self.current_dice_count - len(dice_response)
      print(f"You have {unbanked} unbanked points and {dice_remaining} dice remaining")
      print("(r)oll again, (b)ank your points or (q)uit:")
      
      round_response = input("> ")
      if round_response == "r":
        self.start_round(current_dice_count)
      if round_response == "b":
        self.banker.balance += unbanked
        print(f"You banked {unbanked} points in round {current_round}")
        current_round += 1
        print(f"Total score is {self.banker.balance} points")
    #   start_round()
        if round_response == "q":
          self.end_game()


   
  def start_game(self, roller): 
    current_round = 1
    while True:
      self.start_round(current_round,self.current_dice_count)
      current_round += 1
      
    # roll = GameLogic.roll_dice(current_dice_count)

    print("Enter dice to keep, or (q)uit:") 
    dice_response = input("> ")
    if dice_response == "q": 
      self.end_game()
    start_round(dice_response)


  def new_roll(self, current_dice_count):
    print(f"Rolling {current_dice_count} dice...")

    roll = self._roller(current_dice_count)
    print("*** " + " ".join([str(i) for i in roll]) + " ***")
    """    for num in roll:
      self.roller_str += str(num) + " "
    print(f"*** {self.roller_str}***")"""

    #return str(self.roller_str)


  def quit_game(self): 
    print("OK. Maybe another time")

  def end_game(self): 
    print(f'Thanks for playing. You earned {self.banker.balance} points')
    sys.exit()
  
  
class GameLogic:
    number_of_dice_rolled = 0

    def __init__(self):
      pass 
      
      
    @staticmethod
    def roll_dice(rolled_dice):
        dice_list = []
        GameLogic.number_of_dice_rolled = rolled_dice
        for _ in range(rolled_dice):
            dice_list.append(random.randint(1,6))
        print(tuple(dice_list))
        return tuple(dice_list)

    @staticmethod
    def calculate_score(dice_list):
      # Set semi-global current_roll_score storage variable
      current_roll_score = 0
      # print((dice_list))
      roll_resp = str(dice_list)
      # print(roll_resp)
      count_roll = Counter(dice_list)
      # print(f'this is count roll: {count_roll}')
      

    # Check if there is a straight roll
      if len(count_roll) == 6:
            print("This is a straight: 1500")
            current_roll_score += 1500
            return 1500

    # Iterate through the roll to determine its score
      pairs = 0
      for i in count_roll:
        # Set the counter dictionary key as an integer for comparison eg {'5': 1} i = int('5')
        set_i_int = int(i)
        # Testing to try and see the object issue
        """count_roll_type = count_roll.keys()
        print(f'Count Roll Type: {count_roll_type}')
        print(f'This is i of count roll: {type(i)}')
        print(f'This is count_roll[i]: {count_roll[i]}')"""
      # Check for pairs of numbers
        if count_roll[i] == 2:
          pairs += count_roll[i]
          if pairs == 6:
            current_roll_score += 1500
      
      # Check for rolls of 5 less than 3 of a kind
      # Threw in an extra condition to handle if the dict obj is a str (or i == '5)
        if set_i_int == 5 and count_roll[i] < 3:
          score = count_roll[i] * 50
          # print(f'Score: {score}')
          current_roll_score += score

      # Check for rolls of 1 less than 3 of a kind
        elif set_i_int == 1 and count_roll[i] < 3:
          current_roll_score += count_roll[i] * 100
      
      # Write a function that iterates through here and doubles it
      # Deal with rolls of 1 more than 3 of a kind
        elif set_i_int == 1 and count_roll[i] >= 3:
          current_roll_score += ((count_roll[i] - 2) * 1000)
        elif count_roll[i] >= 3:
          current_roll_score += ((set_i_int * 100) * (count_roll[i] - 2))        

      # print(f'this is current roll score: {current_roll_score}')
      return current_roll_score      
 
class Banker:
  def __init__(self): 
     self.balance = 0
     self.shelved = 0

  def shelf(self, points=0):
    self.shelved += points  

  def bank(self): 
    self.balance += self.shelved  
    self.shelved = 0 
    return self.balance   

  def clear_shelf(self): 
    self.shelved = 0 


# if __name__ == "__main__":
  # game_instance = GameLogic()
  # current_dice_roll = GameLogic.roll_dice(6)
  # GameLogic.calculate_score(current_dice_roll)
  # example_roll = GameLogic.calculate_score([6, 6, 4, 4, 2, 2])
  # print(example_roll)
  # game_instance.calculate_score(game_instance.roll_dice(6))
 # game_instance
  # test_roll_1 = [(4,),(4,),(5,),(2,),(3,),(1,)]
  # test_roll_2 = [(4,),(2,),(6,),(4,),(6,),(5,)]
  # def mock_roller(rolls):
    
  #       # return (4,3, 1, 1)
  #       return rolls.pop(0) if rolls else default_roller()
  
  # Game.play(mock_roller())