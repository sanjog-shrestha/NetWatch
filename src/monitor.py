import time
import logging 
from ping3 import ping
from datetime import datetime

#Setup Logging
logging.basicConfig(
    filename='/logs/netwatch.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

TARGETS = ['8.8.8.8', '1.1.1.1']
INTERVAL = 30 #seconds

def monitor ():
    while True:
        for target in TARGETS:
            try:
                rtt = ping(target, timeout=2)
                if rtt is None:
                    status = "LOSS"
                    rtt_val = 0
                else:
                    status = "OK"
                    rtt_val = round(rtt * 1000, 2) #ms
                    
                log_msg = f"{target} | {status} | {rtt_val}ms"
                print(log_msg)
                logging.info(log_msg)
            except Exception as e:
                logging.error(f"{target} | ERROR | {str(e)}")
        time.sleep(INTERVAL)

if __name__ == '__main__':
    monitor()