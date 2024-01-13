import tkinter as tk
from math import pi
# Function to calculate circumference and area of a circle
def calculate_circle_properties(radius):
    circumference = 2 * pi * radius
    area = pi * (radius ** 2)
    return circumference, area
# Get user input for width, height, radius, outline color, and fill color
width = int(input("Enter the width of the graphics window: "))
height = int(input("Enter the height of the graphics window: "))
background_color = input("Enter the background color of the graphics window: ")
radius = int(input("Enter the radius of the circle: "))
outline_color = input("Enter the outline color of the circle: ")
fill_color = input("Enter the fill color of the circle: ")
# Create the main window
root = tk.Tk()
root.title("Circle Drawing Example")
# Create a Canvas widget
canvas = tk.Canvas(root, width=width, height=height)
# Set the background color of the canvas
canvas.configure(bg=background_color)
# Pack the canvas into the main window
canvas.pack()
# Calculate the center of the canvas
center_x = width // 2
center_y = height // 2
# Draw the circle at the center
circle = canvas.create_oval(center_x - radius, center_y - radius, center_x +
radius, center_y + radius, outline=outline_color, fill=fill_color)
# Calculate circumference and area
circumference, area = calculate_circle_properties(radius)
# Print out the results
print("Circumference of the circle:", circumference)
print("Area of the circle:", area)
# Start the Tkinter event loop
root.mainloop()
