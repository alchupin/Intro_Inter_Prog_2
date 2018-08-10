import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# global constants
WIDTH = 400
HEIGHT = 300

click_pos = [WIDTH/2, HEIGHT/2]

IMG_WIDTH = 95
IMG_HEIGHT = 93
img_center = [IMG_WIDTH//2, IMG_HEIGHT//2]
img_size = [IMG_WIDTH, IMG_HEIGHT]
# load test image
img = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png')

# mouseclick handler
def click(pos):
    global click_pos
    click_pos  = list(pos)

    
# draw handler
def draw(canvas):
    canvas.draw_image(img, img_center, img_size,
                      click_pos, img_size)

    
# create frame and register draw handler    
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")


frame.set_mouseclick_handler(click)    
frame.set_draw_handler(draw)


# start frame
frame.start()
