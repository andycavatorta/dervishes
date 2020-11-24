import importlib
import os
import queue
import sys
import threading
import time

app_path = os.path.dirname((os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
sys.path.append(os.path.split(app_path)[0])

import settings
from thirtybirds3 import thirtybirds
from thirtybirds3.adapters.actuators import roboteq_command_wrapper


class Roboteq_Data_Receiver(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.queue = queue.Queue()
        self.start()

    def add_to_queue(self, message):
        self.queue.put(message)

    def run(self):
        while True:
            message = self.queue.get(True)
            print("data",message)
            #if "internal_event" in message:
            #    pass

roboteq_data_receiver = Roboteq_Data_Receiver()


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

        self.controllers = roboteq_command_wrapper.Controllers(
            roboteq_data_receiver.add_to_queue, 
            self.status_receiver, 
            self.network_status_change_handler, 
            {"C3-D3":settings.Roboteq.BOARDS["C3-D3"]},
            {
                "C3":settings.Roboteq.MOTORS["C3"],
                "D3":settings.Roboteq.MOTORS["D3"],
            }
        )

        self.tb.subscribe_to_topic("C3")
        self.tb.subscribe_to_topic("D3")
        self.start()

    def network_message_handler(self,topic, message, origin):
        print("network_message_handler",topic, message, origin)
        self.add_to_queue(topic, message, origin)
    def network_status_change_handler(self, status, hostname):
        print("network_status_change_handler", status, hostname)
    def exception_handler(self, exception):
        print("exception_handler",exception)
    def add_to_queue(self, topic, message, origin):
        self.queue.put((topic, message, origin))

    def run(self):
        while True:
            try:
                topic, message, origin = self.queue.get(True)
                print(topic, message, origin)
                pitch = message["pitch"]
                volume = message["volume"]
                if topic == b"C3":
                    if pitch=="0":
                        speed = 0
                    if pitch=="C3":
                        speed = 0
                    if pitch=="C4":
                        speed = 0
                    if pitch=="G4":
                        speed = 0
                    if pitch=="C5":
                        speed = 0
                    if pitch=="E5":
                        speed = 0
                    if pitch=="G4":
                        speed = 0
                    self.controllers.motors["C3"].set_motor_speed(speed)

                if topic == b"D3":
                    if pitch=="0":
                        speed = 0
                    if pitch=="D3":
                        speed = 0
                    if pitch=="D4":
                        speed = 0
                    if pitch=="A4":
                        speed = 0
                    if pitch=="D5":
                        speed = 0
                    if pitch=="Gb5":
                        speed = 0
                    if pitch=="A5":
                        speed = 0
                    self.controllers.motors["D3"].set_motor_speed(speed)

            except Exception as e:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                print(e, repr(traceback.format_exception(exc_type, exc_value,exc_traceback)))
main = Main()

#####################################################################


class Roboteq_Data_Receiver(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.queue = queue.Queue()
        self.start()

    def add_to_queue(self, message):
        self.queue.put(message)

    def run(self):
        while True:
            message = self.queue.get(True)
            print("data",message)
            #if "internal_event" in message:
            #    pass

roboteq_data_receiver = Roboteq_Data_Receiver()

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
        self.controllers = roboteq_command_wrapper.Controllers(
            roboteq_data_receiver.add_to_queue, 
            self.status_receiver, 
            self.network_status_change_handler, 
            {"bow":settings.Roboteq.BOARDS["bow"]},
            {
                "bow_height":settings.Roboteq.MOTORS["bow_height"],
                "bow_rotation":settings.Roboteq.MOTORS["bow_rotation"],
            }
        )
        self.tb.subscribe_to_topic("horsewheel_lifter_home")
        self.tb.subscribe_to_topic("horsewheel_speed")
        self.tb.subscribe_to_topic("horsewheel_lifter_position")
        self.tb.publish("horsewheel_connected", True)
        self.start()

    def macro_callback(self, motor_name, action, status):
        print("macro_callback",motor_name, action, status)
        if motor_name == "bow_height":
            if action == 'go_to_limit_switch':
                self.tb.publish("horsewheel_lifter_home", False)
                self.add_to_queue(b"set_bow_height_speed", 1000)

    def status_receiver(self, msg):
        print("status_receiver", msg)
    def network_message_handler(self,topic, message):
        print("network_message_handler",topic, message)
        self.add_to_queue(topic, message)
    def exception_handler(self, exception):
        print("exception_handler",exception)
    def network_status_change_handler(self, status, hostname):
        print("network_status_change_handler", status, hostname)
    def add_to_queue(self, topic, message):
        self.queue.put((topic, message))

    def run(self):
        
        while True:
            try:
                topic, message = self.queue.get(True)
                print(topic, message)
                if topic == b"horsewheel_lifter_home":
                    self.controllers.macros["bow_height"].go_to_limit_switch({}, self.macro_callback)
                    #self.controllers.macros["bow_height"].add_to_queue("go_to_limit_switch")
                    #self.tb.publish("horsewheel_lifter_home", True)
                if topic == b"horsewheel_speed":
                    self.controllers.macros["bow_rotation"].set_speed(int(message))
                if topic == b"horsewheel_lifter_position":
                    self.controllers.motors["bow_height"].set_acceleration(10)
                    self.controllers.motors["bow_height"].set_deceleration(10)
                    self.controllers.motors["bow_height"].set_operating_mode(3) 
                    #self.controllers.motors["bow_height"].set_motor_speed(100)
                    print("________", int(message))
                    self.controllers.motors["bow_height"].go_to_absolute_position(int(-message))
                    #self.controllers.macros["bow_height"].go_to_absolute_position({"position":int(-message), "speed":50})
                if topic == b"set_bow_height_speed":
                    self.controllers.motors["bow_height"].set_default_velocity_in_position_mode(int(message))

            except Exception as e:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                print(e, repr(traceback.format_exception(exc_type, exc_value,exc_traceback)))
main = Main()

