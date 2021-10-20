import random

divisorHundred = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
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
AnswerOneThousand = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
AnswerTen = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
AnswerOne = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

randomDivisonTenMillion = random.choice(divisionTenMillion)
randomDivisonOneMillion = random.choice(divisionOneMillion)
randomDivisonHundredThousand = random.choice(divisionHundredThousand)
randomDivisonTenThousand = random.choice(divisionTenThousand)
randomDivisonOneThousand = random.choice(divisionOneThousand)
randomDivisonHundred = random.choice(divisionHundred)
randomDivisonTen = random.choice(divisionTen)
randomDivisonOne = random.choice(divisionOne)

randomDivisorHundred = random.choice(divisorHundred)
randomDivisorTens = random.choice(divisorTens)
randomDivisorOnes = random.choice(divisorOnes)

randomAnswerTenThousand = random.choice(AnswerTenThousand)
randomAnswerOneThousand = random.choice(AnswerOneThousand)
randomAnswerTen = random.choice(AnswerTen)
randomAnswerOne = random.choice(AnswerOne)

dividind = divisionTenMillion[randomDivisonTenMillion] + divisionOneMillion[randomDivisonOneMillion] + \
           divisionHundredThousand[randomDivisonHundredThousand] \
            + divisionTenThousand[randomDivisonTenThousand] + divisionOneThousand[randomDivisonOneThousand] + \
           divisionHundred[randomDivisonHundred] + divisionTen[randomDivisonTen] + divisionOne[randomDivisonOne]

divisor = divisorHundred[randomDivisorHundred] + divisorTens[randomDivisorTens] + divisorOnes[randomDivisorOnes]
# Fix
Answer = AnswerTenThousand[randomAnswerTenThousand] + AnswerOneThousand[1] + 800 + AnswerTen[randomAnswerTen] + AnswerOne[randomAnswerOne]
# create a for loop to actually make the random numbers go
while Answer != (dividind / divisor) and (dividind % divisor) != 0:
    random.choice(divisionTenMillion)
    random.choice(divisionOneMillion)
    random.choice(divisionHundredThousand)
    random.choice(divisionTenThousand)
    random.choice(divisionOneThousand)
    random.choice(divisionHundred)
    random.choice(divisionHundred)
    random.choice(divisionTen)
    random.choice(divisionOne)

    random.choice(divisorHundred)
    random.choice(divisorTens)
    random.choice(divisorOnes)

    random.choice(AnswerTenThousand)
    random.choice(AnswerOneThousand)
    random.choice(AnswerTen)
    random.choice(AnswerOne)

    print(dividind)
    print(divisor)
    print(Answer)

while Answer == (dividind / divisor) and (dividind % divisor) == 0:
    print("dividend: " + str(dividind))
    print("divisor: " + str(divisor))
    print("Answer:" + str(Answer))
