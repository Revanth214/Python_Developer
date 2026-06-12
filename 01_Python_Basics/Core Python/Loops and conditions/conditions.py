# 1. Basic if :- Use 'if' to run code when a condition is true
age = 18
if age >= 18:
    print("Adult")

# 2. if ... else :- Use else to run fallback code when the if condition is false.
age = 15
if age >= 18:
    print("Adult")
else:
    print("Minor")


# 3. if ... elif ... else :- Use elif to test additional conditions when the first one is false.
score = 75
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D or F"
print(grade)


# 4. Multiple elif branches :- You can have as many elif branches as needed.
value = 0
if value > 0:
    result = "positive"
elif value < 0:
    result = "negative"
elif value == 0:
    result = "zero"
else:
    result = "unknown"
print(result)

# 5. Nested if :- You can put an if inside another block.
x = 10
if x > 0:
    if x % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
else:
    print("Non-positive")

# 6. Conditions can be any Boolean expression :- Common uses include comparisons, membership, and logical operators.
name = "Alice"
if name == "Alice" and len(name) > 3:
    print("Hello Alice")

if x in [1, 2, 3]:
    print("x is 1, 2, or 3")

# 7. if with elif is evaluated top-down :- Only the first true branch runs. Later elif blocks are skipped once one branch matches.

# 8. Fallback else :- else is optional. If omitted and no condition matches, nothing happens.

# 9. Conditional expression (ternary operator) :- This is not a statement form of elif, but it uses if ... else in one line
result = "pass" if score >= 50 else "fail"
print(result)