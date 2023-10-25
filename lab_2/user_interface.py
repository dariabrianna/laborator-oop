# user_interface.py

def run(monitor):
    while True:
        action = input("Enter action (commit, info <filename>, status, or exit): ")
        if action == "commit":
            monitor.create_snapshot()
        elif action.startswith("info"):
            _, filename = action.split(maxsplit=1)
            monitor.show_file_info(filename)
        elif action == "status":
            monitor.scan_folder()
            monitor.check_status()
        elif action == "exit":
            break
        else:
            print("Invalid action. Please try again.")
