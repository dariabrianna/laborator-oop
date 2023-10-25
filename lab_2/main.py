# main.py
import os
import threading
import time
from document_monitor import DocumentMonitor
import user_interface

def schedule_detection(monitor):
    while True:
        monitor.scan_folder()
        monitor.check_status()
        time.sleep(5)  # Schedule detection every 5 seconds

if __name__ == "__main__":
    folder_path = "my_local_folder"
    monitor = DocumentMonitor(folder_path)

    # Create a thread for scheduled detection
    detection_thread = threading.Thread(target=schedule_detection, args=(monitor,))
    detection_thread.daemon = True  # Set the thread as a daemon, so it doesn't block program exit

    # Start the detection thread
    detection_thread.start()

    # Run user interface in the main thread
    user_interface.run(monitor)
