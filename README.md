# MessageNotifier
Notify remote udp server with some information, and on the server, it will pop-out a window with received message.

# Install
Install: python setup.py install
On windows system, it will create an auto-run service which once it received message from remove, it will pop-out a window with received message.

Remove auto-run service: python setup.py remove

# Usage
Server: once it was installed, there is a service running on windows, or you can run the service by: python MessageNotifier.py

Client: 
import MessageNotifier
SERVER_ADDR = 10.198.1.10
MessageNotifier.notify("hello", SERVER_ADDR)
