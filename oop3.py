# Function to calculate Area and Perimeter in the given list

def area(length, width):
    return length * width

def perimeter(length, width):
    return 2 * (length + width)


rectangle = [10, 501, 22, 37, 100, 999, 87, 351]

# Assuming the list contains pairs of length and width
for i in range(0, len(rectangle), 2):
    length = rectangle[i]
    width = rectangle[i + 1]

    # Calculate and print area and perimeter
    print(f"Rectangle with length {length} and width {width}:")
    print(f"Area: {area(length, width)}")
    print(f"Perimeter: {perimeter(length, width)}")
    print()
