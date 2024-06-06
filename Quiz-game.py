print("\nWelcome to my Quiz :)\n")

playing = input("Do you want to play? (Please select yes or no) \n")

if playing.lower() != "yes":
    quit()

print("Okay!! Let's play :)\n")
score = 0

answer = input("What does RAM stands for?\n")
if answer.lower() == "random access memory":
    print("Correct answer!")
    score +=1
else:
    print("Incorrect")


answer = input("How many players are there in a soccer team?\n")
if answer == "11":
    print("Correct answer!")
    score +=1
else:
    print("Incorrect")


answer = input("Who is the CEO of the Tesla?\n")
if answer.lower() == "elon musk":
    print("Correct answer!")
    score +=1
else:
    print("Incorrect")


answer = input("What is the capital city of Canada?\n")
if answer.lower() == "ottawa":
    print("Correct answer!")
    score +=1
else:
    print("Incorrect")

answer = input("What does WWW stands for?\n")
if answer.lower() == "world wide web":
    print("Correct answer!")
    score +=1
else:
    print("Incorrect")


print("You got " + str(score) + " questions correct!")
print("And your score is " + str((score / 5) * 100) + "%")