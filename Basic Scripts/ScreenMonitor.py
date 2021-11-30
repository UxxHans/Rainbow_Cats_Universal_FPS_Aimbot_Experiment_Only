from mss import mss
from screeninfo import get_monitors


class ScreenCapture:

    @staticmethod
    def get_screen(capture_width, capture_height, monitor_width, monitor_height):
        bounding_box = {
            'top': int((monitor_height - capture_height) / 2),
            'left': int((monitor_width - capture_width) / 2),
            'width': capture_width,
            'height': capture_height
        }

        sct = mss()
        sct_img = sct.grab(bounding_box)
        return sct_img

    @staticmethod
    def get_screen_size():
        monitor_width = get_monitors()[0].width
        monitor_height = get_monitors()[0].height
        monitor_size = [monitor_width, monitor_height]
        return monitor_size
