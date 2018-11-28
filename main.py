import time
import threading
from helpers.dataintegrityhelper import *
from helpers.sensehathelper import *

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
            display_as_attached_successfuly(hat)
        else:
            display_as_attaching_to_tangle(hat, step)
            step += 1

while True:   
    global count

    temp = str(round(hat.get_temperature(), 2))
    print("")
    print("#%d:" %count, "Temperature:%s" %temp)

    hat.show_message("Temp:%s" % temp, scroll_speed=0.1)

    payload = get_payload(temp)
    
    #start attaching to tangle
    attachedDoneEvent = threading.Event()
    showAttachingThread = threading.Thread(name='loading_screen_thread', target=display_loading_while_waiting_for_done, args=(attachedDoneEvent, animation_refresh_intervals, hat))
    showAttachingThread.start()

    r = send_data_integrity_info(payload)
    print("Data integrity information is attached to tangle successfully!")
    print(r)
    attachedDoneEvent.set()

    time.sleep(2)

    count += 1