N = int(input("Please Enter The Number Of Marbles : "))
marblesWithPlayer1 = 0
marblesWithPlayer2 = 0
countList = []
for i in range(1, N+1):
    if i % 2 == 0:
        if N % 3 == 0:
            marblesWithPlayer1 = marblesWithPlayer1 + 1 or 2
            N = N - marblesWithPlayer1
        elif N - 1 % 3 == 0:
            marblesWithPlayer1 = marblesWithPlayer1 + 1 or 3
            N = N - marblesWithPlayer1
        elif N - 2 % 3 == 0:
            marblesWithPlayer1 - marblesWithPlayer1 + 1 or 2 or 3
            N = N - marblesWithPlayer1
    else:
        if N % 3 == 0:
            marblesWithPlayer2 = marblesWithPlayer2 + 1 or 2
            N = N - marblesWithPlayer2
        elif N - 1 % 3 == 0:
            marblesWithPlayer2 = marblesWithPlayer2 + 1 or 3
            N = N - marblesWithPlayer2
        elif N - 2 % 3 == 0:
            marblesWithPlayer2 - marblesWithPlayer2 + 1 or 2 or 3
            N = N - marblesWithPlayer2
    i = i + 1
if i % 2 != 0:
    print("Congratulations To Player 1 You Win!!!")
else:
    print("Congratulations To Player 2 You Win!!!")