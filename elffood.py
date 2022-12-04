with open('elf food.txt') as f:
    lines= f.readlines()
list_of_sums = []
sum=0
for food in lines:
    if food != '\n':
       sum =sum+int(food)

    elif food == '\n':
        list_of_sums.append(sum)
        sum=0
max=max(list_of_sums)
print(max)


