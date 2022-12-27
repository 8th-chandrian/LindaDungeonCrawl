import time


def print_delay(text_arr, delay):
    for text in text_arr:
        print(text)
        time.sleep(delay)