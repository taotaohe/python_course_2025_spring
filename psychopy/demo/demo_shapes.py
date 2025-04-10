#!/usr/bin/env python3
#
# Description:
# Move the rectangle along the line and change the filling color of
# the polygon when it overlaps with the rectangle

from psychopy import visual, event, core

# Open a Window
win = visual.Window(size=[800, 600], units='pix')

# Line
line_vertices = [(-400, -300), (400, 300)]
line = visual.ShapeStim(win, vertices=line_vertices,
                        lineColor='white', closeShape=False)

# Rectangle
rect_vertices = [(-400, -300), (-320, -300), (-320, -240), (-400, -240)]
rect = visual.ShapeStim(win, vertices=rect_vertices,
                        fillColor='blue', lineWidth=0)

# Polygon
poly = visual.Polygon(win, edges=6, radius=100, fillColor='green')

# make the rectangle moving
while True:
    if rect.overlaps(poly):
        poly.fillColor = 'red'
    else:
        poly.fillColor = 'green'
    line.draw()
    poly.draw()
    rect.draw()
    win.flip()
    # Update the position of the rectangle following each flip
    rect.pos += (.4, .3)
    # Break out when the rectangle reaches the end of the line
    if rect.contains((400, 300)):
        break

# Close the window and quit PsychoPy
win.close()
core.quit()
