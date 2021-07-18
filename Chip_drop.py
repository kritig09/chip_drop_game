def display():
    for i in range(7):
        print(" ".join(chipdrop[i]))
    return


def check(p1, p2):
    for i in range(7):
        for j in range(4):
            if chipdrop[i][j] == chipdrop[i][j + 1] == chipdrop[i][j + 2] == chipdrop[i][j + 3] == "B":
                return p1
            elif chipdrop[i][j] == chipdrop[i][j + 1] == chipdrop[i][j + 2] == chipdrop[i][j + 3] == "R":
                return p2
    for i in range(7):
        for j in range(4):
            if chipdrop[j][i] == chipdrop[j + 1][i] == chipdrop[j + 2][i] == chipdrop[j + 3][i] == "B":
                return p1
            elif chipdrop[j][i] == chipdrop[j + 1][i] == chipdrop[j + 2][i] == chipdrop[j + 3][i] == "R":
                return p2

    return


restart = "y"

player1 = input("You are Player One: Enter your name,you will choose chip B").title()
player2 = input("You are Player Two: Enter your name,you will choose chip R").title()
number_wins = {player1: 0, player2: 0}
while restart != "n":
    chipdrop = [[".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."]]

    display()

    game_on = True
    chance_count = 0
    while game_on is not False:
        chance = int(input("Enter the column number (1-7) where you want to drop chip"))
        if chance_count % 2 == 0:
            for i in range(6, 0, -1):
                if chipdrop[i][chance - 1] == ".":
                    chipdrop[i][chance - 1] = "B"
                    break
            display()
            chance_count += 1
        else:
            for i in range(6, 0, -1):
                if chipdrop[i][chance - 1] == ".":
                    chipdrop[i][chance - 1] = "R"
                    break
            display()
            chance_count += 1

        winner = check(player1, player2)
        if winner == player1:
            print(player1 + " " + "won this round!")
            number_wins[player1] += 1
            game_on = False
            break
        elif winner == player2:
            print(player2 + " " + "won this round!")
            number_wins[player2] += 1
            game_on = False
            break

    restart = input("Do you want to play again? Type y to restart, n to quit").lower()
    if restart == "n":
        break
print("Score Board")
print(player1 + " " + "won" + " " + str(number_wins[player1]) + " " + "times!")
print(player2 + " " + "won" + " " + str(number_wins[player2]) + " " + "times!")
print(max(number_wins.keys()) + "won the game")
