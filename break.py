x=int(input("how many candies do you want"))
av=5
i=1
while(i<=x):

    if i>av:
        print("out of stock")
        break

    print("candy")
    i+=1

print("bye")

for  i in range(1,101):

    if i%3==0 or i%5==0:
        continue

    print(i)

print("bye bye")