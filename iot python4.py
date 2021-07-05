import ibmiotf.application
import ibmiotf.device
import random
import json
import time

#Provide your IBM Watson Device Credentials
organization = "q41r9v"
deviceType = "iotdevice"
deviceId = "9381"
authMethod = "token"
authToken = "9381362443"


# Initialize the device client.
def myCommandCallback(cmd):
    print("light on")
    print("Command received: %s" % cmd.data['command'])
try:
 deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
 deviceCli = ibmiotf.device.Client(deviceOptions)
#..............................................

except Exception as e:
 print("Caught exception connecting device: %s" % str(e))
 sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        time.sleep(1)
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
