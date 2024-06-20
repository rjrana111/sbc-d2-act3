from random import randint

result = randint(100, 999)
res = str(result)

print(f"The winning number is {result}.")

user = input("untag mo daog (three-digit number) TARGET/RAMBOL numbers: ")
if user == res:
    print("Congrats Daog ka sa target.")
elif (sorted(user) == sorted(res)) and (user != result):
    print("daog kas rambol")
elif len(user) == 4:
    print("tulo ra taman brad")
else:
    print(f"pildi man ka brad {result}.")