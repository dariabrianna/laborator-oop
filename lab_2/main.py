import sys
from document_monitor import DocumentMonitor
import user_interface

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_name>")
    else:
        file_name = sys.argv[1]
        monitor = DocumentMonitor("my_local_folder")  # Folder path is constant
        user_interface.run(monitor, file_name)
