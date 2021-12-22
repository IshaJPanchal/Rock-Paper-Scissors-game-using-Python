import random as rd
print('''
      Rock Paper Scissors Game
      
      Please choose one of the three
      
      1-Rock
      2-Paper
      3-Scissors
      4-Exit the game
      
      Rules
      1. Rock beats scissors
      2. Scissors beats paper
      3. Paper beats rock
      
      Have fun!!
      ''')
while True:
    User_1=int(input("Your choice:"))
    
    if User_1==4:
        break
    elif User_1>=5:
        print("Please choose between 1 to 4")
    else:
        Game = {
            1:'Rock',
            2:'Paper',
            3:"Scissors"
        }
        AI_1= rd.randint(1,3)
        AI=Game.get(AI_1)
        User=Game.get(User_1)
        if AI=='Rock' and User == 'Scissors':
            print ('''
            
            You: 3-Scissors
            Computer: 1-Rock
            
            You were defeated
            ''')
        elif AI=='Scissors' and User == 'Paper':
            print('''
            
            You: 2-Paper
            Computer: 3-Scissors
            
            You were defeated
            ''')
        elif AI=='Paper' and User == 'Rock':
            print ('''
            
            You: 1-Rock
            Computer: 2-Paper
            
            You were defeated
            ''')
        elif AI=='Rock' and User =='Paper':
            print ('''
            You: 2-Paper
            Computer: 1-Rock
            
            You won
            ''')
        elif AI=='Scissors' and User == 'Rock':
            print('''
            You: 1-Rock
            Computer: 3-Scissors
            
            You won
            ''')
        elif AI=='Paper' and User == 'Scissors':
            print ('''
            You: 3-Scissors
            Computer: 2-Paper
            
            You won
            ''')
        elif AI==User=='Rock':
            print('''
            You: 1-Rock
            Computer: 1-Rock
            
            Draw
            ''')
        elif AI==User=='Paper':
            print('''
            You: 2-Paper
            Computer: 2-Paper
            
            Draw
            ''')
        elif AI==User=='Scissors':
            print('''
            You: 3-Scissors
            Computer: 3-Scissors
            
            Draw
            ''')