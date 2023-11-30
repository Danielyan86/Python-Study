import os

# Create a pipe using os.pipe() method
# It will return a pair of
# file descriptors (r, w) usable for
# reading and writing, respectively.
r, w = os.pipe()

# Check if file descriptor r
# is open and connected
# to a tty(-like) device
# using os.isatty() method
print("Connected to a terminal:", os.isatty(r))

# Open a new pseudo-terminal pair
# using os.openpty() method
# It will return master and slave
# file descriptor for
# pty ( pseudo terminal device) and
# tty ( native terminal device) respectively
master, slave = os.openpty()

# Check if file descriptor master
# is open and connected
# to a tty(-like) device
# using os.isatty() method
print("Connected to a terminal:", os.isatty(master))
