#
# Tello Python3 Control Demo
#
# http://www.ryzerobotics.com/
#
# 1/1/2018


#This is a test to eliminate the delays/sleep time by the drone

import threading
import socket
import sys
import time
from tello import Tello
from datetime import datetime

host = ''
port = 9000
locaddr = (host,port)


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#tello_address0 = ('192.168.0.36', 8889) # DC8
tello_address1 = ('192.168.10.1', 8889) # FDC
sock.bind(locaddr)

def recv():
    print ('Grognak')
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print ('Recv Data')
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break


print ('\r\n\r\nTello Python3 Demo.\r\n')

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print ('end -- quit demo.\r\n')


#






#recvThread create
#recvThread = threading.Thread(target=recv)
#recvThread.start()
file_name = 'CommandFDC.txt'
f = open(file_name, "r")
CommandsFDC = f.readlines()
FDC_len = len(CommandsFDC)
##file_name = 'Command DC8.txt'
##f = open(file_name, "r")
##CommandsDC8 = f.readlines()
##DC8_len = len(CommandsDC8)
if DC8_len >= FDC_len:
    longest = DC8_len
else:
    longest = FDC_len
i = 0
while (i < (longest +1)):
    cmdFDC = CommandsFDC[i]
    cmdDC8 = CommandsDC8[i]
    cmdFDC = cmdFDC.rstrip()
    cmdDC8 = cmdDC8.rstrip()
    msg1 = cmdDC8
    msg1 = msg1.encode(encoding="utf-8")
    print ('DC8 =', msg1)
    sent = sock.sendto(msg1, tello_address0)
    msg2 = cmdFDC
    msg2 = msg2.encode(encoding="utf-8")
    print ('FDC =', msg2)
    sent = sock.sendto(msg2, tello_address1)
    waitflag = True
    i = i + 1
    index = 0
    NumOk = 0
    while waitflag:
        index += 1
        print ('in while loop', index)
        response, ip = sock.recvfrom(1518)
        RDecode = response.decode(encoding="utf-8")
        print ('response =', RDecode)
        print ('ip =', ip)
        if RDecode == 'ok':
            NumOk += 1
            if NumOk == 1:
                waitflag = False
            print ('Recv Ok')
    else:
        print ('end -- quit demo.\r\n')















##        if command.find('delay') != -1:
##            sec = float(command.partition('delay')[2])
##            print ('delay %s' % sec)
##            time.sleep(sec)


#===================Up is Nov 2 Edits Bellow is before that===================
#            sent = sock.sendto(msg, tello_address1)
#            else:
#                tello.send_command(command)


        #if not msg:
        #    break

        #if 'end' in msg:
         #   print ('...')
        #    sock.close()
         #   break

        # Send data
#                msg = msg.encode(encoding="utf-8")
#            sent = sock.sendto(msg, tello_address0)
#            sent = sock.sendto(msg, tello_address1)
#except KeyboardInterrupt:
#    print ('\n . . .\n')
#    sock.close()
#    break

#===============================(Drone 1)======================================#
#start_time = str(datetime.now())

#file_name = sys.argv[1]
#file_name = 'command3.txt'
#f = open(file_name, "r")
#commands = f.readlines()

#tello = Tello('192.168.0.39', 8889)
#for command in commands:
 #   if command != '' and command != '\n':
 #       command = command.rstrip()
#
 #       if command.find('delay') != -1:
  #          sec = float(command.partition('delay')[2])
   #         print ('delay %s' % sec)
    #        time.sleep(sec)
     #       pass
      #  else:
       #     tello.send_command(command)


#=====================(Drone 2)=====================#


#tello = Tello('192.168.0.40')
#for command in commands:
#    if command != '' and command != '\n':
#        command = command.rstrip()
#
#        if command.find('delay') != -1:
#            sec = float(command.partition('delay')[2])
#            print ('delay %s' % sec)
#            time.sleep(sec)
#            pass
#        else:
#           tello.send_command(command)
# log = tello.get_log()
#
# out = open('log/' + start_time + '.txt', 'w')
# for stat in log:
#     stat.print_stats()
#     str = stat.return_stats()
#     out.write(str)


#    try:
        #msg = input("");
