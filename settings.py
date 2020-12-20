"""
This file contains the default config data for the reports system

On start-up thirtybirds loads config data.  It loads default configs from config/ unless otherwise specified.  New config data can be loaded dynamically at runtime.

Typical usage example:

from config import reports

foo = ClassFoo(reports.foo_config)

"""

class Roles():
    controller_hostname="feral"
    hosts={
        "feral":"controller",
        "dervishes-1":"dervishes-1",
        "dervishes-2":"dervishes-2",
        "dervishes-3":"dervishes-3",
        "dervishes-4":"dervishes-4",
        "dervishes-5":"dervishes-5",
        "dervishes-6":"dervishes-6",
        "dervishes-7":"dervishes-7",
    }

class Reporting():
    app_name = "dervishes"
    #level = "ERROR" #[DEBUG | INFO | WARNING | ERROR | CRITICAL]
    #log_to_file = True
    #print_to_stdout = True
    publish_to_dash = True
    class Status_Types:
        EXCEPTIONS = True
        INITIALIZATIONS = True
        NETWORK_CONNECTIONS = True
        NETWORK_MESSAGES = True
        SYSTEM_STATUS = True
        VERSION_STATUS = True
        ADAPTER_STATUS = True

class Version_Control():
    update_on_start = False
    github_repo_owner = "andycavatorta"
    github_repo_name = "dervishes"
    branch = "master"

class Roboteq:
    BOARDS = {
        "board-1":{
            "mcu_id":"300:1058:2031663:1429493506:540422710",
            "serial_data_watchdog":0, #miliseconds
            "serial_echo":0, #0 = enabled, 1 is disabled
        },
        "board-2":{
            "mcu_id":"",
            "serial_data_watchdog":0, #miliseconds
            "serial_echo":0, #0 = enabled, 1 is disabled
        },
        "board-3":{
            "mcu_id":"",
            "serial_data_watchdog":0, #miliseconds
            "serial_echo":0, #0 = enabled, 1 is disabled
        },
        "board-4":{
            "mcu_id":"",
            "serial_data_watchdog":0, #miliseconds
            "serial_echo":0, #0 = enabled, 1 is disabled
        },
        "board-5":{
            "mcu_id":"",
            "serial_data_watchdog":0, #miliseconds
            "serial_echo":0, #0 = enabled, 1 is disabled
        },
        "board-6":{
            "mcu_id":"",
            "serial_data_watchdog":0, #miliseconds
            "serial_echo":0, #0 = enabled, 1 is disabled
        },
        "board-7":{
            "mcu_id":"",
            "serial_data_watchdog":0, #miliseconds
            "serial_echo":0, #0 = enabled, 1 is disabled
        },
    }
    MOTORS = {
        "C3":{
            "mcu_id":"300:1058:2031663:1429493506:540422710",
            "channel":"1",
            "z_index_pin":0,
            "motor_acceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "motor_deceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "operating_mode":0, #0: Open-loop,1: Closed-loop speed,2: Closed-loop position relative,3: Closed-loop count position,4: Closed-loop position tracking,5: Torque,6: Closed-loop speed position
            "pid_differential_gain":1, # 0-255
            "pid_integral_gain":1, # 0-255
            "pid_proportional_gain":1, # 0-255
            "encoder_ppr_value":4000,
        },
        "D3":{
            "mcu_id":"300:1058:2031663:1429493506:540422710",
            "channel":"2",
            "z_index_pin":0,
            "motor_acceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "motor_deceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "operating_mode":0, #0: Open-loop,1: Closed-loop speed,2: Closed-loop position relative,3: Closed-loop count position,4: Closed-loop position tracking,5: Torque,6: Closed-loop speed position
            "pid_differential_gain":1, # 0-255
            "pid_integral_gain":10, # 0-255
            "pid_proportional_gain":5, # 0-255
            "encoder_ppr_value":4000,
        },


        "C#3":{
            "mcu_id":"",
            "channel":"1",
            "z_index_pin":0,
            "motor_acceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "motor_deceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "operating_mode":1, #0: Open-loop,1: Closed-loop speed,2: Closed-loop position relative,3: Closed-loop count position,4: Closed-loop position tracking,5: Torque,6: Closed-loop speed position
            "pid_differential_gain":1, # 0-255
            "pid_integral_gain":1, # 0-255
            "pid_proportional_gain":1, # 0-255
            "encoder_ppr_value":4000,
        },
        "E3":{
            "mcu_id":"",
            "channel":"2",
            "z_index_pin":0,
            "motor_acceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "motor_deceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "operating_mode":1, #0: Open-loop,1: Closed-loop speed,2: Closed-loop position relative,3: Closed-loop count position,4: Closed-loop position tracking,5: Torque,6: Closed-loop speed position
            "pid_differential_gain":1, # 0-255
            "pid_integral_gain":10, # 0-255
            "pid_proportional_gain":5, # 0-255
            "encoder_ppr_value":4000,
        },


        "D#3":{
            "mcu_id":"",
            "channel":"1",
            "z_index_pin":0,
            "motor_acceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "motor_deceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "operating_mode":1, #0: Open-loop,1: Closed-loop speed,2: Closed-loop position relative,3: Closed-loop count position,4: Closed-loop position tracking,5: Torque,6: Closed-loop speed position
            "pid_differential_gain":1, # 0-255
            "pid_integral_gain":1, # 0-255
            "pid_proportional_gain":1, # 0-255
            "encoder_ppr_value":4000,
        },
        "F#3":{
            "mcu_id":"",
            "channel":"2",
            "z_index_pin":0,
            "motor_acceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "motor_deceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "operating_mode":1, #0: Open-loop,1: Closed-loop speed,2: Closed-loop position relative,3: Closed-loop count position,4: Closed-loop position tracking,5: Torque,6: Closed-loop speed position
            "pid_differential_gain":1, # 0-255
            "pid_integral_gain":10, # 0-255
            "pid_proportional_gain":5, # 0-255
            "encoder_ppr_value":4000,
        },

        "F3":{
            "mcu_id":"",
            "channel":"1",
            "z_index_pin":0,
            "motor_acceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "motor_deceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "operating_mode":1, #0: Open-loop,1: Closed-loop speed,2: Closed-loop position relative,3: Closed-loop count position,4: Closed-loop position tracking,5: Torque,6: Closed-loop speed position
            "pid_differential_gain":1, # 0-255
            "pid_integral_gain":1, # 0-255
            "pid_proportional_gain":1, # 0-255
            "encoder_ppr_value":4000,
        },
        "G#3":{
            "mcu_id":"",
            "channel":"2",
            "z_index_pin":0,
            "motor_acceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "motor_deceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "operating_mode":1, #0: Open-loop,1: Closed-loop speed,2: Closed-loop position relative,3: Closed-loop count position,4: Closed-loop position tracking,5: Torque,6: Closed-loop speed position
            "pid_differential_gain":1, # 0-255
            "pid_integral_gain":10, # 0-255
            "pid_proportional_gain":5, # 0-255
            "encoder_ppr_value":4000,
        },

        "G3":{
            "mcu_id":"",
            "channel":"1",
            "z_index_pin":0,
            "motor_acceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "motor_deceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "operating_mode":1, #0: Open-loop,1: Closed-loop speed,2: Closed-loop position relative,3: Closed-loop count position,4: Closed-loop position tracking,5: Torque,6: Closed-loop speed position
            "pid_differential_gain":1, # 0-255
            "pid_integral_gain":1, # 0-255
            "pid_proportional_gain":1, # 0-255
            "encoder_ppr_value":4000,
        },
        "A#3":{
            "mcu_id":"",
            "channel":"2",
            "z_index_pin":0,
            "motor_acceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "motor_deceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "operating_mode":1, #0: Open-loop,1: Closed-loop speed,2: Closed-loop position relative,3: Closed-loop count position,4: Closed-loop position tracking,5: Torque,6: Closed-loop speed position
            "pid_differential_gain":1, # 0-255
            "pid_integral_gain":10, # 0-255
            "pid_proportional_gain":5, # 0-255
            "encoder_ppr_value":4000,
        },

        "A3":{
            "mcu_id":"",
            "channel":"1",
            "z_index_pin":0,
            "motor_acceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "motor_deceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "operating_mode":1, #0: Open-loop,1: Closed-loop speed,2: Closed-loop position relative,3: Closed-loop count position,4: Closed-loop position tracking,5: Torque,6: Closed-loop speed position
            "pid_differential_gain":1, # 0-255
            "pid_integral_gain":1, # 0-255
            "pid_proportional_gain":1, # 0-255
            "encoder_ppr_value":4000,
        },
        "C4":{
            "mcu_id":"",
            "channel":"2",
            "z_index_pin":0,
            "motor_acceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "motor_deceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "operating_mode":1, #0: Open-loop,1: Closed-loop speed,2: Closed-loop position relative,3: Closed-loop count position,4: Closed-loop position tracking,5: Torque,6: Closed-loop speed position
            "pid_differential_gain":1, # 0-255
            "pid_integral_gain":10, # 0-255
            "pid_proportional_gain":5, # 0-255
            "encoder_ppr_value":4000,
        },

        "B3":{
            "mcu_id":"",
            "channel":"1",
            "z_index_pin":0,
            "motor_acceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "motor_deceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "operating_mode":1, #0: Open-loop,1: Closed-loop speed,2: Closed-loop position relative,3: Closed-loop count position,4: Closed-loop position tracking,5: Torque,6: Closed-loop speed position
            "pid_differential_gain":1, # 0-255
            "pid_integral_gain":1, # 0-255
            "pid_proportional_gain":1, # 0-255
            "encoder_ppr_value":4000,
        },
        "C#4":{
            "mcu_id":"",
            "channel":"2",
            "z_index_pin":0,
            "motor_acceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "motor_deceleration_rate":500, # Min:0, Max:500000, Default: 10000 = 1000.0 RPM/s
            "operating_mode":1, #0: Open-loop,1: Closed-loop speed,2: Closed-loop position relative,3: Closed-loop count position,4: Closed-loop position tracking,5: Torque,6: Closed-loop speed position
            "pid_differential_gain":1, # 0-255
            "pid_integral_gain":10, # 0-255
            "pid_proportional_gain":5, # 0-255
            "encoder_ppr_value":4000,
        },
    }

pitches_to_speeds = {
        "C3":{ #0
            "0":0,
            "C3":0,
            "C4":0,
            "G4":0,
            "C5":0,
            "E5":0,
            "G5":0
        },
        "D3":{ #2
            "0":0,
            "D3":0,
            "D4":0,
            "A4":0,
            "D5":0,
            "F#5":0,
            "A5":0,
        },

        "C#3":{ #1
        },
        "E3":{ #4
        },

        "D#3":{ #3
        },
        "F#3":{ #6
        },

        "F3":{ #5
        },
        "G#3":{ #8
        },

        "G3":{ #7
        },
        "A#3":{ #10
        },

        "A3":{ #9
        },
        "C4":{ #12
        },

        "B3":{ #11
        },
        "C#4":{ #13
        },
    }