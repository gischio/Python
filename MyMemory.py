# implementation of card game - Memory

import simpleguitk as simplegui
import random

# preparing deck
card_deck = range(0,8)
list_2 = range(0,8)
card_deck.extend(list_2)

# list of images
card_back = simplegui.load_image('http://media-hearth.cursecdn.com/attachments/4/578/icecrown.png')
card_0 = simplegui.load_image('http://www.schiochet.it/wp-admin/devimg/FF-Menu-0-300px.png')
card_1 = simplegui.load_image('http://www.schiochet.it/wp-admin/devimg/FF-Menu-1-300px.png')
card_2 = simplegui.load_image('http://www.schiochet.it/wp-admin/devimg/FF-Menu-2-300px.png')
card_3 = simplegui.load_image('http://www.schiochet.it/wp-admin/devimg/FF-Menu-3-300px.png')
card_4 = simplegui.load_image('http://www.schiochet.it/wp-admin/devimg/FF-Menu-4-300px.png')
card_5 = simplegui.load_image('http://www.schiochet.it/wp-admin/devimg/FF-Menu-5-300px.png')
card_6 = simplegui.load_image('http://www.schiochet.it/wp-admin/devimg/FF-Menu-6-300px.png')
card_7 = simplegui.load_image('http://www.schiochet.it/wp-admin/devimg/FF-Menu-7-300px.png')

card_list = [card_0, card_1, card_2, card_3, card_4, card_5, card_6, card_7]

# helper function to initialize globals
def new_game():
    global exposed, state, card_1, card_2, counter
    exposed = [False] * 16
    card_1 = 0
    card_2 = 0
    state = 0
    counter = 0
    label.set_text("Turns = " + str(counter))
    random.shuffle(card_deck)   
    
# define event handlers
def mouseclick(pos):
    global state
    # card values and indexes are global, to be checked 
    # in the if statements
    global card_1, card_2, i1, i2, counter
    index = pos[0] // 50;
    if exposed[index]:     
        pass
    else:
        if state == 0:
            i1 = index
            exposed[i1] = True
            card_1 = card_deck[i1]
            state = 1
        elif state == 1:
        # 1 card is exposed
            i2 = index
            exposed[i2] = True
            card_2 = card_deck[i2]
            state = 2
        # update attempts
            counter += 1
            label.set_text("Turns = " + str(counter))
        else:
        # 2 cards are exposed
            if card_1 != card_2:
                exposed[i1] = False
                exposed[i2] = False
            i1 = index    
            exposed[i1] = True
            card_1 = card_deck[i1]
            state = 1    
                     
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for n, val in enumerate(card_deck):
        if exposed[n] == True:
            canvas.draw_image(card_list[val], (50 // 2, 100 // 2), (50, 100), (25 + 50*n, 50), (50, 100))
        else:
            canvas.draw_image(card_back, (241 // 2, 359 // 2), (241, 359), (25 + 50*n, 50), (50, 100))
              
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()