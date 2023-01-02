
#https://python-socketio.readthedocs.io/en/latest/client.html

# pip install python-socketio
# pip install websocket-client
import socketio  

# 
sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")

# Register method
@sio.event
def chatMessage(data):
    print('chatMessage Called')
    #print("Socket ID: " , sid)
    print(data)

#@sio.on('chatMessage')
#async def on_message(data):
#      print('I received a message!')

## If we wanted to create a new websocket endpoint,
## use this decorator, passing in the name of the
## event we wish to listen out for
#@sio.on('chatMessage')
#def print_message(sid, message):
    ## When we receive a new event of type
    ## 'message' through a socket.io connection
    ## we print the socket ID and the message
#    print('chatMessage Called')
#    print("Socket ID: " , sid)
    #print(message)



#await sio.connect('http://localhost:3000')
sio.connect('http://localhost:3000')

