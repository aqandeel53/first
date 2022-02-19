
mx,mn=0,1e9

while True:
    x=input("insert number : ")
    if x=='q': break
    mx =max(mx,int(x))
    mn =min(mn,int(x))

print("Largest number is ",mx)
print("smallest number is ",mn)
    

