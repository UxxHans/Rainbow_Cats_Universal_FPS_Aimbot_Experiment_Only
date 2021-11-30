import win32api
import win32con
import pynput
import ctypes

screenWidth = 2560
screenHeight = 1440

SendInput = ctypes.windll.user32.SendInput
PUL = ctypes.POINTER(ctypes.c_ulong)


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class MouseHandler:
    @staticmethod
    def left_click():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    @staticmethod
    def move_mouse_simple(x, y):
        win32api.SetCursorPos((x, y))

    @staticmethod
    def move_mouse_advanced(x, y):
        x = 1 + int(x * 65536./screenWidth)
        y = 1 + int(y * 65536./screenHeight)
        extra = ctypes.c_ulong(0)
        ii_ = pynput._util.win32.INPUT_union()
        ii_.mi = pynput._util.win32.MOUSEINPUT(x, y, 0, (0x0001 | 0x8000), 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
        command = pynput._util.win32.INPUT(ctypes.c_ulong(0), ii_)
        SendInput(1, ctypes.pointer(command), ctypes.sizeof(command))
