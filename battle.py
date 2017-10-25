import sys

class Attribute:
  def __init__(self, setMax):
    self.setMax(setMax)

  def setMax(self, newMax):
    self.max = newMax
    self.now = self.max
  
  def addMax(self, delta):
    self.max += delta
    self.now += delta
  
  def add(self, delta):
    if (self.now + delta <= self.max):
      self.now += delta
    else:
      print("Already at max!")
    
  def get(self):
    return self.now
    
  def getMax(self):
    return self.max

class Entity:
  def __init__(self, name, hp = 100, mp = 100, stam = 100, thirst = 100, psych = 100):
    self.isAlive = True
    self.name = name
    self.stats = {'hp': Attribute(hp), 'mp': Attribute(mp), 'stam': Attribute(stam), 'thirst': Attribute(thirst), 'psych': Attribute(psych)}
  
  def showName(self):
    print(f"Name: {self.name}")
    
  def showHp(self):
    print(f"Health:  {self.stats['hp'].get()}/{self.stats['hp'].getMax()}")

  def showMp(self):
    print(f"Spirit:  {self.stats['mp'].get()}/{self.stats['mp'].getMax()}")

  def showStam(self):
    print(f"Stamina: {self.stats['stam'].get()}/{self.stats['stam'].getMax()}")
    
  def showThirst(self):
    print(f"Hunger:  {self.stats['thirst'].get()}/{self.stats['thirst'].getMax()}")
    
  def showPsych(self):
    print(f"Sanity:  {self.stats['psych'].get()}/{self.stats['psych'].getMax()}")

  def showName(self):
    print(self.name)

  def showStats(self):
    self.showHp()
    self.showMp()
    self.showStam()
    self.showThirst()
    self.showPsych()
    print("")

class Question:
  def __init__(self, text, options, outcomes):
    self.text = text
    self.options = options
    self.outcomes = outcomes

def playerPrompt():
  name = input("What is your name?")
  answerKey = ['a','b','c','d','e']
  
  color = Question("What is your favorite color?", 
    {"a":"Purple",
    "b":"Blue",
    "c":"Yellow",
    "d":"Red",
    "e":"Brown"},
    
    {"a":lambda: player.stats['psych'].addMax(50),
    "b":lambda: player.stats['mp'].addMax(50),
    "c":lambda: player.stats['stam'].addMax(50),
    "d":lambda: player.stats['hp'].addMax(50),
    "e":lambda: player.stats['thirst'].addMax(50)})
    
  action = Question("What would you rather be?", 
    {"a":"Acrobat",
    "b":"Dancer",
    "c":"Singer",
    "d":"Talker",
    "e":"Weight lifter"},
    
    {"a":"player.action.append('acrobat')",
    "b":"player.action.append('dancer')",
    "c":"player.action.append('sing')",
    "d":"player.action.append('talk')",
    "e":"player.action.append('strong')"})
  
  ans = ''
  while (ans not in answerKey):
    ans = input(f"{color.text}\nA) {color.options['a']}\nB) {color.options['b']}\nC) {color.options['c']}\nD) {color.options['d']}\nE) {color.options['e']}\n").lower()
  colorAns = ans
  
  ans = ''
  while(ans not in answerKey):
    ans = input(f"{action.text}\nA) {action.options['a']}\nB) {action.options['b']}\nC) {action.options['c']}\nD) {action.options['d']}\nE) {action.options['e']}\n").lower()
  actionAns = ans
  
  # print(f"\nHi {name}!\nYou're a {color.options[colorAns].lower()}-shirted {action.options[actionAns].lower()}!")

  player = Entity(name)
  color.outcomes[colorAns]()
  return player

def gameLoop():
  player = playerPrompt()
  monster = Entity("Eldritch Horror", hp = 250, mp = 125, psych = 175)
  print(f"{player.name}, you are in a winding and dangerous maze-like dungeon.","\nYou are unaware how you got here, but you must journey forward to escape.")
  
  while(player.isAlive):
    ans = input(f"Will you journey forward?\nA) Yes\nB) No\n").lower()
    if (ans == 'a'):
      print(f"You have encountered a {monster.name}.")
      while(player.isAlive and monster.isAlive):
        ans = input("What action will you take?\nA) Fight\nB) Pick it up\nC) Dance")
        if (ans == 'a'):
          print(f"You attack the monster with your sword dealing 73 damage.",
          "\nIt lashes back with its tentacles, dealing 15 damage.\n")
          monster.stats['hp'].add(-73)
          player.stats['hp'].add(-25)
        elif (ans == 'b'):
          print(f"You strain to pick up the {monster.name}, dealing 85 damage but losing 35 stamina.",
          f"\nThe {monster.name} struggles to get back up.\n")
          if (player.stats['stam'].get() -35 <= 0):
            player.isAlive = False
            print(f"{player.name} has died!\nGame Over.")
            break
          else: 
            player.stats['stam'].add(-35)
            player.showStam()
          if (monster.stats['hp'].get() -85 <= 0):
            monster.isAlive = False
            print(f"{monster.name} is dead!\n You win!")
          else:
            monster.stats['hp'].add(-85)
            monster.showHp()
        elif (ans == 'c'):
          print(f"You dance your heart out, reducing {monster.name}'s spirit by  41.",
          f"\nThe {monster.name} belts out an undescribable cry, reducing your sanity by 30.\n")
        else:
          pass
    elif (ans == 'b'):
      print("You commit ritual sudoku and die.\n")
      player.isAlive = False
    else:
      pass
  return player

player = gameLoop()
