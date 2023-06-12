import subprocess
import asyncio
import sys
import os

class InteractiveSession:
    def __init__(self, path, args=[]):
        self.child = subprocess.Popen(['bash', path, *args], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.stdout = self.child.stdout
        self.stderr = self.child.stderr
    