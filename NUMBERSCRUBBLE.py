
#purpose:Each player takes turns picking a number from 1 to 9. Once a number has been picked, it cannot be picked again. If a player has picked three numbers that add up to 15, that player wins the game.
#if all the numbers are used and no player gets exactly 15, the game is a draw.


# welcome message and display status
print("Welcome to NUMBER SCRABBLE")
numbers = [1, 2, 3, 4, 5 , 6, 7, 8, 9]
array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sum1 = 0
sum2 = 0
mylist1 = []
mylist2 = []
x = False
y = False
while True:
    x = True
    if sum1 or sum2 == 15:
        break
    #player1's turn
    for i in range(0, 5):
        if len(numbers) == 0:
            break
        print("These are the avalible numbers:", numbers)
        if len(mylist1) > 0:
            print("Player1, you have entered these numbers:", mylist1)
        player1 = int(input("Player1, Please select a valid number:"))
        while True:
           if player1 <=9 and player1 >0:
             if array[player1] == 1:
               print("""Please,"Plyer1" select an available valid number""")
               x = False
               break
             else:
               array[player1] = 1
               mylist1.append(player1)
               numbers.remove(player1)
               #check if player1 wins
               if len(mylist1) >=3:
                for i in range(len(mylist1)):
                   for k in range(i + 1, len(mylist1)):
                       for j in range(k + 1, len(mylist1)):
                           if mylist1[i] + mylist1[k] + mylist1[j] == 15:
                               print("Player1 has selected these numbers", mylist1)
                               print(mylist1[i],"+", mylist1[k], "+", mylist1[j], "=15")
                               print("Player1 wins the game")
                               sum1 = 15
                if sum1 == 15:
                    break
                # if all numbers have picked
                if len(numbers) == 0:
                   print("Player1 has selected these numbers", mylist1)
                   print("Player2 has selected these numbers", mylist2)
                   print("the game is draw")
                   x = False
                   break
           else:
               print("""Please,"Player1" select a valid number""")
               x = False
           break
        break
    #player2'turn
    if x == True:
         if len(numbers) == 0:
            break
         if sum1 or sum2 == 15:
            break
         print(numbers)
         for i in range(0,4):
            if len(mylist2) > 0:
                print("Player2, you have entered these numbers:", mylist2)
            player2 = int(input("Player2, Please select a valid number: "))
            y=True
            while y == True:
              if player2 <= 9 and player2 > 0:
                 if array[player2] == 1:
                    print("""Please,"Plyer2" select an available valid number""")
                    y = False
                    break
                 else:
                    array[player2] = 1
                    mylist2.append(player2)
                    numbers.remove(player2)
                    # check if player2 wins
                    if len(mylist2) >= 3:
                     for i in range(len(mylist2)):
                        for k in range(i + 1, len(mylist2)):
                            for j in range(k + 1, len(mylist2)):
                                if mylist2[i] + mylist2[k] + mylist2[j] == 15:
                                    print("Player2 has selected these numbers", mylist2)
                                    print(mylist2[i], "+", mylist2[k], "+", mylist2[j], "=15")
                                    print("Plyer2 wins the game")
                                    sum2 = 15
                    if sum2 == 15:
                        break
                    # if all numbers have picked
                    if len(numbers) == 0:
                        print("Player1 has selected these numbers", mylist1)
                        print("Player2 has selected these numbers", mylist2)
                        print("the game is draw")
                        break
              else:
                print("""Please,"Plyer2" select a valid number""")
                y = False
              break
            if y:
             break
