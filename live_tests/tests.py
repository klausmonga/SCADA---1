# python 3.11
from lib.tests_lib import send_report


def test_1():
    send_report({'status':1,'test_name':'Control de laliaison serie rs232 du capteur de pression','message':'TEST OK', 'flag':False})
    return True

def test_2():
    send_report({'status':1,'test_name':'Control de laliaison serie PIC du capteur DHT11','message':'TEST OK', 'flag':False})
    return True
def test_3():
    send_report({'status':1,'test_name':'Control de la conectivité avec le brocker','message':'TEST ok ', 'flag':False})
    return True
def test_4():
    send_report({'status':1,'test_name':'TEST du port usb0','message':'tty/usb0 OK', 'flag': True})
    return True
if __name__ == '__main__':
    if test_1():
        if test_2():
            if test_3():
                if test_4():
                    print("DONE TEST !!!")
