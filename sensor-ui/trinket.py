import sys, time, getopt, select
import usb.core, usb.util
import logging
import inspect

logger = logging.getLogger()

class Sensor:
    name = 'sensor_trinket'
    keyword = 'sensor'
    trinket = False
    endpoint = 0x81

    def __init__(self):
        self.trinket = self.__findTrinket()

        if self.trinket != False:
            self.endpoint = self.trinket[0][(0,0)][0]

    def __del__(self):
        self.trinket = False

    # This is invoked when installed as a Bottle plugin
    def setup(self, app):
        self.routes = app

        for other in app.plugins:
          if not isinstance(other, Sensor):
            continue
          if other.keyword == self.keyword:
            raise PluginError("Found another instance of Sensor running!")

    # This is invoked within Bottle as part of each route when installed
    def apply(self, callback, context):
        conf = context.get('sensor') or {}
        keyword = conf.get('keyword', self.keyword)

        args = inspect.getargspec(callback)[0]
        if keyword not in args:
            return callback

        def wrapper(*args, **kwargs):
            kwargs[self.keyword] = self
            rv = callback(*args, **kwargs)
            return rv
        return wrapper

    # De-installation from Bottle as a plugin
    def close(self):
        self.trinket = False

    def readline(self):
        if not self.trinket:
            logging.error('No trinket connected')
            return

        try:
            char_buffer = ''
            while True:
                data = self.trinket.read(self.endpoint.bEndpointAddress, self.endpoint.wMaxPacketSize)
                readCnt = len(data)
                if readCnt > 0:
                    char_buffer += bytearray(data)
                    if '\r\n' in char_buffer[-2:] and len(char_buffer.strip()) > 0:
                        return char_buffer.strip()

        except Exception as ex:
            exStr = str(ex).lower()
            if 'timeout' not in exStr:
                logging.error('USB read error', ex)
                self.trinket = False

    def __findTrinket(self):
        device = usb.core.find(idVendor = 0x1781, idProduct = 0x1111)
        if device == None or device == False or device == 0 :
            return False

        device.set_configuration()
        return device
