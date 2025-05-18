import socket

# Tello's IP and command port
TELLO_IP = "192.168.10.1"
TELLO_PORT = 8889

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind explicitly to the local Wi-Fi interface IP
# You MUST replace this IP with your Mac's IP on the Tello network
sock.bind(("192.168.10.2", 9000))  # 9000 is arbitrary local port

# Send 'command' to Tello
sock.sendto(b"command", (TELLO_IP, TELLO_PORT))
print("Command sent!")