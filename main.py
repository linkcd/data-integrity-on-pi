import time
import threading
from helpers.dataintegrityhelper import *
from helpers.sensehathelper import *

#for printing color
from colorama import init
init()
from colorama import Fore, Back, Style

#variables
count = 0
animation_refresh_intervals = 0.1 #smaller is faster

#setup sense hat
hat = SenseHat()
hat.set_rotation(180)
hat.low_light = True


def display_loading_while_waiting_for_done(e, t, hat):
    step = 1
    while not e.isSet():
        event_is_set = e.wait(t)
        if event_is_set:
            display_as_attached_successfully(hat)
        else:
            display_as_attaching_to_tangle(hat, step)
            step += 1

while True:   
    global count

    temp = str(round(hat.get_temperature(), 2))
    print("")
    print("#" + str(count) + " - Temperature: %s" %temp)
    #print("#%d:" %count, "Temperature:%s" %temp)

    hat.show_message("Temp:%s" % temp, scroll_speed=0.1)

    payload = get_payload(count, temp)
    
    #start attaching to tangle
    attachedDoneEvent = threading.Event()
    showAttachingThread = threading.Thread(name='loading_screen_thread', target=display_loading_while_waiting_for_done, args=(attachedDoneEvent, animation_refresh_intervals, hat))
    showAttachingThread.start()

    print(Fore.GREEN + "Submitting data integrity information to distributed ledger (IOTA tangle)...")
    r = send_data_integrity_info(payload)
    if r == "":
        print(Fore.RED + "Failed...")
    else:
        print(Fore.WHITE + str(r))
        print(Fore.GREEN + "Submitted successfully!")
    print(Style.RESET_ALL)
    attachedDoneEvent.set()

    time.sleep(3)

    count += 1