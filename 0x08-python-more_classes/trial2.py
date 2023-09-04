def create_rectangle(width, height):
    # Use a list comprehension to create each row
    rows = ["*" * width for _ in range(height)]
    
    # Join the rows using newline characters to form the rectangle
    rectangle = "\n".join(rows)
    
    return rectangle

# Get user input for width and height
width = int(input("Enter the width of the rectangle: "))
height = int(input("Enter the height of the rectangle: "))

# Call the function and print the resulting rectangle
result = create_rectangle(width, height)
print(result)

