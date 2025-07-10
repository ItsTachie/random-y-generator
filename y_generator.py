import turtle
import tkinter as tk
import random

def offset():
    return random.randint(105,135)

def draw_y():
    btn.config(state=tk.DISABLED)
    t.clear()
    rotation = random.randint(0,90)

    for _ in range (3):
        rotation += offset()
        t.left(rotation)

        # draw first line
        t.forward(random.randint(50,150))


        t.home()

    btn.config(state=tk.NORMAL)

# Create the main Tkinter window
root = tk.Tk()
root.title("Random Y Generator")

# Create a Tkinter Canvas for the turtle graphics
turtle_canvas = tk.Canvas(root, width=400, height=400)
turtle_canvas.pack(padx=20, pady=20)

# Create a TurtleScreen from the Tkinter Canvas
turtle_screen = turtle.TurtleScreen(turtle_canvas)

# Create a RawTurtle object on the TurtleScreen
t = turtle.RawTurtle(turtle_screen)
t.pensize(3)
t.speed(10)
t.hideturtle()


# Create a Tkinter Button and associate it with the draw_circle function
btn = tk.Button(root, text="Generate", command=draw_y)
btn.pack(padx=20, pady=20)

draw_y()


# Start the Tkinter event loop
root.mainloop()