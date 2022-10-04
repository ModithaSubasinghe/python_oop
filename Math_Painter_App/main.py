from Math_Painter_App.canvas import Canvas
from Math_Painter_App.shapes import Rectangle, Square

#Get canvas width and height from the user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

#Make a dictionary of color codes and prompt for color
colors = {"white": (255,255,255), "black": (0,0,0)}
canvas_color = input("Enter canvas color(white or black): ")

#Create a canvas with the user data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type=input("What do you like to draw(square or rectangle)? Enter quit to quit  ")
    # Ask for rectangle data and create rectangle if user entered 'rectangle'
    if shape_type.lower()=="rectangle":
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter width of the rectangle: "))
        rec_height = int(input("Enter height of the rectangle: "))
        red = int(input("How much red should the rectangle have? "))
        green = int((input("How much green? ")))
        blue = int((input("How much blue? ")))

        #create the rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red,green,blue))
        r1.draw(canvas)

    #Ask for square data and create square if user entered 'square'
    if shape_type.lower() == "square":
        sqr_x = int(input("Enter x of the square: "))
        sqr_y = int(input("Enter y of the square: "))
        sqr_side = int(input("Enter side length of the square: "))
        red = int(input("How much red should the rectangle have? "))
        green = int((input("How much green? ")))
        blue = int((input("How much blue? ")))

        s1 = Square(x=sqr_x, y=sqr_x, side=sqr_side, color=(red, green, blue))
        s1.draw(canvas)

    if shape_type == 'quit':
        break

canvas.make('files/canvas.png')