import threading
import time

def print_numbers():
    for i in range(1, 6):
        print("Thread 1:", i)
        time.sleep(1)

def print_letters():
    for letter in 'abcde':
        print("Thread 2:", letter)
        time.sleep(1)

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("Both threads have finished execution.")
