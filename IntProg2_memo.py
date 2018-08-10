# implementation of card game - Memory

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

COUNT = 0
cards_list = [x for x in range(0, 8)]*2
random.shuffle(cards_list)
exposed_list = []

for i in range(16):
    exposed_list.append(False)
# helper function to initialize globals
def new_game():
    global state, COUNT
    label.set_text('Turns = 0')
    COUNT = 0
    state = 0
    random.shuffle(cards_list)
    for i in range(16):
        exposed_list[i] = False
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, card_1, card_2, COUNT
    n = pos[0]//50

    if exposed_list[n] == False:
        if state == 0:
            exposed_list[n] = True 
            card_1 = n                    
            state = 1
            COUNT += 1            
        elif state == 1:
            exposed_list[n] = True            
            card_2 = n
            state = 2   
        else:
            exposed_list[n] = True
            if not cards_list[card_1] == cards_list[card_2]:
                exposed_list[card_1] = False
                exposed_list[card_2] = False
                card_1 = n
                state = 1
                COUNT += 1
            else:
                card_1 = n
                state = 1
                COUNT += 1
        label.set_text('Turns = ' + str(COUNT))               
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards_list
    for i in range(0, 16):
        if not exposed_list[i]:            
            canvas.draw_polygon([[i*50, 100], [i*50, 0], [i*50+50, 0], [i*50+50, 100]], 1, 'Green', 'Green')
        else:
            canvas.draw_text(str(cards_list[i]), [i*50+10, 80], 80, 'Red')
    for j in range(1, 16):
        canvas.draw_line((j*50, 0), (j*50, 100), 1, 'Yellow')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
label.set_text('Turns = ' )

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
