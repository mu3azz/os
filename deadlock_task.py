import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread_a():
    print("Thread A: Trying to acquire Lock 1...")
    with lock1:
        print("Thread A: Acquired Lock 1")
        time.sleep(2) 
        
        print("Thread A: Waiting for Lock 2...")
    with lock2:
      print("Thread A: Acquired Lock 2")
      print("Thread A: Both locks acquired - critical section")

def thread_b():
    print("Thread B: Trying to acquire Lock 2...")
    with lock2:
        print("Thread B: Acquired Lock 2")
        time.sleep(2)  
        
        print("Thread B: Waiting for Lock 1...")
        with lock1:
            print("Thread B: Acquired Lock 1")
            print("Thread B: Both locks acquired - critical section")


thread1 = threading.Thread(target=thread_a, name="Thread-A")
thread2 = threading.Thread(target=thread_b, name="Thread-B")


thread1.start()
thread2.start()

