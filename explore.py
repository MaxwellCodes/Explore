
from sys import exit
def endgame():
    print("Congrats, you failed")
    print("Do you want restart the game (yes or no)")
    playagain = input()

    if playagain == "yes":
        game()
    else:
        exit()
def wingame():
    print("Congrats, you won the game! Thanks for playing! Made by RazrX”)
    print("Do you want restart the game (yes or no)")
    playagain = input()

    if playagain == "yes":
        game()
    else:
        exit()
   
def game():
        print("""You are a Cave Explorer, while exploring you find a dark cave, the cave branches off to two other caves
which cave should you go into, Cave 1 or Cave 2?""")

        cave = input("> ")

        if cave == "1":
            print("There is a dungeon and a mysterious wall.")
            print("What do you do?")
            print("1. Open the dungeon")
            print("2. Lean against the wall and wait")

            dungeon = input("> ")
                
            if dungeon == "1":
                print("You enter a the dungeon and immediatly get trapped and die of starvation.")
                endgame()
            elif dungeon == "2":
                print("As you lean against the wall, a secret trap activates and kills you.")
                endgame()
            else:
                print("You die from the toxic fumes in the cave.")
                endgame()

        elif cave == "2":
            print("You see a dim light at the end of the cave.")
            print("What do you do?")
            print("1. You go on.")
            print("2. You go back home.")


            light = input("> ")

            if light == "1":
            
                print("At the end of the cave you see a big hole dimly lit by iridescent flowers.")
                print("You fall in and splash into the middle an underground pond and see some ancient ruins on the other side of the cave")
                print("What do you do?")
            
                print("1. Swim across the pond and enter the ruins")
                print("2. Look around for an exit")
                print("3. Swim directly down")
            
        
                pond = input("> ")
                
                if pond == "1":
                    print("Theres a trap that immediately kills you")
                    endgame()
                    
                elif pond == "2":
                    print("you find a small staircase that leads upward")
                    print("you go up the stairs")
                    print("you fall down into a revine and die")
                    endgame()

                elif pond == "3":
                    print("you find as mysterious trapdoor at the bottom of the lake")
                    print("do you want to open it?")
                
                trapdoor = input()
                    
                if trapdoor == "yes":
                        print("you open the trapdoor and get sucked into it")
                        print("""you find yourself in a room with crystals surrounding you,
                    there is a mysterious gem that snines in the dark cave. Do you take it?""")
                    
                        take = input()
                        
                        if take == "yes":
                            print("when you take the gem you wake up and realize this was all a dream jk get baited kid")
                            endgame()
                        
                        if take == "no":
                            print("you pass out and awake in a dark alley")
                            print("there is a ladder leading up to the top of the building")
                            print("what do you do?")
                            print("1. Go up the ladder")
                            print("2. Stay in the alley")

                            alley = input()

                            if alley == "1":
                                print("""As you go up the ladder, you notice someethings off, 
                            when you finally get up the ladder, you notice a figure staring at you
                                """)
                                print("What do you do?")
                                print("1. Go up to the figure")
                                print("2. Stay at a distance")

                                ending = input()

                                if ending == "1":
                                    print("As you go up to the figure, they say")
                                    print("'I see that you have been on quite of the journey'")
                                    print("You try to reply, but cant speak")
                                    print("""They raise their hand at you and you suddenly wake up in bed
                                    realizing this had just been a dream""")
                                    wingame()
                                
                                if ending == "2":
                                    print("they come up to you and push you off the building, you hit the ground with a loud thud")
                                    endgame()
                            
                            if alley == "2":
                                print("You find a gun and shoot yourself")
                                endgame()
                        if trapdoor == "no":
                            print("You drown in the pond")
                            endgame()
                        
                        else:
                            endgame()

            else:
                print("you get tired and cant swim and drown")
            
        elif light == "2":
                print("you go home and cry in the corner")
                endgame()

        else:
            print("you die of the toxic fumes in the cave.")
            endgame()
        
game()

