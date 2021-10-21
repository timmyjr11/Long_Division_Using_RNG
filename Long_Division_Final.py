import random

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

dividind = random.choice(divisionTenMillion) + random.choice(divisionOneMillion) + \
           random.choice(divisionHundredThousand) \
           + random.choice(divisionTenThousand) + random.choice(divisionOneThousand) + \
           random.choice(divisionHundred) + random.choice(divisionTen) + random.choice(divisionOne)

divisor = random.choice(divisorHundred) + random.choice(divisorTens) + random.choice(divisorOnes)
# Fix
Answer = random.choice(AnswerTenThousand) + 0 + 800 + 0 + random.choice(AnswerOne)

true = True

while true:

    dividind = random.choice(divisionTenMillion) + random.choice(divisionOneMillion) + \
               random.choice(divisionHundredThousand) \
               + random.choice(divisionTenThousand) + random.choice(divisionOneThousand) + \
               random.choice(divisionHundred) + random.choice(divisionTen) + random.choice(divisionOne)

    divisor = random.choice(divisorHundred) + random.choice(divisorTens) + random.choice(divisorOnes)
    # Fix
    Answer = random.choice(AnswerTenThousand) + 0 + 800 + 0 + random.choice(AnswerOne)

    print("dividind:" + str(dividind))
    print("divisor: " + str(divisor))
    print("Answer: " + str(Answer))

    if Answer == (dividind / divisor) and (dividind % divisor) == 0:
        true = False
        print("Final dividend: " + str(dividind))
        print("Final divisor: " + str(divisor))
        print("Final Answer:" + str(Answer))

    else:
        print("fail")
