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
        # 1
        "C3":{ #0
            "0":[-10,-10,-10],
            "C3":[-26,-26,-26],
            "C4":[-46,-53,-60],
            "G4":[-68,-84,-99],
            "C5":[-105,-117,-130],
            "E5":[-145,-155,-165],
            "G5":[-26,-26,-26]
        },
        "D3":{ #2
            "0":[10,10,10],
            "D3":[20,20,20],
            "D4":[41,43,44],
            "A4":[65,69,73],
            "D5":[80,88,96],
            "F#5":[106,113,120],
            "A5":[132,135,137],
        },
        #2 
        "C#3":{ #1
            "0":[10,10,10],
            "C#3":[20,20,20],
            "C#4":[48,50,62],
            "G#4":[75,90,105],
            "C#5":[120,125,130],
        },
        "E3":{ #4
            "0":[-10,-10,-10],
            "E3":[-20,-20,-20],
            "E4":[-54,-56,-59],
            "B4":[-75,-86,-92],
            "E5":[-103,-111,-120],
            "G5":[-142,-147,-152],
        },
        #3
        "D#3":{ #3
            "0":[-10,-10,-10],
            "D#3":[-20,-20,-21],
            "D#4":[-47,-50,-54],
            "A#4":[-67,-75,-84],
            "D#5":[-94,-106,-114],
            "F#5":[-125,-132,-140],
        },
        "F#3":{ #6
            "0":[10,10,10],
            "F#3":[20,20,20],
            "F#4":[65,77,80],
            "C#5":[99,113,127],
            "F#5":[140,156,172],
        },
        #4
        "F3":{ #5
            "0":[-10,-10,-10],
            "F3":[-20,-20,-20],
            "F4":[-57,-60,-68],
            "C5":[-85,-95,-108],
            "F5":[-120,-128,-136],
        },
        "G#3":{ #8
            "0":[10,10,10],
            "G#3":[20,20,20],
            "G#4":[52,60,64],
            "E#5":[82,94,100],
            "G#5":[115,122,130],
            "B5":[148,153,158],
        },
        #5
        "G3":{ #7
            "0":[-10,-10,-10],
            "G3":[-20,-20,-20],
            "G4":[-50,-54,-57],
            "D5":[-73,-92,-93],
            "G5":[-100,-112,-125],
        },
        "A#3":{ #10
            "0":[10,10,10],
            "A#3":[33,33,33],
            "A#4":[64,72,80],
            "F5":[94,113,132],
            "A#5":[147,163,171],
        },
        #6
        "A3":{ #9
            "0":[-10,-10,-10],
            "A3":[-30,-30,-30],
            "A4":[-60,-69,-75],
            "E5":[-90,-103,-115],
            "A5":[-128,-142,-159],
        },
        "C4":{ #12
            "0":[10,10,10],
            "C4":[58,60,62],
            "C5":[102,110,128],
            "G5":[102,110,128],
            "C6":[102,110,128],
        },
        #7
        "B4":{ #11
            "0":[-10,-10,-10],
            "B4":[-30,-30,-30],
            "B5":[-30,-30,-30],
            "F#4":[-30,-30,-30],
            "B6":[-30,-30,-30],
        },
        "C#4":{ #13
            "0":[10,10,10],
            "C#4":[20,20,20],
            "C#5":[48,50,62],
            "G#5":[75,90,105],
            "C#6":[120,125,130],
        },
    }