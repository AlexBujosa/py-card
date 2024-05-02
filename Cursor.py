import sys
from typing import Callable

class Cursor:
    def print_at_position(self, x, y, text):
        # Move cursor to position
        sys.stdout.write("\033[%d;%dH" % (y, x))
        # Print text
        sys.stdout.write(text)
        sys.stdout.flush()
        
    def print_at_position_with_method(self, x, y, text, method: Callable[[], None]):
        sys.stdout.write("\033[%d;%dH" % (y, x))
        
        method(text)
        
        