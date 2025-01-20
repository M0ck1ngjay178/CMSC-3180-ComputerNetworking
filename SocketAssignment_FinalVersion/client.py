#===============CMSC-3180-SOCKET ASSIGNMENT=======================#
# -Group 1 Members: Margo Bonal, Anthony Beitko                   #
# -Due: Thursday 10/24                                            #
#=================================================================#

#=========LIBRARIES==========#
import socket
import random
#============================#
#++++++++++SCOURCE+++++++++++++#
# Socket Programming In Python(Guide):
# https://realpython.com/python-sockets/
#++++++++++++++++++++++++++++++#
#=========================CLASS: CLIENT===============================================#
class Client:

    def __init__(self):
        self.received_data = False
        self.ipAddr = '158.83.11.22'
        self.valid = True
        self.echo = True

    # -----------------PRINT HEADER----------------------------#
    def printHeader(self):
        print('\n--------------CLIENT----------------------\n')
    # -----------------END PRINT HEADER-----------------------#

    # -----------------PRINT CLOSE----------------------------#
    def printClose(self):
        print('\n------------------------------------------\n')
    # -----------------END PRINT CLOSE-----------------------#

    # ----------------RANDOM_MSG----------------------------#
    def random_msg(self):
        messages =["Margo", "Anthony", "Dr. Chen", "Comp Networking"]
        return random.choice(messages)
    # ----------------END RANDOM_MSG------------------------#


    # -----------------connectClient: HANDLE SOCKET CONNECTION-----------------------#
    def connectClient(self, event=None):
        self.printHeader()

        while self.valid:
            # Ask user for port number input
            port_value = input("Enter the Port Number: ")
            self.valid = False
            try:
                port_value = int(port_value)  # Convert port to an integer

                if port_value < 0:
                    print("INVALID! Cannot be negative, Re-enter:\n")
                    self.valid = True
                else:
                    self.valid = False

            except ValueError:
                print("***INVALID Port Number! Please re-enter a Valid Integer***\n")
                self.valid = True
            
        self.server_address = (self.ipAddr, port_value)
        print(f"Attempting to connect to {self.server_address}...")
        self.printClose()

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(self.server_address)
                print(f"Connected to {self.server_address}.\n")

                # Receive initial data from server
                self.data = sock.recv(1024)
                print("Server: ", self.data.decode(), "\n")

                while True:

                    while True: #validity checks for input
                        user_option = input("Enter: (QUIT, ECHO_ON msg, ECHO_OFF msg, HELP, RANDOM) ")
                        # Validate command
                        if user_option.strip().upper() == 'QUIT':
                            break
                        elif user_option.upper().startswith("ECHO_ON"):
                            break
                        elif user_option.upper().startswith("ECHO_OFF"):
                            break
                        elif user_option.upper().startswith("HELP"):
                            break
                        elif user_option.upper().startswith("RANDOM"):
                            break
                        else:
                            print("**INVALID COMMAND! Please enter a valid option.**\n")
                            continue  # Reprompt

                    # QUIT protocol
                    if user_option.strip().upper() == 'QUIT':
                        sock.sendall(user_option.encode())
                        print("Closing connection...")
                        break

                    #HELP Display
                    if user_option.strip().upper() == 'HELP':
                        self.printClose()
                        print("OPTIONS:\n"
                            "1. QUIT: Close Connection.\n"
                            "2. ECHO_ON <msg>:  Enable echo mode and send message.\n"
                            "3. ECHO_OFF <msg>: Disable echo mode and send message.\n"
                            "4. HELP: Display each command and information.\n"
                            "5. RANDOM: Send a random message to server.           ")
                        
                        self.printClose()

                    #RANDOM message
                    if user_option.strip().upper() == 'RANDOM':
                        r_msg = self.random_msg()
                        sock.sendall(r_msg.encode())
                        print("\n---------------------")
                        print(f"Client RANDOM: {r_msg}")
                        print("---------------------\n")
                        sock.recv(1024).decode()  # Clear out server's response


                    # Echo mode ON
                    elif user_option.upper().startswith("ECHO_ON"):
                        self.echo = True
                        print("\nECHO Mode ON")
                        print("---------------------")
                        if len(user_option.split()) > 1:  # Check if a message is provided after ECHO_ON
                            message = user_option.split(" ", 1)[1]
                            print(f"Client: {message}")
                            sock.sendall(message.encode())  # Send the message part only
                            server_response = sock.recv(1024).decode()
                            print(f"Server: {server_response}\n")
                        print("---------------------\n")

                    # Echo mode OFF
                    elif user_option.upper().startswith("ECHO_OFF"):
                        self.echo = False
                        print("\nECHO Mode OFF")
                        print("---------------------")
                        if len(user_option.split()) > 1:  # Check if a message is provided after ECHO_OFF
                            message = user_option.split(" ", 1)[1]
                            print(f"Client: {message}\n")
                            sock.sendall(message.encode())  # Send the message part only
                            sock.recv(1024).decode()  # Clear out server's response
                        print("---------------------\n")
                    else:
                        # Send data to server
                        print(f"Client: {user_option}")
                        sock.sendall(user_option.encode())

                        # Receive response from the server
                        server_response = sock.recv(1024).decode()

                        # Handle echo mode
                        if self.echo:
                            print(f"Server: {server_response}")
                        else:
                            print("Message sent to server, no echo.")

        except ConnectionRefusedError:
            print(f"Failed to connect to server at {self.server_address}. Please check the server and try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # -----------------END connectClient: HANDLE SOCKET CONNECTION-----------------------#
    
# ===========================MAIN======================================#
if __name__ == "__main__":
    client = Client()  # Initialize client
    client.connectClient()  # Start the connection process
# =====================================================================#
