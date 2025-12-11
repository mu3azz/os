import threading
import time

room = threading.Semaphore(1)

def print_1(num):
    """Function representing a person entering/leaving a room"""
    print(f"Person {num} is waiting to enter the room")
    
    room.acquire() 
    print(f"Person {num} entered the room")
    
    time.sleep(2) 
    
    print(f"Person {num} left the room")
    room.release() 

people = []
for i in range(5):
    t = threading.Thread(target=print_1, args=(i,))
    people.append(t)
    t.start()
