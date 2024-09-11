some_list = ['a', 'b', 'c', 'a', 'd', 'b', 'e', 'f', 'g', 'd', 'b','g']
dup_list = []
# we can also use set instead of empty list or typecast the list to set and get the values out
# brut force
for i in range(len(some_list)):
    for j in some_list[i+1:]:
        if some_list[i] == j and j not in dup_list:
            dup_list.append(j)

print(dup_list)
# optimised to 0(n)
dup_list_1 = []

for i in some_list:
    if some_list.count(i) > 1 and i not in dup_list_1:
        dup_list_1.append(i)
print(dup_list_1)