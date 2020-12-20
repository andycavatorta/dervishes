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
from thirtybirds3.dev.hid.oxygen88 import oxygen88

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
        #self.tb.subscribe_to_topic("")

        self.hostname = self.tb.get_hostname()
        self.midi = oxygen88.Main(self.hostname, self.add_to_queue)
        self.wing_to_controller = [
            "dervishes-1", #c3
            "dervishes-2", #C#3
            "dervishes-1", #D3
            "dervishes-3", #D#3
            "dervishes-2", #E3
            "dervishes-4", #F3
            "dervishes-3", #F#3
            "dervishes-5", #G
            "dervishes-4", #G#3
            "dervishes-6", #A3
            "dervishes-5", #A#3
            "dervishes-7", #B3
            "dervishes-6", #C4
            "dervishes-7", #c#4
        ]
        self.wing_busy_states = [0]*14
        self.pitch_to_wing = [
            [0],#24
            [1],#25
            [2],#26
            [3],#27
            [4],#28
            [5],#29
            [6],#30
            [7],#31
            [8],#32
            [9],#33
            [10],#34
            [11],#35
            [12,0],#36
            [13,1],#37
            [2],#38
            [3],#39
            [4],#40
            [5],#41
            [6],#42
            [7,0],#43
            [8,1],#44
            [9,2],#45
            [10,3],#46
            [11,4],#47
            [12,5,0],#48
            [13,6,1],#49
            [7,2],#50
            [8,3],#51
            [9,4,0],#52
            [10,5,1],#53
            [11,6,2],#54
            [12,7,3],#55
            [13,8,4],#56
            [9,5],#57
            [10,6],#58
            [11,7],#59
            [12,8],#60
            [13,9],#61
            [10],#62
            [11],#63
            [12],#64
            [13],#65
        ]
        # set up midi file sources?
        # look for all hosts defined in settings
        # if any not present
            # report which are missing
            # ^ repeat
        # start GUI in BASH or HTTP
        self.start()

    def find_wing_for_pitch(self,pitch,control):
        if 24 <= pitch <= 65:
            pitch_ordinal = pitch - 24
            wing_options = self.pitch_to_wing[pitch_ordinal]
            for wing_number in wing_options:
                if control == 'note_on':
                    if self.wing_busy_states[wing_number] == 0:
                        self.wing_busy_states[wing_number] = pitch
                        return wing_number
                else:
                    if self.wing_busy_states[wing_number] == pitch:
                        self.wing_busy_states[wing_number] = 0
                        return wing_number
            return -1
        return -1

    def network_message_handler(self, topic, message, origin, destination):
        self.add_to_queue(topic, message, origin, destination)
    def exception_handler(self, exception):
        print("exception_handler",exception)
    def network_status_change_handler(self, status, hostname):
        print("network_status_change_handler", status, hostname)

    def add_to_queue(self, topic, message, origin, destination ):
        self.queue.put((topic, message, origin, destination ))
    def run(self):
        while True:
            try:
                topic, message, origin, destination = self.queue.get(True)
                #print(">>>",topic, message, origin, destination)
                if topic == "oxygen88":
                    control,value = message
                    if control in ["note_on","note_off"]:
                        wing = self.find_wing_for_pitch(value, control)
                        if wing > -1:
                            controller = self.wing_to_controller[wing]
                            print(controller,[control,value])
                            self.tb.publish(controller,[control,value])

            except Exception as e:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                print(e, repr(traceback.format_exception(exc_type, exc_value,exc_traceback)))
main = Main()
