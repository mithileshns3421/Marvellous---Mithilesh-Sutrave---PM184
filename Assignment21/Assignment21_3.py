from threading import Thread, Lock

# Shared variable
counter = 0

# Create a lock
lock = Lock()

# Function executed by each thread
def update_counter():
    global counter

    for i in range(100000):
        lock.acquire()      # Acquire the lock
        counter += 1        # Update shared variable
        lock.release()      # Release the lock

# Create threads
t1 = Thread(target=update_counter)
t2 = Thread(target=update_counter)
t3 = Thread(target=update_counter)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for all threads to finish
t1.join()
t2.join()
t3.join()

# Display final value
print("Final Counter Value:", counter)