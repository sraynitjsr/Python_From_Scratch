import threading
import time

current_number = 1

lock = threading.Lock()

def print_even():
    global current_number
    while current_number <= 10:
        lock.acquire()
        if current_number % 2 == 0:
            print("Even thread:", current_number)
            current_number += 1
        lock.release()
        time.sleep(0.5)

def print_odd():
    global current_number
    while current_number <= 10:
        lock.acquire()
        if current_number % 2 != 0:
            print("Odd thread:", current_number)
            current_number += 1
        lock.release()
        time.sleep(0.5)

even_thread = threading.Thread(target=print_even)
odd_thread = threading.Thread(target=print_odd)

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()

print("Both threads have finished execution.")
