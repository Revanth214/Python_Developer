# Python loop examples

# 1. for loop over a list
fruits = ["apple", "banana", "cherry"]# Use 'for' when you want to iterate over a sequence
for fruit in fruits:# Common for patterns:1.iterate over a list, tuple, string, set, dictionary, or range. 2. use range() for numeric loops
    print("Fruit:", fruit)

print()

# 2. for loop over a range
for i in range(5):
    print("Count:", i)

print()

# 3. while loop
count = 0
while count < 5: # Use 'while' when you want to repeat until a condition changes
    print("While count:", count)
    count += 1

print()

# 4. break stops the loop early
for number in range(10):
    if number == 4:
        print("Breaking at", number)
        break
    print("Number before break:", number)

print()

# 5. continue skips to the next iteration
for number in range(6):
    if number % 2 == 0:
        continue
    print("Odd number:", number)

print()

# 6. else on a for loop runs only when the loop finishes normally
for number in range(3):
    print("Looping:", number)
else:
    print("For loop completed without break")

print()

# 7. else on a while loop works the same way
count = 0
while count < 3:
    print("While looping:", count)
    count += 1
else:
    print("While loop completed without break")

print()

# 8. nested loops
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row}, {col})", end=" ")
    print()

print()

# 9. using if/elif/else inside loops
scores = [95, 82, 67, 50, 30]
for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"Score {score} => Grade {grade}")
