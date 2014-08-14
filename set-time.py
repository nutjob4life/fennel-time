#!/usr/bin/env python
#
# fennel, the 3com OfficeConnect ISDN LAN modem, provides analog
# telephone service in our home of Piedra Blanca.  However, its clock
# is bad (or maybe it simply needs a fresh battery), so when a call
# comes in, it announces the time of the call in the analog caller-ID
# stream bad.  So, this script sets the LAN modem's clock.  It should
# be run periodically from cron to keep the LAN modem's clock
# synchronized to actual local time.  Running every hour or so should
# be sufficient, you'd think, but the clock has so much drift that
# more frequent updates seem to be necessary.

import datetime, telnetlib

class OfficeConnectISDNLANModem(object):
    def __init__(self):
        self.modem = telnetlib.Telnet('fennel.home.zon')

    def setTime(self):
        index, match, text = self.modem.expect(['Password:'], timeout=5)
        if index == -1: raise IOError('No password prompt found')
        self.modem.write('\r\n')
        index, match, text = self.modem.expect(['Password:'], timeout=5)
        if index == -1: raise IOError('No 2nd password prompt found')
        self.modem.write('secret\r\n')
        index, match, text = self.modem.expect(['LANmodem>'], timeout=5)
        if index == -1: raise IOError('No command prompt found')
        current = datetime.datetime.today()
        self.modem.write('tset %d %d %d %d %d %s\r\n' % (current.year, current.month, current.day, \
                                 current.hour, current.minute, current.second))
        index, match, text = self.modem.expect(['LANmodem>'], timeout=5)
        if index == -1: raise IOError('Time setting failed')
        self.modem.write('exit\r\n')
        self.modem.close()

if __name__ == '__main__':
    modem = OfficeConnectISDNLANModem()
    modem.setTime()
