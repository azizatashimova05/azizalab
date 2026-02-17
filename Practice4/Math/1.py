import math

degree = float(input("Input degree: "))
radian = degree * (math.pi / 180)
# Or simply: radian = math.radians(degree)

print(f"Output radian: {radian:.6f}")
