def create_rectangle(width, height):
    # Initialize an empty string to build the rectangle
    rectangle = ""

    # Loop through the rows (height)
    for i in range(height):
        # Loop through the columns (width)
        for j in range(width):
            # Append a "*" character to the rectangle string
            rectangle += "*"
        # Add a newline character to move to the next row
        rectangle += "\n"

    return rectangle

# Get user input for width and height
width = int(input("Enter the width of the rectangle: "))
height = int(input("Enter the height of the rectangle: "))

# Call the function and print the resulting rectangle
result = create_rectangle(width, height)
print(result)

