#import bluetooth as bt
#import sh
import time
import pexpect
from sh import bluetoothctl
import subprocess
mac = "C8:84:47:26:E6:3C"
#sh.bluetoothctl("pair", mac)
print ("stuck here")
#bluetoothctl("connect", mac)
def connect():
    child = pexpect.spawn('bluetoothctl')
    child.sendline('power on')
    child.sendline('agent on')
    child.sendline('default-agent')
    child.sendline('pair C8:84:47:26:E6:3C')
    time.sleep(1)
    child.sendline('trust C8:84:47:26:E6:3C')
    time.sleep(1)
    child.sendline('connect C8:84:47:26:E6:3C')
    print("connecting...")
    time.sleep(5)
    subprocess.call("pulseaudio --start",shell=True)
    subprocess.call("pacmd set-default-sink bluez_sink.C8_84_47_26_E6_3C",shell=True)
    subprocess.call("aplay Glados.wav", shell=True)

connect()

