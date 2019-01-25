
x = int(input("Enter year of birth: "))

years = 2019 - x

if years <= 18:
    print ("You're a minor")

elif years <= 36:
    print ("You're a youth")

else:
    print("You're an elder")