list1 = [15, 27, 43, 68]
list2 = [43, 68, 91, 24]

common = []

for i in list1:
    if i in list2:
        common.append(i)

print("Common Elements:", common)