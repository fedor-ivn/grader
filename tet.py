import subprocess
import os
import termios

# execute the "read" command and capture its output

master, slave = os.openpty()
old = termios.tcgetattr(slave)
old[3] &= ~termios.ECHO
termios.tcsetattr(slave, termios.TCSADRAIN, old)

process = subprocess.Popen(
    "read -p test d; echo $d",
    shell=True,
    stdin=slave,
    stderr=slave,
    stdout=slave,
    text=True,
)

os.write(master, b"abcabc\n")
print(os.read(master, 100))
print(os.read(master, 100))


# with open(master, "r") as file:
# print(file.read())
