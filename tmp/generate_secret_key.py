import base64
import os

b = os.urandom(16)
s = base64.b64encode(b).decode("utf-8")
print(s)
