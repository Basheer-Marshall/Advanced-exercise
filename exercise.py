import math
a = 5
b = 10
c = 7

a += 3

b *= 2

c %= 4

result = math.sqrt(a**2 + b**2 + c**2)

print(f"{result:.2f}")






x = int(input("Enter an integer for x: "))
y = int(input("Enter an integer for y: "))
z = int(input("Enter an integer for z: "))

is_even = x % 2 == 0
is_positive = y > 0
is_in_range = 10 <= z <= 50

final_condition = is_even and is_positive and is_in_range

print(final_condition)




base_score = float(input("Enter your base score: "))

adjusted_score = base_score + 5 - 10

final_score = max(0.0, min(adjusted_score, 100.0))

if final_score >= 90:
    grade = "A"
elif final_score >= 80:
    grade = "B"
elif final_score >= 70:
    grade = "C"
elif final_score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Final Score: {final_score}")
print(f"Grade: {grade}")
