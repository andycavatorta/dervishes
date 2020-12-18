import importlib
import mido
import os
import queue
import sys
import threading
import time

app_path = os.path.dirname((os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
print(app_path)
sys.path.append(os.path.split(app_path)[0])

import settings
from thirtybirds3 import thirtybirds
#from thirtybirds3.dev.hid.oxygen88 import oxygen88

class Main(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.tb = thirtybirds.Thirtybirds(
            settings, 
            app_path,
            self.network_message_handler,
            self.network_status_change_handler,
            self.exception_handler
        )
        self.queue = queue.Queue()
        self.tb.subscribe_to_topic("")

        # set up to Oxygen88 Keyboard
        # if present
            # load libraries
        # else
            # stop setup?

        # set up midi file sources?

        # look for all hosts defined in settings
        # if any not present
            # report which are missing
            # ^ repeat
        
        # start GUI in BASH or HTTP

        print(self.tb.hardware_management.get_system_status())
        self.start()

    def network_message_handler(self, topic, message, origin, destination):
        self.add_to_queue(topic, message, origin, destination)
    def exception_handler(self, exception):
        print("exception_handler",exception)
    def network_status_change_handler(self, status, hostname):
        print("network_status_change_handler", status, hostname)

    def add_to_queue(self, topic, message):
        self.queue.put((topic, message))
    def run(self):
        while True:
            try:
                topic, message, origin, destination = self.queue.get(True)
                print(">>>",topic, message, origin, destination)

            except Exception as e:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                print(e, repr(traceback.format_exception(exc_type, exc_value,exc_traceback)))
main = Main()

class MIDI(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        #self.last_horsewheel_speed = 0
        self.wheel_lifter_coarse = 0
        self.wheel_lifter_fine = 0
        self.start()
    def run(self):
        time.sleep(1)
        """
        with mido.open_input("Oxygen 88:Oxygen 88 MIDI 1 20:0") as inport:
            for midi_o in inport:
                #print(midi_o)
                if midi_o.type == "note_on":
                    main.add_to_queue("pitch_slider_position", ((midi_o.note-21)*30000)+100000 )
                    continue
                if midi_o.type == "control_change":
                    if midi_o.control == 73: # pitch fine
                        continue
                    if midi_o.control == 74: # wheel lift coarse
                        self.wheel_lifter_coarse = midi_o.value * 5000
                        main.add_to_queue("horsewheel_lifter_position", self.wheel_lifter_coarse + self.wheel_lifter_fine)
                        continue
                    if midi_o.control == 71: # wheel lift fine
                        self.wheel_lifter_fine = midi_o.value * 100
                        main.add_to_queue("horsewheel_lifter_position", self.wheel_lifter_coarse + self.wheel_lifter_fine)
                        continue
                    if midi_o.control == 91: # wheel speed
                        main.add_to_queue("horsewheel_speed", midi_o.value)
                        continue
                    if midi_o.control == 93: # wheel slide
                        main.add_to_queue("horsewheel_slider_position", ((midi_o.value)*10000)+20000)
                        continue
                    if midi_o.control == 5: # vibrato depth
                        pass
                    if midi_o.control == 84: # vibrato speed
                        pass
        """
midi = MIDI()
