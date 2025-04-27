# import pyautogui
# import time
# def draw_pyramid(levels):
#     time.sleep(3)
#     for i in range(1, levels + 1):
#         pyautogui.typewrite('#' * i)
#         pyautogui.press('enter')
# if __name__ == "__main__":
#     levels = int(input("Enter the number of levels for the pyramid: "))
#     draw_pyramid(levels)

import pyautogui
import time

# Wait 3 seconds to switch to the target application
time.sleep(3)

# Take input from the user
levels = int(input("Enter the number of levels: "))

# Draw the pyramid
for i in range(1, levels + 1):
    pyautogui.typewrite('#' * i)  # Type the '#' pattern
    pyautogui.press('enter')     # Press Enter to move to the next line
