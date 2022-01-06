# import pytest
import random
from collections import Counter 
import sys

class Game: 
  current_round = 0
  def __init__(self, current_dice_count=6):
    self.current_dice_count = current_dice_count
    # Bring in an instance of the Banker Class to store scores
    self.banker = Banker()
   
  def play(self, roller=None):  
    self._roller = roller or GameLogic.roll_dice
    print("Welcome to Game of Greed")
    print("(y)es to play or (n)o to decline")
    response = input("> ") 
    
    if response == "y": 
      self.start_game(roller) 

    elif response == "n": 
      self.quit_game()
  



  def start_round(self, current_round, current_dice_count, first_round=True): 
    if first_round:
      print(f"Starting round {current_round}")
    print(f"Rolling {current_dice_count} dice...")
    round_roll = self.new_roll(current_dice_count)
    self.zilch(round_roll, current_round) 

    

    status = True
    while status:
      print("Enter dice to keep, or (q)uit:") 
      dice_response = input("> ")
      dice_response = dice_response.replace(" ", "")
      
      

      if dice_response == "q":
        self.end_game()
      elif GameLogic.validate_keepers(round_roll, dice_response) == False:
        print("Cheater!!! Or possibly made a typo...")
        print("*** " + " ".join([str(i) for i in round_roll]) + " ***")    
        continue
      
      unbanked = GameLogic.calculate_score(dice_response) + self.banker.shelved
      dice_remaining = current_dice_count - len(dice_response)
      print(f"You have {unbanked} unbanked points and {dice_remaining} dice remaining")
      print("(r)oll again, (b)ank your points or (q)uit:")
      
      round_response = input("> ")
      if round_response == "r":
        if dice_remaining == 0:
          self.banker.shelved += unbanked
          self.current_dice_count = 6
          self.start_round(current_round, current_dice_count, False)
        
        else:
          self.banker.shelved += unbanked
          self.current_dice_count = dice_remaining
          self.start_round(current_round, dice_remaining, False)

      elif round_response == "q":
        self.end_game()     

      elif round_response == "b":
        self.banker.balance += unbanked
        print(f"You banked {unbanked} points in round {current_round}")
        print(f"Total score is {self.banker.balance} points")
        self.banker.clear_shelf()
        self.current_dice_count = 6

        current_round += 1
        print(f"Starting round {current_round}")
        self.start_round(current_round, 6, False)
        status = False

  def start_game(self, roller): 
    current_round = 1
    while current_round <= 20:
      self.start_round(current_round,self.current_dice_count)
      print(f'Current Round at Bank: {current_round}')
  
  def new_roll(self, current_dice_count):
    roll = self._roller(current_dice_count)
    print("*** " + " ".join([str(i) for i in roll]) + " ***")
    return roll 

  def zilch(self,round_roll,current_round): 
    if GameLogic.calculate_score(round_roll) == 0:
      print("""****************************************
**        Zilch!!! Round over         **
****************************************""")
      print(f"You banked 0 points in round {current_round}")
      print(f"Total score is {self.banker.balance} points")
      self.start_round(current_round+1, 6)


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


if __name__ == "__main__":
  game_instance = Game()
  game_instance.play()

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
