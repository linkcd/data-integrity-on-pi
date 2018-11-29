from sense_hat import SenseHat

#LED display variables
r = (255, 0, 0)
g = (0, 255, 0)
n = (0,0,0) #nothing
y = (255, 255, 0)
w = (255,255,255)



static_unlocked = [
    n, n, n, n, n, w, w, n,
    n, n, n, n, w, n, n, w,
    n, n, n, n, w, n, n, w,
    n, n, n, n, w, n, n, n,
    r, r, r, r, r, r, n, n,
    r, r, r, r, r, r, n, n,
    r, r, r, r, r, r, n, n,
    r, r, r, r, r, r, n, n
]

locked = [
    n, n, n, w, w, n, n, n,
    n, n, w, n, n, w, n, n,
    n, n, w, n, n, w, n, n,
    n, n, w, n, n, w, n, n,
    n, g, g, g, g, g, g, n,
    n, g, g, g, g, g, g, n,
    n, g, g, g, g, g, g, n,
    n, g, g, g, g, g, g, n
]

def get_locking_current(step): #step can be from 1 to n, step 1 is init, then loop from 2 to 5
    o = g #light

    if step > 5:
        stepAfterModulo = step % 4 
        if stepAfterModulo < 2: # 0 or 1
            stepAfterModulo += 4;
    else:
        stepAfterModulo = step

    loadingLEDArray = {
        1: [o, n, n, n],
        2: [o, o, n, n],
        3: [n, o, o, n],
        4: [n, n, o, o],
        5: [o, n, n, o]
    }
    c= loadingLEDArray.get(stepAfterModulo, "invalid step") #current_loading_led_array

    unlocked = [
        c[0], c[1], n, n, n, w, w, n,
        c[3], c[2], n, n, w, n, n, w,
        n, n, n, n, w, n, n, w,
        n, n, n, n, w, n, n, n,
        r, r, r, r, r, r, n, n,
        r, r, r, r, r, r, n, n,
        r, r, r, r, r, r, n, n,
        r, r, r, r, r, r, n, n
    ]
    return unlocked



def get_fade_in_static_locking(step): #step from 1 to 8
    return 

def display_as_attaching_to_tangle(hat, step):
    hat.set_pixels(get_locking_current(step))

def display_as_attached_successfully(hat):
    hat.set_pixels(locked)
 