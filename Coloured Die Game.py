import random

i = 1

print("Welcome to the dice game, where you and your opponent each"
      "choose one of the red, green or blue dice and roll them.")
print('''The dice contain the following sides:
                Red: 1 4 4 4 4 4
                Green: 2 2 2 5 5 5
                Blue: 6 3 3 3 3 3''')


def roll_r():
    sequence_r = [1, 4, 4, 4, 4, 4]
    r = int(random.choice(sequence_r))
    if r in sequence_r:
        return r


def roll_g():
    sequence_g = [2, 2, 2, 5, 5, 5]
    g = int(random.choice(sequence_g))
    if g in sequence_g:
        return g


def roll_b():
    sequence_b = [6, 3, 3, 3, 3, 3]
    b = int(random.choice(sequence_b))
    if b in sequence_b:
        return b


die1 = input("Enter the die color player 1 (R, G or B): ")
die2 = input("Enter the die color player 2 (R, G or B): ")


def roll_die1(die1):
    if die1 == 'R':
        return roll_r()

    elif die1 == 'G':
        return roll_g()

    else:
        return roll_b()


def roll_die2(die2):
    if die2 == 'R':
        return roll_r()

    elif die2 == 'G':
        return roll_g()

    else:
        return roll_b()


x = roll_die1(die1)
y = roll_die2(die2)
score_1 = 0
score_2 = 0


def score(x, y):
    global score_1
    global score_2
    if x > y:
        score_1 += 1
        return score_1
    elif x < y:
        score_2 += 1
        return score_2


for i in range(1,51):
    player1 = roll_die1(die1)
    player2 = roll_die2(die2)
    score(roll_die1(die1), roll_die2(die2))

    print(i,'.', die1,':',x, die2,':',y, "-> Score:", score_1, "to", score_2)
    i += 1