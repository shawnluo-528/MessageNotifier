# MessageNotifier
Notify remote udp server with some information. On windows system, after install this package, it will create an auto-run service, when it receives message, it will pop-out a window and show the received message.

# Install
```python
python setup.py install
```

Remove auto-run service: 
```python
python setup.py remove
```

# Usage
Server: once it was installed, there is a service running on windows, or you can run the service by: python MessageNotifier.py

Client: 
```python
import MessageNotifier
SERVER_ADDR = 10.198.1.10
MessageNotifier.notify("hello", SERVER_ADDR)
```
