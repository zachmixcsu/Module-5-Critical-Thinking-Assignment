
years = int(input("Input how many years: "))

i = 0
total_rainfall = 0

while(i < years):

    for j in range(12):
        total_rainfall += int(input(f'Enter the rainfall for month {j + 1}: '))


    i += 1

print(f'Total rainfall: {total_rainfall} inches')
print(f'Total months: {years * 12}')
print(f'Average monthly rainfall: {total_rainfall/(years * 12)}')
