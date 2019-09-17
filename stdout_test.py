import sys
import time

def restart_line():
    sys.stdout.write('\r'*4)
    sys.stdout.flush()

def print_line(text1='sample', text2='banana'):
    sys.stdout.write(text1)
    sys.stdout.flush()
    time.sleep(2) # wait 2 seconds...
    restart_line()
    sys.stdout.write(text2)
    sys.stdout.flush()
