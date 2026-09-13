list1 = [18, 35, 47, 62]
list2 = [35, 51, 78, 90]

difference = []
difference1 = []

for i in list1:
    if i not in list2:
        difference.append(i)

for i in list2:
    if i not in list1:
        difference1.append(i)
print("Elements only in List1:", difference)
print("Elements only in List1:", difference1)

print("----------------------------------------------")
print("                    OR                        ")
print("----------------------------------------------")

list1 = [18, 35, 47, 62]
list2 = [35, 51, 78, 90]
difference = []
for i in list1:
    if i not in list2:
        difference.append(i)

print("Elements only in List1:", difference)
