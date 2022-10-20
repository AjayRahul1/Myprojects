n = int(input("Enter a number :"))
if n%2!=0:
    print("Weird")
elif n in range(2,6):
    if n%2==0:
        print("Not Weird")
elif n in range(6,21):
    if n%2==0:
        print("Weird")
else:
    if n%2==0:
        print("Not Weird")
