# main.py
from document_monitor import DocumentMonitor
import user_interface

if __name__ == "__main__":
    folder_path = "path_to_monitored_folder"
    monitor = DocumentMonitor(folder_path)
    user_interface.run(monitor)
