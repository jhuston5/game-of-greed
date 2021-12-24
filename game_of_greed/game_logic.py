import random
from collections import Counter


class GameLogic:
    number_of_dice_rolled = 0

    def __init__(self):
      # self.dice_list = dice_list
      pass

    def __str__(self):
      print(f"Current dice roll is")

    @staticmethod
    def roll_dice(rolled_dice):
        dice_list = []
        GameLogic.number_of_dice_rolled = rolled_dice
        for _ in range(rolled_dice):
            dice_list.append(random.randint(1,6))
        print(tuple(dice_list))
        return tuple(dice_list)

    
    @staticmethod
    def calculate_score(self):
      # Set semi-global current_roll_score storage variable
      current_roll_score = 0
      print(Counter(self))
      count_roll = Counter(self)

      common_count_roll = Counter(self).most_common(1)
      

    # Check if there is a straight roll
      if len(count_roll) == 6:
            print("This is a straight: 1500")
            current_roll_score += 1500
            return 1500

    # Iterate through the roll to determine its score
      pairs = 0
      for i in count_roll:
        # Check for pairs of numbers
          if count_roll[i] == 2:
            pairs += count_roll[i]
            if pairs == 6:
              current_roll_score += 1500
        
        # Check for rolls of 5 less than 3 of a kind
          if i == 5 and count_roll[i] < 3:
            score = count_roll[i] * 50
            current_roll_score += score

        # Check for rolls of 1 less than 3 of a kind
          elif i == 1 and count_roll[i] < 3:
            current_roll_score += count_roll[i] * 100
        
        # Write a function that iterates through here and doubles it
        # Deal with rolls of 1 more than 3 of a kind
          elif i == 1 and count_roll[i] >= 3:
            if count_roll[i] == 3:
              current_roll_score += 1000
            if count_roll[i] == 4:
              current_roll_score += 2000
            if count_roll[i] == 5:
              current_roll_score += 3000
            if count_roll[i] == 6:
              current_roll_score += 4000
        
        # Deal with any other 3 of a kind roll
          elif count_roll[i] == 3:
            current_roll_score += (i * 100)      
        # Deal with any other 4 of a kind roll
          elif count_roll[i] == 4:
            current_roll_score += (i * 100) * 2
        # Deal with any other 5 of a kind roll
          elif count_roll[i] == 5:
            current_roll_score += (i * 100) * 3
        # Deal with any other 6 of a kind roll
          elif count_roll[i] == 6:
            current_roll_score  += (i * 100) * 4
      print(current_roll_score)
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


if __name__ == "__main__":
  # game_instance = GameLogic()
  # current_dice_roll = GameLogic.roll_dice(6)
  # GameLogic.calculate_score(current_dice_roll)
  example_roll = GameLogic.calculate_score([6, 6, 4, 4, 2, 2])
  print(example_roll)
  # game_instance.calculate_score(game_instance.roll_dice(6))
 # game_instance
