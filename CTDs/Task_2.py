
bag =[6,22,10,999,76,43]
print("Program output : ",bag)

for x in range(6):
    s =input("User :")
    n =int(input("User :"))
    if s=="enter":  bag.append(n)
    else:
        if len(bag)==5: print("Cannot remove , bag is at minimum capacity")
        else : bag.remove(n)
    print("Program output : ",bag)
