limit = int(input("Enter Limit you set:"))
list = []
list2 = []

for i in range(limit):
    list.append(int(input("Enter element:")))

num = int(input("Enter a number:"))

print("Entered list:",list)

for i in list:
    if num > i:
        list2.append(i)


print("New list:",list2)