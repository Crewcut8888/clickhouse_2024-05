import datetime

from pynput import mouse

from models import mouse_movementsBuffer

from infi.clickhouse_orm import Database

import datetime

import gi
gi.require_version("Wnck", "3.0")
from gi.repository import Wnck

def on_move(x, y):
    global prevx, curx, prevy, cury
    prevx = curx
    curx = x
    prevy = cury
    cury = y
    timestamp = datetime.datetime.now().timestamp()
    scr = Wnck.Screen.get_default()
    scr.force_update()
    result = []
    result.append(mouse_movementsBuffer(x=x, y=y, deltaX=curx - prevx, deltaY=cury - prevy,clientTimeStamp=timestamp, button=0, target=scr.get_active_window().get_name()))
    db.insert(result)

def on_click(x, y, button, pressed):
    global prevx, curx, prevy, cury
    prevx = curx
    curx = x
    prevy = cury
    cury = y
    timestamp = datetime.datetime.now().timestamp()
    scr = Wnck.Screen.get_default()
    scr.force_update()
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    result = []
    result.append(mouse_movementsBuffer(x=x, y=y, deltaX=curx - prevx, deltaY=cury - prevy,clientTimeStamp=timestamp, button=str(button).replace('Button.left', '1').replace('Button.right', '2'), target=scr.get_active_window().get_name()))
    db.insert(result)

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

if __name__ == '__main__':
    db = Database('default')
    db.create_table(mouse_movementsBuffer)
    prevx = 0
    curx = 0
    prevy = 0
    cury = 0

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