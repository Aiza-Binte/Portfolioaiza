# Little adventure game
print("Welcome to the Adventure Game!")
print("Your car broke down in the middle of the road with a warning of a snow storm coming ahead.")
#choies
print("1) You can stay in the car with no signal.")
print("2) You ask help from a creepy old mansion.")
direction = input("Which one will you pick? choose 1 or 2?")
#choices
if direction == "1": #"Stay in the car.":
    print("The snow storm eventually breaks out and you freeze to death in the car.")
elif direction == "2": #"Ask help from the old creepy mansion.":
    print("You knock but no one answered the door but the door was slghtly ajar.")
    print("Inside you heard a voice, what will you do?")
    print("1) Go back to your car because you're scared.")
    print("2) You investigate the mansion.")
    choice = input()
if choice == "1":
        print("The weather gets really cold, and you freeze to death.")
elif choice == "2":
    print ("With mobile flash you enter and investigate the mansion.")  
    print ("You see a shadow figure at the end of the hall but it disappears fast. What will you do?")   
    print ("1)You get scared and and drop your phone and break it")
    print ("2)You get scared and close the door and try to proccess what you just saw.")
    choice = input()
if choice == "1":
    print ("Now you will have to explore without light.")
    print ("It is dark and you trip and fall and hit you head.")
elif choice == "2":
    print ("You relax a bit and start investigating again.")
    print ("The mansion was big and creepy and you felt like being watched.") 
    print ("Suddenly, the door closes and traps you inside the mansion. What will you do")
    print ("1) Break the door with you foot.")
    print ("2) Try to find an escape by exploring the mansion.")
    choice = input()
if choice == "1":
      print ("Instead of breaking the door you break your foot.")
    elif choice == "2":
      print ("You start to explore the mansion for an escape.")
      print ("While exploring the mansion, you see someone sitting in the library, what will you do?")
      print ("1) Ignore and quietly go explore further.")
      print ("2) Approach it and ask for help.")
      choice = input()
if choice == "1":
    print ("It hears you and haunts you down.")
elif choice == "2":
    print ("You approach it and speak to him but it stays silent")
    print ("You walk to the front of the sofa just to see there was no one.")
    print ("You were confused and terrified, what will you do now?")
    print ("1) Freak out and go crazy.")
    print ("2) Stay calm and collected and explore further.")
    choice = input()
if choice == "1":
    print ("For years you stayed there like a mad, crazy person.")
elif choice == "2":
    print ("You further explored the library and found one book in the bookshelf fascinating. Would you?")
    print ("1) Would you not take out the book out the bookshelf and die from curiosity?")
    print ("2) Would you take out the book out the bookshelf?")
    choice = input()
if choice == "1":
    print ("You missed the escape plan and got stuck in the house for years.")
elif choice == "2":
    print ("As you took out the book out of the bookshelf, the whole bookshelf slides reveal and a secreat passage.")
    print ("There were stairs going down and up, which one would you choose?")
    print ("1) upstairs.")
    print ("2) downstairs.")
    choice = input()
if choice == "1":
    print ("The door was closed and the key was downstairs")
    print ("You go downstairs") 
elif choice == "2":
    print ("The stairs lead downstairs to a maze looking hallway. What will you do?") 
    print ("1) Just go staight in.")
    print ("2) Look for a map first then try to sescape the maze.")
    choice = input()
if choice == "1":
    print ("You got lost for years in the maze.")
elif choice == "2":
    print ("You look around the library and eventually find the map and start your escape.")
    print ("You start exploring the maze according to map but you still didnt escape, why?")
    print ("1) You are horrible at seeing maps.")
    print ("2) Someone is sabotaging you")

print("Game over.")
# End of the game
print("Thanks for playing!")