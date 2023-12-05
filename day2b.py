height = input()
weight = input()

height_as_float = float(height)
weight_as_int = int(weight)

bmi = weight_as_int / (height_as_float * height_as_float)
bmi_as_int = int(bmi)
print(bmi_as_int)