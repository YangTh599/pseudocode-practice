# Thayer Yang
# 24 SEP 2024
# Pseudocode Practice

# Practice A

first_name = input("Enter your first name: \n")

print('Enter your 3 test scores: ')
quiz1 = float(input())
quiz2 = float(input())
quiz3 = float(input())

average_score = (quiz1+quiz2+quiz3)/3

print(f"Hello {first_name}.")
print(f'Quiz 1 score: {quiz1}')
print(f'Quiz 2 score: {quiz2}')
print(f'Quiz 3 score: {quiz3}')
print(f'Quiz Average: {average_score}')

# Practice B 

first_name = input("Enter your first name: \n")

distance = float(input("Enter distance travelled in miles: \n"))
gasoline_used = float(input('Enter the number of gallons of gasoline used today: \n'))

miles_per_gallon = distance/gasoline_used

print(f'Hello {first_name}.')
print(f'You have driven {distance} miles today.')
print(f'You have used {gasoline_used} gallons of gasoline today.')
print(f'You have used {miles_per_gallon} miles per gallon on the car.')