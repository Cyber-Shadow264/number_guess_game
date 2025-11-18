print("\033c")
print('''  ====================================
            WELCOME
               TO
       GUESSING  NUMBER  GAME
======================================    
              ''')

user = input("Please, Enter your name : ")

print(f'''

Hello, {user}!
My name is Bot.
I am your computer opponent in this game.

This is a simple Guessing Number Game.
I will choose a secret number between 1 and 5, and you must guess it.
After each guess, I will give you a hint:
- Too high
- Too low
- Or correct!

Try to guess the number in the fewest attempts.
Good luck!
''')

x1 = input('''
You are ready!
Please, write to run! : ''')

if x1.upper() == "RUN":
    print("\033c")
else:
    print("Invalid input! You must type RUN.")
    exit()

print('''  ====================================
            WELCOME
               TO
       GUESSING  NUMBER  GAME
======================================    
              ''')

# random module use 
import random
num = random.randint(1, 5)

# user guess input
x2 = input("""I have chosen a number between 1 and 5.
Try to guess the number : """)

if num == int(x2):
    print("Congratulations! You guessed the correct number!")

elif int(x2) < 1 or int(x2) > 5:
    print("Invalid input! Please enter a number between 1 and 5.")
           
elif int(x2) < num:
    print("Too low! Try a higher number.")
    
elif int(x2) > num:
    print("Too high! Try a lower number.")

	
# FUTURE TO IMPROVEMENT
# I AM LEARNING STAGE
