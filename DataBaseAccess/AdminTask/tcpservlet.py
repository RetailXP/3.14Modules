#!/usr/bin/env python

import sys
import socket
from time import sleep
import json
import threading
from Service.AndroidService import AndroidService
import queue
from AdminTask.MessageFormat import MessageFormat

class TCPServlet(threading.Thread):
    # IP Address of the server (host, that is, RPi)
    TCP_IP = '10.0.0.200'
    TCP_PORT = 5005
    BUFFER_SIZE = 4096
    
    #s = None 
    #conn = None 
    #addr = None 
    #service = None
    
    # When initialized, the TCPServlet will create a socket connection
    def __init__(self):
        threading.Thread.__init__(self)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((TCPServlet.TCP_IP, TCPServlet.TCP_PORT))
        self.s.listen(1)
        # accept() is a blocking operation, need to handle this later
        (self.conn, self.addr) = self.s.accept()
        # Set timeout for non-blocking IO
        self.conn.settimeout(2)
        print('Connection address:' + str(self.addr))
        # Create AndroidService object to make calls to database
        self.service = AndroidService()
        # Create message queue
        self.msgQueue = queue.Queue(0) 

    def getMsgQueue(self):
        return self.msgQueue

    def run(self):
        while 1:
            print("Waiting for data...")
            try:
                # Keep listening for incoming data
                data = self.conn.recv(TCPServlet.BUFFER_SIZE)
            except socket.timeout as e:
                err = e.args[0]
                if err == 'timed out':
                    # yield the current thread
                    sleep(1)
                    print('recv timed out, retry later')
                    continue
                else:
                    print(e)
                    sys.exit(1)
            except socket.error as e:
                print("Another error popped up")
                print(e)
                sys.exit(1)
            else:
                if not data:
                    print("no data, exiting")
                    break   
                else:
                    # Handle incoming data
                    print("received data:" + data.decode('utf-8'))
                    parsed_data = json.loads(data.decode('utf-8'))
                    request_type = parsed_data["Request"]
                    request_type = request_type.strip()
                    response = ""
                    print("Received request for: " + request_type)

                    if request_type == "MainDisplay":
                        # received message only consists of header
                        # return main display
                        query_result = self.service.getFirstPageInfo()
                        shoelist = list()
                        for tup in query_result:
                            selection = tup[0]
                            name = tup[1]
                            brand = tup[2]
                            desc = tup[3]
                            price = tup[4]
                            shoe = {'Selection':selection,'Name':name,'Brand':brand,'Desc':desc,'Price':price}
                            shoelist.append(shoe)
                        msg = {}
                        # shoe1 = {'Name':'Nike','Price':'3', 'Selection':'Selection1'}
                        # shoe2 = {'Name':'Adidas','Price':'4', 'Selection':'Selection2'}
                        msg['Type'] = 'MainDisplay'
                        # msg['Shoes'] = [shoe1, shoe2]
                        msg['Shoes'] = shoelist
                        response = json.dumps(msg);
                    elif request_type == "DetailedShoeDisplay":
                        # received message contains selection of requested shoe
                        # return detailed info for available shoes of selection
                        print("Selection: " + parsed_data["Selection"])
                        selection = (parsed_data["Selection"]).strip()
                        query_result = self.service.getSecondPageInfo(selection)
                        shoelist = list()
                        for tup in query_result:
                            barcode = tup[0]
                            size_US = tup[1]
                            size_UK = tup[2]
                            size_EURO = tup[3]
                            sizelist = [size_US, size_UK, size_EURO]
                            sex = tup[4]
                            avail = tup[5]
                            shoe = {'Barcode':barcode,'Size':sizelist,'Sex':sex,'Avail':avail}
                            shoelist.append(shoe)
                        msg = {}
                        msg['Type'] = 'DetailedShoeDisplay'
                        msg['Shoes'] = shoelist
                        response = json.dumps(msg)
                    elif request_type == "AvailabilityUpdate":
                        # return availability of the specified barcode
                        print("Barcode: " + parsed_data["Barcode"])
                        # Special case where JSON isn't used, just return a number
                        # Not sure if need to strip barcode, it's supposed to be a number
                        # barcode = (parsed_data["Barcode"]).strip()
                        response = self.service.numItemsAvailable(barcode);
                        print("Availability: " + str(response))
                    elif request_type == "Order":
                        # order a shoe
                        # no need for a response
                        print("Barcode: " + parsed_data["Barcode"])
                        customerID = "1" # Hardcoded customer ID
                        # Not sure if need to strip barcode, it's supposed to be a number
                        # barcode = (parsed_data["Barcode"]).strip()
                        # Order only one shoe. Don't need to get the response.
                        service_response = self.service.reserveInventoryIfAvailable(customerID, parsed_data["Barcode"], 1)
                        queued = (MessageFormat.retInv, service_response)
                        # Put this into the queue so that the admin task can relay it to the robot
                        self.msgQueue.put(queued)
                    elif request_type == "Restock":
                        # restock a shoe
                        # no need for a response
                        print("Barcode: " + parsed_data["Barcode"])
                        queued = (MessageFormat.depInv, str(parsed_data["Barcode"]))
                        self.msgQueue.put(queued)
                    # Need to append newline character so that it sends properly
                    print("Response: " + str(response))
                    response = str(response) + "\n"
                    print(len(response))
                    check = response.strip()
                    if len(check) > 0:
                        num = self.conn.send(bytes(response, 'UTF-8')) # echo
                        print("number of bytes sent:", num)
        print("bye felicia")
        self.conn.close()
        sys.exit(0)


def main():
    print("Hello")
    servlet = TCPServlet()
    print("Yo")
    servlet.start()
    print("Bye")
    

if __name__ == "__main__":
    main()  



