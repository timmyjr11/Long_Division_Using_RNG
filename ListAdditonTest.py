import random

Ones = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
Tens = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
true = True
while true:
    Rone = random.choice(Ones)
    Rten =random.choice(Tens)

    print(Rone)
    print(Rten)

    if Rone + Rten == 55:
        true = False
        print("Final Ones: " + str(Rone))
        print("Final Tens: " + str(Rten))
