import pgzrun
import time, random
WIDTH=800
HEIGHT=600
CENTER=(400,300)
FINAL_LEVEL=6
START_SPEED=10
ITEMS={"bag","bottle","chips","battery"}
game_over=False
game_complete=False
current_level=1
items=[]
animations=[]

def draw():
    screen.clear()
    screen.blit("background",(0,0))
    if game_over:
        display_message("GAME OVER, TRY AGAIN")
    elif game_complete:
        display_message("GOOD JOB")
    else:
        for i in items:
            i.draw()
def update():
    global items
    if len(items)==0:
        items=make_items(current_level)
        

def make_items(number_of_extra_items):
    items_to_create=get_option_create(number_of_extra_items)
    new_items=create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items
def get_option_create(number_of_extra_items):
    items_to_create=["paper"]
    for a in range(0,number_of_extra_items):
        random_option=random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create


def create_items(items_to_create):
    new_items=[]
    global items
    for i in items_to_create:
        item=Actor(i+"img")
        new_items.append(item)

    return new_items        
        
    


def layout_items(items_to_layout):
    number_of_gaps=len(s_to_layout)+1
    
    gap_size=800/number_of_gaps
    random.shuffle(items_to_layout)
    for index, item in enumerate(items_to_layout):
        new_x_pos=gap_size*(index+1)
        item.x=new_x_pos
def animate_items(items_to_animate):
    global animations
    for i in items_to_animate:
        duration=START_SPEED-current_level
        i.anchor=("center","bottom")
        a=animate(i,duration=duration,on_finished=handle_game_over,y=HEIGHT)
        animations.append(a)

        
def handle_game_over():
    global game_over
    game_over=True
def on_mouse_down(pos):
    global items, current_level
    for i in items:
        if i.collidepoint(pos):
            if "paper" in i.image:
                handle_game_complete()
            else:
                handle_game_over()

def handle_game_complete():
    global game_complete,items, current_level
    stop_animation(animations)
    if current_level==FINAL_LEVEL:
        game_complete=True
    else:
        current_level=current_level+1
        animations=[]
        items=[]        
def stop_animation(animations_to_stop):
    for i in animations_to_stop:
        if i.running:
            i.stop()
def display_message(ht,sht):
    
    screen.draw.text(ht,fontsize=60,center=CENTER,color="white")
    if sht:
        screen.draw.text(sht,fontsize=30,center=(400,330),color="white")

pgzrun.go()
