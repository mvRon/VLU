def bt16():
    import socket
    return socket.gethostname()    

print(f"Hostname: {bt16}")

def bt17():
    import os
    return os.environ["Username"]
    
# print(f"OS name: {bt17()}")