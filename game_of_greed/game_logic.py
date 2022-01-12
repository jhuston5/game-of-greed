import pytest
import random
from collections import Counter 
from sys import exit


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
      return tuple(dice_list)

    @staticmethod
    def calculate_score(dice_list):
      # Set semi-global current_roll_score storage variable
      current_roll_score = 0
      count_roll = Counter(dice_list)
      
    # Check if there is a straight roll
      if len(count_roll) == 6:
            current_roll_score += 1500
            return 1500

      # Test list comprehension [True for value in count_roll.values() if [value] == 2]
      # ('5', 3, '2', 2, '3', 1)
      if len(count_roll) == 3 and all(val == 2 for val in count_roll.values()):
        current_roll_score += 1500
        return 1500

    # Iterate through the roll to determine its score
      # else:
          
      for i in count_roll:
        # Set the counter dictionary key as an integer for comparison eg {'5': 1} i = int('5')
        set_i_int = int(i)
      
      # Check for rolls of 5 less than 3 of a kind
        if set_i_int == 5 and count_roll[i] < 3:
          score = count_roll[i] * 50
          current_roll_score += score

      # Check for rolls of 1 less than 3 of a kind
        if set_i_int == 1 and count_roll[i] < 3:
          score = count_roll[i] * 100
          current_roll_score += score
      
      # Deal with rolls of 1 more than 3 of a kind
        if set_i_int == 1 and count_roll[i] >= 3:
          current_roll_score += ((count_roll[i] - 2) * 1000)
        if set_i_int != 1 and count_roll[i] >= 3:
          current_roll_score += ((set_i_int * 100) * (count_roll[i] - 2))        

      # print(f'this is current roll score: {current_roll_score}')
      return current_roll_score      

    @staticmethod
    def validate_keepers(round_roll, dice_response):
      # change round_roll/dice_response to a string; it was an int
      dice_string = str(round_roll)
      dice_resp_string = str(dice_response)
       
      #removes all the weird characters in the strings 
      disallowed_char = ", ()[]"
      for char in disallowed_char:
        dice_string = dice_string.replace(char, "")
        dice_resp_string =  dice_resp_string.replace(char, "") 
        
      #get the counter dictionary from the strings made from round_roll and dice_response
      count_rr = Counter(dice_string)
      count_dr = Counter(dice_resp_string)

      #for loop to compare the key value pairs and set the status to pull into the while loop in Game.start_round
      for key in count_rr:
        value_1 = count_rr[key]
        value_2 = count_dr[key]

        #this manages the number of kept numbers compared to the number of dice in the current dice roll. 
        if value_1 < value_2:
          return False
        elif value_1 > value_2:
          return True

    @staticmethod 
    def get_scorers(dice_list): 
      #passing in dice_list through calculate_score function
      all_dice = GameLogic.calculate_score(dice_list)  

      #if the dice have no scoring dice.     
      if all_dice == 0:
        return tuple() 

      #holds the sets of tuples in an list 
      scorers = [] 
      for i in range(len(dice_list)): 
          #takes the numbers in dicelist and chooses the first index ([:i] then concatenates the following values in that list on an increment of 1)
          sub_roll = dice_list[:i] + dice_list[i + 1:] 
          #of those in sub_roll runs them through gamelogic.calculate score
          sub_score = GameLogic.calculate_score(sub_roll)
          # print(f'subroll: {sub_roll}') 

          #if the sub score is not all dice (it shouldnt be):
          if sub_score != all_dice:
              #add them into the scorers list 
              scorers.append(dice_list[i]) 
      #convert this list into tuples
      return tuple(scorers) 



if __name__ == "__main__":
  game_instance = Game()
  game_instance.play()


