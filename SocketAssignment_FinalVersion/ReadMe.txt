#===============CMSC-3180-SOCKET ASSIGNMENT=======================#
# -Group 1 Members: Margo Bonal, Anthony Beitko                   #
# -Due: Thursday 10/24                                            #
#=================================================================#

**This document serves as an structural breakdown of the Client program.
--Defined Purpose: This program serves the purpose as a client structure to function in correspondence to provided server program.
-- Language Used: Python
-- Libraries: Socket, Random
-- 2 BONUS FEATURES: HELP & RANDOM
#=========================CLASS: CLIENT===============================================#
---------------------------------------------------
def __init__(self):
-function to initialize all program variables and data
-accepts one positional argument
---------------------------------------------------

---------------------------------------------------
def printHeader(self):
-function to print top readability header
-accepts one positional argument
---------------------------------------------------

---------------------------------------------------
def printClose(self):
-function to print bottom readability header
-accepts one positional argument
---------------------------------------------------

---------------------------------------------------
def random_msg(self):
-function to send random message to server
-accepts one positional argument
---------------------------------------------------

---------------------------------------------------
def connectClient(self, event=None):
-function to handle socket connection with server
-validity checks to insure proper input
-connection error handling
-accepts two position arguments
-echo mode handling
-Help display
-Send Random Message
---------------------------------------------------
#=========================CLASS: CLIENT===============================================#