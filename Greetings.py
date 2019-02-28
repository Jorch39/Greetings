def greet(friend, money):

    if friend and (money > 20):
        print ("Hola")
        money = money - 20
    elif friend:
        print ("Hi")
    else:
        print ("Ha ha")
        money = money +10
    return money

money = 35

money = greet(True, money)
print ("Dinerito:", money)
print()

money = greet(False, money)
print ("Dinerito:", money)
print()


