import os
import time
from datetime import datetime

STATUS = {}

def ping(host):
    return os.system(f"ping -n 1 {host} > nul") == 0

def load_devices():
    with open("devices.txt") as f:
        return [x.strip() for x in f if x.strip()]

def check_devices():
    global STATUS
    devices = load_devices()

    results = []

    for device in devices:
        status = "UP" if ping(device) else "DOWN"

        changed = device in STATUS and STATUS[device] != status

        STATUS[device] = status

        results.append({
            "device": device,
            "status": status,
            "changed": changed
        })

    return results