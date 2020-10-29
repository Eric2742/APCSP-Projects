from random import choices
from time import sleep

Answers = ["Yes", "No", "Possibly", "Maybe", "Likely", "Unlikely", "Very Unlikely", "Very Likely"]

def func():
    Question = input("Ask a Question: ")
    print(".")
    sleep(1)
    print("..")
    sleep(1)
    print("...")
    Answers1 = choices(Answers)
    print(*Answers1, sep = " ")

func()
Question2 = input("Would You Like to Ask Another Question? (Yes/No): ")

if Question2.lower() == "no":
    exit()
else:
    while Question2.lower() == "yes":
        func()
        Question2 = input("Would You Like to Ask Another Question? (Yes/No): ")


