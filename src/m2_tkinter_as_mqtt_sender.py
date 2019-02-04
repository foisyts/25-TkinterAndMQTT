"""
Using a fake robot as the receiver of messages.
"""

# DONE: 1. In mqtt_remote_method_calls, set LEGO_NUMBER at line 131
# to YOUR robot's number.

# DONE: 2. Copy your Tkinter/ttk ROBOT gui code from the previous session (m6).
# Then modify it so that pressing a button sends a message to a teammate
# of the form:
#   (for Forward)
#        ["forward", X, y]
#   where X and Y are from the entry box.
#
# Implement and test.

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import time


def main():
    root = tkinter.Tk()
    root.title("MQTT Remote")

    name1 = input("Enter one name (sender name): ")
    name2 = input("Enter another name (receiver name): ")

    mqtt_client = com.MqttClient()
    mqtt_client.connect(name1, name2)
    time.sleep(1)

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()  # only grid call that does NOT need a row and column

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid()
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid()

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid()
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid()

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid()
    forward_button['command'] = lambda: mqtt_client.send_message("forward",
                                                                 [left_speed_entry.get(), right_speed_entry.get()])
    root.bind('<Up>', lambda event: print("Forward key"))

    root.mainloop()


main()
