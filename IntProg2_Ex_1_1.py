import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# initialize globals
width = 300
height = 300

# event handler for mouse click
def click(pos):
    print(pos)

# create frame
f = simplegui.create_frame('Mouse coordinates', width, height)
f.set_canvas_background('White')

# register event handler
f.set_mouseclick_handler(click)

# start frame
f.start()
