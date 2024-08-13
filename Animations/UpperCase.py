import time
import sys

def play_upper_case():
    string = "awesome uppercase animation"
    while True:
        for i in range(len(string)):
            modified_string = ""
            for j in range(len(string)):
                if j == i:
                    modified_string += string[j].upper()
                elif j == i - 1:
                    modified_string += string[j].lower()
                else:
                    modified_string += string[j]
            
            sys.stdout.write('\r' + modified_string)
            sys.stdout.flush()
            time.sleep(0.1)

play_upper_case()