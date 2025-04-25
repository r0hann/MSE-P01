def areaOfLand(length, width):
    landArea = length * width
    intArea = int(landArea)
    return landArea, intArea
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = areaOfLand(length, width)
print("Area of Land:", area);