import os
import hashlib
import time
from datetime import datetime
from image_processing import get_image_size
from text_processing import get_text_stats

class DocumentMonitor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.snapshot_time = None
        self.file_info = {}

    def create_snapshot(self):
        self.snapshot_time = datetime.now()
        self.file_info = {}
        print(f"Snapshot updated at {self.snapshot_time}")

    def scan_folder(self):
        files = os.listdir(self.folder_path)
        for file in files:
            file_path = os.path.join(self.folder_path, file)
            if os.path.isfile(file_path):
                self.update_file_info(file_path)

    def update_file_info(self, file_path):
        file_info = {}
        file_info["name"] = os.path.basename(file_path)
        file_info["extension"] = os.path.splitext(file_path)[1]
        file_info["created_time"] = datetime.fromtimestamp(os.path.getctime(file_path))
        file_info["modified_time"] = datetime.fromtimestamp(os.path.getmtime(file_path))

        if file_info["extension"] in {".png", ".jpg"}:
            file_info["image_size"] = get_image_size(file_path)
        elif file_info["extension"] == ".txt":
            file_info["line_count"], file_info["word_count"], file_info["char_count"] = get_text_stats(file_path)

        self.file_info[file_info["name"]] = file_info

    def show_file_info(self, filename):
        if filename in self.file_info:
            file_info = self.file_info[filename]
            print("File Name:", file_info["name"])
            print("Extension:", file_info["extension"])
            print("Created Time:", file_info["created_time"])
            print("Modified Time:", file_info["modified_time"])
            if "image_size" in file_info:
                print("Image Size:", file_info["image_size"])
            elif "line_count" in file_info:
                print("Line Count:", file_info["line_count"])
                print("Word Count:", file_info["word_count"])
                print("Character Count:", file_info["char_count"])
        else:
            print(f"File '{filename}' not found in the monitored folder.")

    def check_status(self):
        if self.snapshot_time:
            print(f"Snapshot taken at {self.snapshot_time}")
            for filename, file_info in self.file_info.items():
                if os.path.exists(os.path.join(self.folder_path, filename)):
                    if file_info["modified_time"] > self.snapshot_time:
                        print(f"{filename} - Changed")
                    else:
                        print(f"{filename} - No change")
                else:
                    print(f"{filename} - File deleted")
