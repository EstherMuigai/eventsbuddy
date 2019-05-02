# get_info.py

# Helper functions to get additional information required by the application
import socket, random, string

def get_device_id():
    device_id  = socket.gethostbyname(socket.getfqdn())
    return device_id


def generate_events_id():
    random_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    return random_id