import serial
import serial.tools.list_ports
import time

def test():
    #enumerate serial ports
    """
    for port in serial.tools.list_ports.comports():
        s = port
        print(port)
        print(s[0])
    """

    arq = open("test.txt", "w")
    arq.write("test for python\n")

    try:
        p = serial.Serial("COM3", baudrate = 115200, timeout = .1)

        #wait for arduino
        time.sleep(2)

        a = "test for ready"

        p.write(bytes(a, "ASCII"))

        line = p.readline().decode("ASCII")
        
        while len(line) > 0:
            line = line[:len(line) - 1]
            print(line)
            arq.write(line)
            arq.flush()
            line = p.readline().decode("ASCII")

    except Exception as e:
        print(e)

    arq.close()
    
test()
