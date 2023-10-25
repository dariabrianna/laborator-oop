def run(monitor, file_name):
    while True:
        action = input("Enter action (commit, info <filename>, status, or exit): ")
        if action.startswith("info "):
            filename = action[5:]
            monitor.show_file_info(filename)
        elif action == "status":
            monitor.scan_folder()
            monitor.check_status()
        elif action == "exit":
            break
        else:
            print("Invalid action. Please try again.")
