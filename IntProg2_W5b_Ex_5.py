import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# global constants
WIDTH = 600
HEIGHT = 600

click_pos = [WIDTH/2, HEIGHT/2]

IMG_WIDTH = 720
IMG_HEIGHT = 720
SCALE = 0.5
img_center = [IMG_WIDTH//2, IMG_HEIGHT//2]
img_size = [IMG_WIDTH, IMG_HEIGHT]

w_size = [IMG_WIDTH*SCALE, IMG_HEIGHT*SCALE]

# load test image
img = simplegui.load_image('http://i.imgur.com/sX0CCcJ.jpg')

# mouseclick handler
def click(pos):
    global click_pos
    click_pos  = list(pos)

    
# draw handler
def draw(canvas):
    canvas.draw_image(img, img_center, img_size,
                      click_pos, w_size)

    
# create frame and register draw handler    
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")


frame.set_mouseclick_handler(click)    
frame.set_draw_handler(draw)


# start frame
frame.start()
