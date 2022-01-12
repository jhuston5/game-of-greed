from sys import exit

try:
    from game_of_greed.game_logic import GameLogic
    from game_of_greed.banker import Banker  
except:
    from game_logic import GameLogic
    from banker import Banker


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
    exit()