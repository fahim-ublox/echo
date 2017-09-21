from time import sleep
import sys
import os
import socket 
import select
import re
from socket import SOL_SOCKET, SO_REUSEADDR


host = 'ciot.it-sgn.u-blox.com' 
port = 5050
backlog = 1 
size = 1500
max_data_Size=size
StopTestCaseOnFailure=True

prompt = "UDP ECHO Server:"

'''UDP echo server '''    
class UDP_Server():
    '''UDP_Server: initialization'''
    def __init__(self, timeout):
        print prompt+'Starting UDP server'
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind((host,port))
        '''Blocking sockets'''
        self.s.settimeout(timeout) 

    ''' Accept connection and echo back the data'''
    def Start_Server(self):
        print prompt+'Accepting UDP Connection'
        while 1:
            try:                
                print prompt +" Waiting to receive UDP data "
                data,address = self.s.recvfrom(size)
                print data
                if data:
                    print prompt +" Received the data from the client "
                    print address
                    print prompt+data
                    self.s.sendto(data,(address[0],address[1]))
                else:
                    print prompt +" Invalid data received "
            except Exception as ex:
                print(prompt + 'caught exception {}'.format(type(ex).__name__))
                print prompt +"Exception occured while receiving/transfering data"
                break
                
    def __del__(self):
        print prompt +"UDP_Server __del__ called"
        try:
            self.s.shutdown(socket.SHUT_RDWR)
            print prompt +"UDP_Server shutdown"
            self.s.close()
            print prompt +"UDP_Server close"
        except Exception as ex:
            print('Exception while shutting down UDP_Server:  {} - {}'.format(type(ex).__name__, ex.message))


if __name__ == '__main__':
    server = UDP_Server(None)
    server.Start_Server()    
