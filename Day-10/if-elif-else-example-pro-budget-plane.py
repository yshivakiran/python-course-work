budget = int(input("enter the budget: "))

if budget > 50000:
    print("you can go for trip")
elif budget > 30000:
    print("you can go for pub")
elif budget > 10000:
    print("you can go for the shopping")
elif budget > 5000:
    print("you can go for cafe")
elif budget > 2000:
    print("you can go for the movie")
elif budget > 500:
    print("you can recharge your phone")
else:
    print("take rest")
