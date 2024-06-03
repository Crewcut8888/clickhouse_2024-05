from pynput import mouse

import gi
gi.require_version("Wnck", "3.0")
from gi.repository import Wnck

prevx = 0
curx = 0
prevy = 0
cury = 0

def on_move(x, y):
    global prevx, curx, prevy, cury
    prevx = curx
    curx = x
    prevy = cury
    cury = y
    print(curx - prevx)
    print(cury - prevy)
    print('Pointer moved to {0}'.format(
        (x, y)))
    scr = Wnck.Screen.get_default()
    scr.force_update()
    print(scr.get_active_window().get_name())



    """ x Int16 - текущая координата X
    y Int16 - текущая координата Y
    deltaX Int16 - смещение по оси X
    deltaY Int16 - смещение по оси Y
    clientTimeStamp Float32 - время получения данных
    button Int8 - код кнопки мыши
    target String - название окна (объекта интерфейса, на котором произошло событие)
 """

def on_click(x, y, button, pressed):
    print(str(button).replace('Button.left', '1').replace('Button.right', '2'))
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    #if not pressed:
        # Stop listener
        #return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()