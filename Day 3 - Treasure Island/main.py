ascii_art = """
___________.__              __      __        .__   __   .__                 ________                     .___ 
\__    ___/|  |__   ____   /  \    /  \_____  |  | |  | _|__| ____    ____   \______ \   ____ _____     __| _/ 
  |    |   |  |  \_/ __ \  \   \/\/   /\__  \ |  | |  |/ /  |/    \  / ___\   |    |  \_/ __ \\__  \   / __ |  
  |    |   |   Y  \  ___/   \        /  / __ \|  |_|    <|  |   |  \/ /_/  >  |    `   \  ___/ / __ \_/ /_/ |  
  |____|   |___|  /\___  >   \__/\  /  (____  /____/__|_ \__|___|  /\___  /  /_______  /\___  >____  /\____ |  
"""

print(ascii_art)

print("Welcome to the nightmare!\n You must go to Alexandria before you get caught by walkers!")
choice = input('You are in the Sanctuary! What do you want to do? Digit "Left" or "Right". ').lower()
if choice == "left":
    print("You killed 2 walkers! Go ahead!")
    choice = input('You run away from Saviors! And you see a lake. What do you want to do? Digit "Swim" or "Wait" .').lower()
    if choice == "swim":
        print("You escaped from the Whispers!") 
        choice = input('You passed the lake. Now you see a thousands of walkers! What do you want to do? Digit "Disguise", "Wait", "Cry". ').lower()
        if choice == "disguise":
            print("Excellent! You arrived at Alexandria!")
        elif choice == "wait":
            print("5 walker killed you! Game over!")
        else:
            print("You cried and some walkers killed you! Game over!")
    else:
        print("The whispers killed you! Game Over!")    
else:
    print("Negan killed you! Game Over!")
