#!/bin/python3

import os
import time

user = input("what's ur UNIX username? ")
pico = '/media/'+user+'/RPI-RP2'
pico2 = '/media/'+user+'/CIRCUITPY'


os.system("git clone https://github.com/dbisu/pico-ducky.git")
os.system("wget https://downloads.circuitpython.org/bin/raspberry_pi_pico/en_US/adafruit-circuitpython-raspberry_pi_pico-en_US-9.0.5.uf2")
os.system("wget https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20240625/adafruit-circuitpython-bundle-8.x-mpy-20240625.zip")
os.system("sudo apt install unzip -y")
os.system("sudo unzip adafruit-circuitpython-bundle-8.x-mpy-20240625.zip")

clone = 'pico-ducky'
curcuit = 'adafruit-circuitpython-raspberry_pi_pico-en_US-9.0.5.uf2'
adafruit = 'adafruit-circuitpython-bundle-8.x-mpy-20240625'

os.system("sudo cp adafruit-circuitpython-raspberry_pi_pico-en_US-9.0.5.uf2 "+pico)
print("please wait until the pico reboots then mount the CIRCUITPY...")
print("| DONT UNPLUG THE DEVICE |")
ans = input("when mounted, type 'y' then ENTER >> ")

time.sleep(10)
os.system("sudo cp "+adafruit+"/lib/adafruit_hid "+pico2+"/lib")
os.system("sudo cp "+adafruit+"/lib/adafruit_debouncer.mpy "+pico2+"/lib")
os.system("sudo cp "+adafruit+"/lib/adafruit_ticks.mpy "+pico2+"/lib")
os.system("sudo cp "+adafruit+"/lib/asyncio "+pico2+"lib")
os.system("sudo cp "+adafruit+"/lib/adafruit_wsgi "+pico2+"/lib")
os.system("sudo cp "+clone+"/boot.py "+pico2+"/")
os.system("sudo cp "+clone+"/duckyinpython.py "+pico2+"/")
os.system("sudo cp "+clone+"/code.py "+pico2+"/")
os.system("sudo cp "+clone+"/webapp.py "+pico2+"/")
os.system("sudo cp "+clone+"/wsgiserver.py "+pico2+"/")
time.sleep(3)
print("""
   #####################################
  #this is how it should look after   #
 ##################################### 
#                                    #
#       lib                          #
#               adafruit_hid         #
#               adafruit_wsgi        #
#               asyncio              #
#               adafruit_debouncer.py#
#               adafruit_ticks.py    #
#                                    #
#       system volume information    #
#               IndexerVolumeGuid    #
#               WPSSettings.dat      #
#                                    #
#       boot.py                      #
#       boot_out.txt                 #
#       payload.dd                   #
#       code.py                      #
#       duckyinpython.py             #
#       webapp.py                    #
#       wsginserver.py               #
#                                    #
# ####################################
# # Edit Payload.dd for what u want # 
#################################### 
""")

Print("Made by 96057")
print("Done.")
