*************
 Fennel Time
*************

Our old `3com OfficeConnect ISDN Modem`_ (hostname ``fennel``) used to provide
our 2 analog phone numbers as well as ISDN connectivity for internet access.
(I'm so glad modern connectivity came to this neighborhood.)

The unit would synthesize caller ID information on its POTS ports when calls
came in, but the time reported for these calls were wildly incorrect.  Turns out
the thing had a bad real time clock.  Or maybe needed a new battery.  Whatever.

Ultimately, I wrote this script and ran it as a periodic cron job to keep the
time set.

.. References:
.. _`3com OfficeConnect ISDN Modem`: http://pro-networking-h17007.external.hp.com/us/en/support/converter/index.aspx?productNum=JE997A