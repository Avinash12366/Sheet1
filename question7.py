a = int(input("Enter angle 1: "))
b = int(input("Enter angle 2: "))
c = int(input("Enter angle 3: "))
if a + b + c != 180:
    print("Not a valid triangle")
elif 90 in [a, b, c]:
    print("Right triangle")
elif a > 90 or b > 90 or c > 90:
    print("Obtuse triangle")
else:
    print("Acute triangle")
