# Paweł

import socket
from datetime import datetime

# to do
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(process)d-%(levelname)s-%(message)s')
logging.warning('Admin logged out')
# debug(), info(), warning(), error(), and critical()

class LogEvents:
    """
    FileLog
    """
    def __init__(self, logname: str):
        self.logname:str = logname
        self.filename:str = ""

    def logMsg(self, sev: int, msg: str):
        #with open(self.fileName, "a") as file_to_save:
        hostname = socket.gethostname()
        #print(hostname)
        self.fileName = f"{hostname}_{self.logname}.txt"
        #print(self.fileName)
        try:
            file_to_save = open(self.fileName, "a")
        except:
            print(f"Problem z otwarciem pliku {self.fileName}")
            return False
        timeNow = datetime.now()
        file_to_save.write(f"{timeNow}\tsev: {sev}\tmsg: {msg}\n")

testEvent = LogEvents("EventLog")
testError = LogEvents("ErrorLog")

testEvent.logMsg(1, "EVENT: Testowa wiadomosc")
testError.logMsg(3, "ERROR: Testowa wiadomosc")
