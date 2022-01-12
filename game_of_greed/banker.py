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