coinname = input("Name Of the Coin : ")
coinrate = input("what was the value of coin when u purchased it  : ")
investrate = input("what amount did u invested in $ : ")

result = float(investrate) / float(coinrate)

print("\033[0;37;40m\nThe Total Coins You Get are : " + str(result) + " !")


coinrate_now = input("\nEnter The Coin Rate For Today : ")

result2 = float(coinrate_now)* float(result)

print(str(result2))
print("The Name Of The Coin Is : " + coinname)
print("\nThe Total Money You Have Is : "  + str(result2))