cost = float(input("Change owed: "))*100
total_coins = 0
total_coins += int(cost/25)
cost = cost%25
total_coins += int(cost/10)
cost = cost%10
total_coins += int(cost/5)
cost = cost%5
total_coins += int(cost/1)
cost = cost%1
print(total_coins)