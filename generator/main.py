import time
import redis
import random
import lockfile

DELAY = 5
RANGE = (1000, 9999)

def main():
    r = redis.from_url('redis://localhost')
    while True:
        r.set('number', random.randrange(*RANGE))
        time.sleep(DELAY)

if __name__ == '__main__':
    lock = lockfile.LockFile(__file__)
    
    if not lock.is_locked():
        with lock:
            main()