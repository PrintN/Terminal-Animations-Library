import random
import time
import os
import shutil

SNOWFLAKE_CHARS = ['*','❄']

def initialize_snowflakes(num_snowflakes, width, height):
    return [{'x': random.randint(0, width - 1), 'y': random.randint(0, height - 1)} for _ in range(num_snowflakes)]

def play_snowing():
    base_num_snowflakes = 50
    while True:
        terminal_size = shutil.get_terminal_size()
        screen_width = terminal_size.columns
        screen_height = terminal_size.lines
        
        num_snowflakes = max(1, int((screen_width * screen_height) / (80 * 24)) * base_num_snowflakes)

        os.system('cls' if os.name == 'nt' else 'clear')
        
        screen = [[' ' for _ in range(screen_width)] for _ in range(screen_height)]
        
        global snowflakes
        snowflakes = initialize_snowflakes(num_snowflakes, screen_width, screen_height)

        for snowflake in snowflakes:
            snowflake['y'] += 0.5
            
            if int(snowflake['y']) >= screen_height:
                snowflake['y'] = 0
                snowflake['x'] = random.randint(0, screen_width - 1)
            
            char = random.choice(SNOWFLAKE_CHARS)
            
            if int(snowflake['y']) < screen_height:
                screen[int(snowflake['y'])][snowflake['x']] = char
            
        for line in screen:
            print(''.join(line))
            
        time.sleep(0.2)

play_snowing()