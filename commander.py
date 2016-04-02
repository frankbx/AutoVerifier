#!/usr/bin/env python
# encoding: utf-8

import time
import serial


"""
    VK_F1,          KEY_ACTION_QUICKKEY_1,               
    VK_F2,          KEY_ACTION_QUICKKEY_2,               
    VK_F3,          KEY_ACTION_QUICKKEY_3,               
    VK_F4,          KEY_ACTION_QUICKKEY_4,               
    VK_F5,          KEY_ACTION_QUICKKEY_5,               
    VK_F6,          KEY_ACTION_QUICKKEY_6,               
    VK_F7,          KEY_ACTION_QUICKKEY_7,               
    VK_F8,          KEY_ACTION_QUICKKEY_8,               
    VK_F9,          KEY_ACTION_QUICKKEY_9,               
    VK_F10,         KEY_ACTION_QUICKKEY_10,              
    VK_F11,         KEY_ACTION_UTILS_WB_SPY,             
    VK_F12,         KEY_ACTION_UTILS_ALARM_SPY,          
    VK_SNAPSHOT,    KEY_ACTION_UTILS_SCREEN_CAPTURE,     
    VK_HOME,        KEY_ACTION_UTILS_LOG_VIEWER,         
    VK_RETURN,      KEY_ACTION_COMWHEEL_PRESS,           
    VK_DOWN,        KEY_ACTION_COMWHEEL_LEFT_TURN,       
    VK_LEFT,        KEY_ACTION_COMWHEEL_LEFT_TURN,       
    VK_RIGHT,       KEY_ACTION_COMWHEEL_RIGHT_TURN,      
    VK_UP,          KEY_ACTION_COMWHEEL_RIGHT_TURN,      
    "A",            KEY_ACTION_MENU_ALARM_SETUP,         
    "B",            KEY_ACTION_MENU_CIRCUIT,             
    "C",            KEY_ACTION_MENU_CHECKOUT,            
    "D",            KEY_ACTION_DUMP_TRENDS,              
    "E",            KEY_ACTION_MENU_START_END_CASE,      
    "F",            KEY_ACTION_MENU_SU_INST_SERVICE,     
    "G",            KEY_ACTION_MENU_GAS_SETUP,           
    "H",            KEY_ACTION_MENU_SERVICE_LOGS,        
    "I",            KEY_ACTION_MENU_AIR_ONLY,            
    "J",            KEY_ACTION_MENU_ALT_O2,              
    "K",            KEY_ACTION_MENU_SU_GAS_CONTROLS,     
    "L",            KEY_ACTION_LOAD_TRENDS,              
    "M",            KEY_ACTION_MENU_VENT_MORE_SETTINGS,  
    "N",            KEY_ACTION_NORMAL_SCREEN,            
    "O",            KEY_ACTION_TOUCHSCREEN_LOCK_TOGGLE,  
    "P",            KEY_ACTION_MENU_PROCEDURES,          
    "Q",            KEY_ACTION_START_STOP_TIMER,         
    "R",            KEY_ACTION_RESET_TIMER,              
    "S",            KEY_ACTION_ALARM_SILENCE,            
    "T",            KEY_ACTION_MENU_TRENDS,              
    "U",            KEY_ACTION_MENU_SCREEN_SETUP,        
    "V",            KEY_ACTION_MENU_VENT_MODE,           
    "W",            KEY_ACTION_MENU_SYSTEM_SETUP,        
    "X",            KEY_ACTION_MENU_SU_SYSTEM_CONFIG,    
    "Y",            KEY_ACTION_MENU_SPIROMETRY,          
    "Z",            KEY_ACTION_MENU_SU_CASEDEFAULTS,     
    "1",            KEY_ACTION_MENU_INSTALLATION,        
    "2",            KEY_ACTION_MENU_COPY_CONFIGURATION,  
    "3",            KEY_ACTION_MENU_SU_GAS_USAGE,        
    "4",            KEY_ACTION_MENU_SU_EXIT,             
    "5",            KEY_ACTION_MENU_TOTALFLOW_QUK_SEL,   
    "6",            KEY_ACTION_MENU_O2PERCENT_QUK_SEL,   
    "7",            KEY_ACTION_MENU_SERVICE_SW_HW_INFO,  
    "8",            KEY_ACTION_MENU_SERVICE_OPTIONS,     
    "9",            KEY_ACTION_QUICKKEY_11,              
    "0",            KEY_ACTION_MENU_AGENT_QUK_SEL,       
"""
ser = serial.Serial(
    port='COM1',
    # Baudrate for MC is 19200
    baudrate=19200,
    stopbits=serial.STOPBITS_ONE,
    parity=serial.PARITY_NONE,
    bytesize=serial.EIGHTBITS
)

print ser.isOpen()

print 'Enter your commands below.\r\nInsert "exit" to leave the application.'
# ser.write('\n')
# ser.write('\x61')
# ser.write(chr(0xa0))
# ser.write(chr(0xa1))
# print chr(0x61)
input = 1
while 1:
    # get keyboard input
    input = raw_input(">> ")
    # Python 3 users
    # input = input(">> ")
    if input == 'exit':
        ser.close()
        exit()
    else:
        # send the character to the device
        # (note that I append a \r\n carriage return and line feed to the characters - this is requested by my device)
        ser.write(input+'\na')
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1)

        if out != '':
            print ">>" + out
