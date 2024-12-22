import os
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

log_dir = '/home/kali/bsm/logs'
log_file = os.path.join(log_dir, 'changes.json')


if not os.path.exists(log_dir):
    os.makedirs(log_dir)


if not os.path.exists(log_file):
    try:
        with open(log_file, 'w') as f:
            json.dump([], f)
    except IOError as e:
        print(f"Error creating log file: {e}")

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"File modified: {event.src_path}")  
        self.log_change(event)

    def on_created(self, event):
        if event.is_directory:
            return
        print(f"File created: {event.src_path}")  
        self.log_change(event)

    def on_deleted(self, event):
        if event.is_directory:
            return
        print(f"File deleted: {event.src_path}")  
        self.log_change(event)

    def log_change(self, event):
        # Değişiklik bilgileri
        event_info = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'event_type': event.event_type,  # 'modified', 'created', or 'deleted'
            'file_path': event.src_path
        }

        try:
           
            with open(log_file, 'r+') as f:
                logs = json.load(f)
                logs.append(event_info)
                f.seek(0)  
                json.dump(logs, f, indent=4)
        except IOError as e:
            print(f"Error accessing log file: {e}")

if __name__ == "__main__":

    path_to_watch = "/home/kali/bsm/test"
    

    if not os.path.exists(path_to_watch):
        print(f"Directory {path_to_watch} does not exist.")
    else:
        event_handler = ChangeHandler()
        observer = Observer()
        observer.schedule(event_handler, path=path_to_watch, recursive=False)
        observer.start()

        print(f"Watching changes in {path_to_watch}...")

        try:
            observer.join()  
        except KeyboardInterrupt:
            observer.stop()
            observer.join()
