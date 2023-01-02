import asyncio
import socketio
import random

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')

@sio.event
async def chatMessage(data):
    print('chatMessage received with ', data)
    #await sio.emit('my response', {'response': 'my response'})
#-----------------------------------------------------------------------
@sio.event
async def disconnect():
    print('disconnected from server')

#----------------------------------------------------------------------------------
#async def send_message(message):
    

#---------------------------------------------------------------------------------------
async def main():

    await sio.connect('http://localhost:3000')

    things_to_say = ['How are you', 'im hungry', 'better call sal']

    #await sio.wait()
    while True:
        #user_input = input("Type something  ")
        random_stuff = things_to_say[random.randint(0, 2)]
        say_this = f"say_{random_stuff}"
        await sio.emit('chatMessage', say_this)
        await sio.sleep(random.randint(1, 3))

        

#---------------------------------------------------------------------------------------
if __name__ == '__main__':

    asyncio.run(main())
    
