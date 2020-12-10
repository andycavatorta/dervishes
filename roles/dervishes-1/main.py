import os
import queue
import sys
import threading
import time

app_path = os.path.dirname((os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
sys.path.append(os.path.split(app_path)[0])

import settings
from thirtybirds3 import thirtybirds
from thirtybirds3.dev.motion_control.sdc2160 import sdc2160


class Main(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.queue = queue.Queue()

        self.tb = thirtybirds.Thirtybirds(
            settings, 
            app_path,
            self.network_message_handler,
            self.network_status_change_handler,
            self.exception_handler
        )

        self.controllers = sdc2160.Main(
            {
                "board-1":settings.Roboteq.BOARDS["board-1"]
            },
            {
                "C3":settings.Roboteq.MOTORS["C3"],
                "D3":settings.Roboteq.MOTORS["D3"],
            },
            self.sdc2160_message_handler,
            self.sdc2160_status_handler, 
            self.exception_handler,
            self.tb
        )

        # make shorter names
        self.board = self.controllers.boards["board-1"]
        self.motors = {
            "C3":self.controllers.motors["C3"],
            "D3":self.controllers.motors["D3"],
        }

        self.motors["C3"].home()
        self.motors["D3"].home()
        self.start()
        self.tb.subscribe_to_topic("C3")
        self.tb.subscribe_to_topic("D3")
    
    def network_message_handler(self,topic, message, origin):
        print("network_message_handler",topic, message, origin)
        self.add_to_queue(topic, message, origin)
    def network_status_change_handler(self, status, hostname):
        print("network_status_change_handler", status, hostname)
    def exception_handler(self, exception):
        print("exception_handler",exception)
    def sdc2160_message_handler(self, message:)
        print("roboteq_message_handler:", message)
    def sdc2160_status_handler(self, message):
        print("status_handler",message)

    def add_to_queue(self, topic, message, origin, destination):
        self.queue.put((topic, message, origin, destination))

    def run(self):

        while True:
            try:
                topic, message, origin, destination = self.queue.get(True)
                print(topic, message, origin, destination)

                if topic == b"C3":
                    speed = settings.pitches_to_speeds["C3"][message]
                    self.controllers.motors["C3"].set_motor_speed(speed)

                if topic == b"D3":
                    speed = settings.pitches_to_speeds["D3"][message]
                    self.controllers.motors["D3"].set_motor_speed(speed)

            except Exception as e:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                print(e, repr(traceback.format_exception(exc_type, exc_value,exc_traceback)))

