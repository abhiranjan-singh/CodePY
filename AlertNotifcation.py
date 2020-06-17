import os
import socket
from _socket import SocketType
import socket
from typing import Union

Host = "mcacms.gov.in"
portx = 443
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host, int(portx)))
