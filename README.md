# BsmAltyap
My code is a Python script that monitors a directory in a Linux system for any changes—like when files are created, modified, or deleted. It uses a watch directory library (such as watchdog ) to track these changes in real-time and automatically generates log files to keep a record of all activities. This makes it useful for auditing, debugging, or just keeping track of file system changes.

Additionally, the script is designed to run as a system operation, meaning it can work in the background as a service or daemon, ensuring continuous monitoring without manual intervention. The logs provide details like timestamps, event types, and affected file paths, making it easy to review what happened and when.
