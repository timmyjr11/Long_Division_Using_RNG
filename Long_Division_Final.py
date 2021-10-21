# Calls the python (the programming language that is being used) libary called "random" which is used to generate
# random numbers
import random

# Creates lists that represent the numbers 0 - 9
divisorHundred = [100, 200, 300, 400, 500, 600, 700, 800, 900]
divisorTens = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
divisorOnes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

divisionTenMillion = [0, 10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000, 80000000, 90000000]
divisionOneMillion = [0, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000]
divisionHundredThousand = [0, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000]
divisionTenThousand = [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]
divisionOneThousand = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
divisionHundred = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
divisionTen = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
divisionOne = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

AnswerTenThousand = [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]
AnswerOne = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Creates the dividend by adding all the lists together while also adding a random selector
dividend = random.choice(divisionTenMillion) + random.choice(divisionOneMillion) + \
           random.choice(divisionHundredThousand) \
           + random.choice(divisionTenThousand) + random.choice(divisionOneThousand) + \
           random.choice(divisionHundred) + random.choice(divisionTen) + random.choice(divisionOne)

divisor = random.choice(divisorHundred) + random.choice(divisorTens) + random.choice(divisorOnes)

Answer = random.choice(AnswerTenThousand) + 0 + 800 + 0 + random.choice(AnswerOne)

# Variable "true" created to be able to switch the while statement from true to false
true = True

# Main part of the program that is a loop at that allows the numbers to be switched and changed
while true:
    # Randomizes the numbers then adds them together
    dividend = random.choice(divisionTenMillion) + random.choice(divisionOneMillion) + \
               random.choice(divisionHundredThousand) \
               + random.choice(divisionTenThousand) + random.choice(divisionOneThousand) + \
               random.choice(divisionHundred) + random.choice(divisionTen) + random.choice(divisionOne)

    divisor = random.choice(divisorHundred) + random.choice(divisorTens) + random.choice(divisorOnes)

    Answer = random.choice(AnswerTenThousand) + 0 + 800 + 0 + random.choice(AnswerOne)

    # Gives information of the different numbers used
    print("dividend:" + str(dividend))
    print("divisor: " + str(divisor))
    print("Answer: " + str(Answer))
    # An if statement that states that if the answer is equal to the dividend divided by the divisor and the
    # remainder is zero
    if Answer == (dividend / divisor) and (dividend % divisor) == 0:
        # If the statement is true, then stop randomizing the numbers and tell the correct answers
        true = False
        print("Final dividend: " + str(dividend))
        print("Final divisor: " + str(divisor))
        print("Final Answer:" + str(Answer))
    # If the if statement is not true, then the code will state that the set of numbers failed to meet the conditions
    # and move on to the next number
    else:
        print("fail")
