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

# part 2
top_3 = sorted(list_of_sums, reverse=True)[:3]
print(top_3)


def sum(list):
    top_sum = 0
    for food in list:
        top_sum = top_sum + int(food)
    return top_sum


print(sum(top_3))