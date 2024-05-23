while True:
    name = input()
    if name != "Voldemort" and name != "Welcome!" and len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif name != "Voldemort" and name != "Welcome!" and len (name) == 5 :
        print (f"{name} goes to Slytherin." )
    elif name != "Voldemort" and name != "Welcome!" and len (name) == 6 :
        print (f"{name} goes to Ravenclaw." )
    elif name != "Voldemort" and name != "Welcome!" and len (name) > 6 :
        print (f"{name} goes to Hufflepuff.")
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break