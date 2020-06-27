myList = ['0','1','2','3']
listLength = len(myList)
x = 5

print("(0 - 3):")
for i in range(0, listLength):
    print(myList[i])

print("\n(3 - 0):")
for i in range(listLength, 0, -1):
    print(myList[i - 1])

print("\n(8 - 2, every other #):")
for i in range(listLength, 0, -1):
    print(int(myList[i - 1]) + x)
    x -= 1
