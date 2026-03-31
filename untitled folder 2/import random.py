import random

def generate_story():
    print("--- Mad Libs Story Generator ---")
    print("Choose a template number:")
    print("1. The Hospital Visit")
    print("2. Camping Trip")
    print("3. Enchanted Castle")
    
    choice = input("Enter choice (1, 2, or 3): ")

    if choice == "1":
        # Template 1: Hospital
        num1 = input("Type a number: ")
        time = input("Type a measure of time: ")
        transport = input("Type a mode of transportation: ")
        adj1 = input("Type an adjective: ")
        adj2 = input("Type another adjective: ")
        noun1 = input("Type a noun: ")
        color = input("Type a color: ")
        body1 = input("Type a part of the body: ")
        verb1 = input("Type a verb: ")
        num2 = input("Type a second number: ")
        noun2 = input("Type a second noun: ")
        noun3 = input("Type a third noun: ")
        body2 = input("Type another part of the body: ")
        verb2 = input("Type another verb: ")
        noun4 = input("Type a fourth noun: ")
        adj3 = input("Type a third adjective: ")
        silly = input("Type a silly word: ")
        noun5 = input("Type one last noun: ")

        print("\n--- YOUR STORY ---")
        print(f"It was about {num1} {time} ago when I arrived at the hospital in a {transport}. "
              f"The hospital is a/an {adj1} place, there are a lot of {adj2} {noun1} here. "
              f"There are nurses here who have {color} {body1}. If someone wants to come into "
              f"my room I told them that they have to {verb1} first. I’ve decorated my room with "
              f"{num2} {noun2}. Today I talked to a doctor and they were wearing a {noun3} on "
              f"their {body2}. I heard that all doctors {verb2} {noun4} every day for breakfast. "
              f"The most {adj3} thing about being in the hospital is the {silly} {noun5}!")

    elif choice == "2":
        # Template 2: Camping
        name = input("Type a Person's Name: ")
        noun1 = input("Type a noun: ")
        adj1 = input("Type an adjective (feeling): ")
        verb1 = input("Type a verb: ")
        adj2 = input("Type another adjective (feeling): ")
        animal1 = input("Type an animal: ")
        verb2 = input("Type a second verb: ")
        color1 = input("Type a color: ")
        v_ing = input("Type a verb ending in 'ing': ")
        adverb = input("Type an adverb (ending in 'ly'): ")
        num1 = input("Type a number: ")
        time = input("Type a measure of time: ")
        color2 = input("Type a second color: ")
        animal2 = input("Type a second animal: ")
        num2 = input("Type a second number: ")
        silly = input("Type a silly word: ")
        noun2 = input("Type a second noun: ")

        print("\n--- YOUR STORY ---")
        print(f"This weekend I am going camping with {name}. I packed my lantern, sleeping bag, "
              f"and {noun1}. I am so {adj1} to {verb1} in a tent. I am {adj2} we might see a(n) "
              f"{animal1}, I hear they’re kind of dangerous. While we’re camping, we are going to "
              f"hike, fish, and {verb2}. I have heard that the {color1} lake is great for {v_ing}. "
              f"Then we will {adverb} hike through the forest for {num1} {time}. If I see a {color2} "
              f"{animal2} while hiking, I am going to bring it home as a pet! At night we will tell "
              f"{num2} {silly} stories and roast {noun2} around the campfire!!")

    elif choice == "3":
        # Template 3: Enchanted Castle
        name = input("Type a Person's Name: ")
        adj1 = input("Type an adjective: ")
        color = input("Type a color: ")
        animal = input("Type an animal: ")
        place = input("Type a place: ")
        adj2 = input("Type a second adjective: ")
        magical1 = input("Type a magical creature (plural): ")
        adj3 = input("Type a third adjective: ")
        magical2 = input("Type a second magical creature (plural): ")
        room = input("Type a room in a house: ")
        noun1 = input("Type a noun: ")
        noun2 = input("Type a second noun: ")
        noun_p = input("Type a plural noun: ")
        adj4 = input("Type a fourth adjective: ")
        noun_p2 = input("Type a second plural noun: ")
        num = input("Type a number: ")
        time = input("Type a measure of time: ")
        v_ing = input("Type a verb ending in 'ing': ")
        adj5 = input("Type a fifth adjective: ")
        noun3 = input("Type a third noun: ")

        print("\n--- YOUR STORY ---")
        print(f"Dear {name}, I am writing to you from a {adj1} castle in an enchanted forest. "
              f"I found myself here one day after going for a ride on a {color} {animal} in {place}. "
              f"There are {adj2} {magical1} and {adj3} {magical2} here! In the {room} there is a "
              f"pool full of {noun1}. I fall asleep each night on a {noun2} of {noun_p} and dream of "
              f"{adj4} {noun_p2}. It feels as though I have lived here for {num} {time}. I hope one "
              f"day you can visit, although the only way to get here now is {v_ing} on a "
              f"{adj5} {noun3}!!")
    
    else:
        print("Invalid choice! Picking a random template for you...")
        print("Please run the program again and select 1, 2, or 3.")

generate_story()