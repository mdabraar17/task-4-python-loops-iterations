# Demonstration of loops and iterations
print("1 Printing numbers from 1 to 100 using for loop")
for i in range(1, 101):
    print(i, end=" ")

print("\n\n2 Printing countdown timer using while loop")
count = 5
while count > 0:
    print("Countdown:", count)
    count -= 1
print("Time's up!")

print("\n3 break and continue demonstration")
for num in range(1, 11):
    if num == 5:
        print("Breaking loop at", num)
        break
    if num == 3:
        print("Skipping", num)
        continue
    print("Number:", num)

print("\n4 Iterating over characters in a string")
name = "Python"
for char in name:
    print(char)

print("\n5 Multiplication table of 5")
number = 5
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print("\n6 Using range with steps (even numbers)")
for i in range(2, 21, 2):
    print(i, end=" ")

print("\n\n7 Loop with condition (checking even or odd)")
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")

print("\n8 Real-world example: Attendance check")
students = ["Aman", "Ravi", "Sara", "Neha"]
for student in students:
    print(student, "is present")
