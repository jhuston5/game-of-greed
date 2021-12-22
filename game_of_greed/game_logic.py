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

    # Calculate_score Static method
    # input is a tuple of integers that represent a dice role
    # output from calculate_score is an integer representing the rolls's score according to the rules of the game

    @staticmethod
    def calculate_score(self):
      # input is dice_list? or rolled_dice?
      # Need to create a place for all the possible scores to be stored?
      # iterate through these scores to check if it includes one of those scores?
      # or instead use Counter to determine how many times a number is rolled, which can determine how many points they receive
      # output returns the stored score integer
      current_roll_score = 0
      print(Counter(self))
      count_roll = Counter(self)
      # (1, 1, 1, 2, 2, 2),

      # print(count_roll.most_common())
      common_count_roll = Counter(self).most_common(1)
      
      if len(count_roll) == 6:
            print("This is a straight: 1500")
            current_roll_score += 1500
            return 1500

      pairs = 0
      for i in count_roll:
          if count_roll[i] == 2:
            pairs += count_roll[i]
            if pairs == 6:
              current_roll_score += 1000
          if i == 5 and count_roll[i] < 3:
            score = count_roll[i] * 50
            current_roll_score += score
          elif i == 1 and count_roll[i] < 3:
            current_roll_score += count_roll[i] * 100
          elif i == 1 and count_roll[i] >= 3:
            if count_roll[i] == 3:
              current_roll_score += 1000
            if count_roll[i] == 4:
              current_roll_score += 2000
            if count_roll[i] == 5:
              current_roll_score += 4000
            if count_roll[i] == 6:
              current_roll_score += 8000
          elif count_roll[i] == 3:
            current_roll_score += i * 100      
          elif count_roll[i] == 4:
            current_roll_score += (i * 100) * 2
          elif count_roll[i] == 5:
            current_roll_score += (((i * 100) * 2 ) * 2)
          elif count_roll[i] == 6:
            current_roll_score  += ((((i * 100) * 2 ) * 2) *2)
      print(current_roll_score)
      return current_roll_score      

      
      # print(f"Most Common Counted Number Roll: {common_count_roll[0][0]}")
      # print(f"Most Common Count Roll: {common_count_roll[0][1]}")
      # print(f"Number of Dice rolled: {GameLogic.number_of_dice_rolled}")
      # print(f"Access individual keys: {common_count_roll.value}")
      # Straight - can check if the length of the count_roll is 6
      # 2 pairs - can check if the length of count_roll is two
      # Should we be checking the individual instances of a numbers occurrence?
      



      # 3 of a kind Logic
      # 3 of a kind are 100*number rolled
      # except three 1s = 1000 points
      #[0]= the actual number on the dice [0]=number of occurances of the dice number 
      # three_kind = int(common_count_roll[0][0]) * 100

      #for i in count_roll:
      # [0:idx ][1:idx ]
      #(3: 1)(2: 2)
"""   if int(common_count_roll[0][1]) == 3:
        # handle 3 ones - does not handle more than 3 ones
        if common_count_roll[0][0] == 1:
          print(f'Three 1s in a row: 1000')
          current_roll_score += 1000
          return 1000
                             #common_count_roll[3][4]
        print(f"Three of a kind score: {three_kind}")
        return three_kind
"""
      # 4/5/6 of a kind logic
      # Each additional die roll doubles the previous amount
      # Base case of the number times 100
     
"""     elif common_count_roll[0][1] == 4:
        if common_count_roll[0][0] == 1:
          print(f'Three 1s in a row: 1000')
          current_roll_score += 2000
          return 2000
        four_kind = three_kind * 2
        print(f"Four of a kind score: {four_kind}")
        current_roll_score += four_kind
        return four_kind

      elif common_count_roll[0][1] == 5:
        if common_count_roll[0][0] == 1:
          print(f'Three 1s in a row: 1000')
          current_roll_score += 4000
          return 4000
        five_kind = ((three_kind * 2) *2)
        print(f"Four of a kind score: {five_kind}")
        current_roll_score += five_kind
        return five_kind"""

        
"""  elif common_count_roll[0][1] == 6:
        if common_count_roll[0][0] == 1:
          print(f'Three 1s in a row: 1000')
          current_roll_score += 8000
          return 8000
        six_kind = (((three_kind * 2) * 2) * 2)
        print(f"Four of a kind score: {six_kind}")
        current_roll_score += six_kind
        return six_kind
"""
 
       

      # if common_count_roll[0][0] == 5:


      # 3 pairs logic
      # can we check if each value in the key == 2?

# return current_roll_score




if __name__ == "__main__":
  # game_instance = GameLogic()
  # current_dice_roll = GameLogic.roll_dice(6)
  # GameLogic.calculate_score(current_dice_roll)
  example_roll = GameLogic.calculate_score([6, 6, 4, 4, 2, 2])
  print(example_roll)
  # game_instance.calculate_score(game_instance.roll_dice(6))
 # game_instance
