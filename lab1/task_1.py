numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum = 0

for i in range(len(numbers)):
    if (i!=4):
        sum+=numbers[i]
a_4=sum/len(numbers)
numbers[4] = a_4


print("Измененный список:", numbers)