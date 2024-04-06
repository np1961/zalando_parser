
from time import sleep
from sys import stdout
from sys import path

from colorama import Fore as COLORS_FRONT
from colorama import Back as COLORS_BACK

def terminal_write(text,
                   time_sleep=0.008,
                   endl=True):

    text=text if not endl else f"{text}\n"
    
    for _text_ in text:
        stdout.write(_text_)
        stdout.flush()
        sleep(time_sleep)
        
def change_colors(index_front=0 , index_back=0):

    colors_names=['RESET','BLUE', 'GREEN', 'MAGENTA', 'RED', 'WHITE', 'YELLOW']
    
    index_front=index_front%len(colors_names)
    index_back=index_back%len(colors_names)

    color_front_name=colors_names[index_front]
    color_back_name=colors_names[index_back]
    
    color_front=COLORS_FRONT.__dict__[color_front_name]
    color_back=COLORS_BACK.__dict__[color_back_name]

    stdout.write(color_front)
    stdout.write(color_back)
    
    
    
    
        

