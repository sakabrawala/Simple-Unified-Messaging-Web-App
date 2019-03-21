print("Please give an input for inventory")
inventory = int(input()) 

helmetcost = "90 77 68 60 54 49 46 44"
helmetarmor = "23 24 16 16 15 13 12 12"

bootscost = "64 51 52 35 33"
bootsarmor = "18 14 20 07 05"

leggingscost = "87 78 75 69 62 59 56 53 47 45 42"
leggingsarmor = "22 18 15 17 11 15 12 14 11 10 13"

chestcost = "67 64 62 59 58 57 55 54 50"
chestarmor = "22 23 21 20 10 19 19 18 17"

helmet = dict(zip(helmetcost.split(), helmetarmor.split()))
boot = dict(zip(bootscost.split(), bootsarmor.split()))
leggings = dict(zip(leggingscost.split(), leggingsarmor.split()))
chest = dict(zip(chestcost.split(), chestarmor.split()))

newhelmet = list(reversed(sorted(helmet.items(), key=lambda x: x[1])))
newboot = list(reversed(sorted(boot.items(), key=lambda x: x[1])))
newleggings = list(reversed(sorted(leggings.items(), key=lambda x: x[1])))
newchest = list(reversed(sorted(chest.items(), key=lambda x: x[1])))

i = 0

for i in range(inventory):
    
    a = newhelmet[i]
    b = newboot[i]
    c = newleggings[i]
    d = newchest[i]
    total = int(a[i]) + int(b[i]) + int(c[i]) + int(d[i])
    balance = 300 - total
    
    if total > 300:
        print("You don't have enough crowns!")
    else:
        print("Thank you for shopping with us! You have the best armor.")
        print("Cost of Helmet in Crowns",a[i])
        print("Cost of boot in Crowns",b[i])
        print("Cost of Leggings in Crowns",c[i])
        print("Cost of Chest in Crowns",d[i])
        print("Crowns still left - ",balance)
        break
    
