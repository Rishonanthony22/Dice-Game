import random

response = "y"

while response == "y":
    no = random.randint(1, 6)
    
    # print the output
    print("---------")
    print("|       |")
    print("|   {}   |".format(no))
    print("|       |")
    print("---------")
    
    response = input("Press 'y' to roll again, or 'n' to exit: ")
    
print("Thanks for playing!")
