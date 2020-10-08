#!/usr/bin/env python3
import os
import platform
from datetime import datetime

print(f'Hello {os.getlogin()}')
print(f'You are using the computer {platform.node()}. It is {datetime.now()}')