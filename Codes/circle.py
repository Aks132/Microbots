# Import the necessary modules
import socket
import threading
import time

# Create a UDP connection that we'll send the command to
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock1.setsockopt(socket.SOL_SOCKET, 25, 'wlp0s20f3'.encode())

sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.setsockopt(socket.SOL_SOCKET, 25, 'wlxd03745f1e17a'.encode())

sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock3.setsockopt(socket.SOL_SOCKET, 25, 'wlxd03745f5c27f'.encode())

sock4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock4.setsockopt(socket.SOL_SOCKET, 25, 'wlxd03745f25ac5'.encode())
# Send the message to Tello and allow for a delay in seconds
def send(message, delay):
  # Try to send the message otherwise print the exception
  try:
    sock1.sendto(message.encode(), ('192.168.10.1', 8889))
    sock2.sendto(message.encode(), ('192.168.10.1', 8889))
    sock3.sendto(message.encode(), ('192.168.10.1', 8889))
    sock4.sendto(message.encode(), ('192.168.10.1', 8889))
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))

  # Delay for a user-defined period of time
  time.sleep(delay)

# Receive the message from Tello
def receive():
  # Continuously loop and listen for incoming messages
  while True:
    # Try to receive the message otherwise print the exception
    try:
      response1, ip_address = sock1.recvfrom(128)
      response2, ip_address = sock2.recvfrom(128)
      response3, ip_address = sock3.recvfrom(128)
      response4, ip_address = sock4.recvfrom(128)
      print("Received message: from drone #1: " + response1.decode(encoding='utf-8'))
      print("Received message: from drone #2: " + response2.decode(encoding='utf-8'))
      print("Received message: from drone #3: " + response3.decode(encoding='utf-8'))
      print("Received message: from drone #4: " + response4.decode(encoding='utf-8'))
    except Exception as e:
      # If there's an error close the socket and break out of the loop
      sock1.close()
      sock2.close()
      sock3.close()
      sock4.close()
      print("Error receiving: " + str(e))
      break

# Create and start a listening thread that runs in the background
# This utilizes our receive functions and will continuously monitor for incoming messages
receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()

# Each leg of the box will be 100 cm. Tello uses cm units by default.
box_leg_distance = 230

# Yaw 90 degrees
yaw_angle = 90

# Yaw clockwise (right)
yaw_direction = "cw"

# Put Tello into command mode
send("command", 3)

# Send the takeoff command
send("takeoff", 8 )

sock1.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock2.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock3.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock4.sendto('command'.encode(), 0, ('192.168.10.1', 8889))

sock1.sendto('right 100'.encode(), 0, ('192.168.10.1', 8889))
sock2.sendto('cw 0'.encode(), 0, ('192.168.10.1', 8889))
sock3.sendto('right 100'.encode(), 0, ('192.168.10.1', 8889))
sock4.sendto('right 200'.encode(), 0, ('192.168.10.1', 8889))

time.sleep(6)

sock1.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock2.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock3.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock4.sendto('command'.encode(), 0, ('192.168.10.1', 8889))

sock1.sendto('cw 0'.encode(), 0, ('192.168.10.1', 8889))
sock2.sendto('cw 0'.encode(), 0, ('192.168.10.1', 8889))
sock3.sendto('cw 0'.encode(), 0, ('192.168.10.1', 8889))
sock4.sendto('forward 210'.encode(), 0, ('192.168.10.1', 8889))

time.sleep(6)

sock1.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock2.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock3.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock4.sendto('command'.encode(), 0, ('192.168.10.1', 8889))

sock1.sendto('cw 180'.encode(), 0, ('192.168.10.1', 8889))
sock2.sendto('cw 90'.encode(), 0, ('192.168.10.1', 8889))
sock3.sendto('cw 0'.encode(), 0, ('192.168.10.1', 8889))
sock4.sendto('ccw 90'.encode(), 0, ('192.168.10.1', 8889))

time.sleep(6)

sock1.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock2.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock3.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock4.sendto('command'.encode(), 0, ('192.168.10.1', 8889))

sock1.sendto('curve 100 100 0 200 0 0 50'.encode(), 0, ('192.168.10.1', 8889))
sock2.sendto('curve 100 100 0 200 0 0 50'.encode(), 0, ('192.168.10.1', 8889))
sock3.sendto('curve 100 100 0 200 0 0 50'.encode(), 0, ('192.168.10.1', 8889))
sock4.sendto('curve 100 100 0 200 0 0 50'.encode(), 0, ('192.168.10.1', 8889))

time.sleep(15)

sock1.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock2.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock3.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock4.sendto('command'.encode(), 0, ('192.168.10.1', 8889))

sock1.sendto('right 100'.encode(), 0, ('192.168.10.1', 8889))
sock2.sendto('back 200'.encode(), 0, ('192.168.10.1', 8889))
sock3.sendto('left 100'.encode(), 0, ('192.168.10.1', 8889))
sock4.sendto('left 200'.encode(), 0, ('192.168.10.1', 8889))

time.sleep(6)

sock1.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock2.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock3.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock4.sendto('command'.encode(), 0, ('192.168.10.1', 8889))

sock1.sendto('cw 180'.encode(), 0, ('192.168.10.1', 8889))
sock2.sendto('ccw 90'.encode(), 0, ('192.168.10.1', 8889))
sock3.sendto('cw 0'.encode(), 0, ('192.168.10.1', 8889))
sock4.sendto('cw 90'.encode(), 0, ('192.168.10.1', 8889))

time.sleep(6)

sock1.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock2.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock3.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
sock4.sendto('command'.encode(), 0, ('192.168.10.1', 8889))

sock1.sendto('cw 0'.encode(), 0, ('192.168.10.1', 8889))
sock2.sendto('ccw 0'.encode(), 0, ('192.168.10.1', 8889))
sock3.sendto('left 15'.encode(), 0, ('192.168.10.1', 8889))
sock4.sendto('right 20'.encode(), 0, ('192.168.10.1', 8889))

time.sleep(6)

#land
send("land", 5)

# Print message
print("Mission completed successfully!")

# Close the socket
sock1.close()
sock2.close()
sock3.close()
sock4.close()