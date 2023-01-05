# O(1) time, O(n) space - n is the number of unique messages that have been received 
class Logger(object):
    # creates a dictionary to store the message and the timestamp of the last time it was received
    def __init__(self):
        self._msg_dict = {}
    
    # function to check if the message should be printed by checking if the message is in the dictionary
    # if it is, check if the timestamp is greater than or equal to 10 from the last time it was received
    # if it is, update the timestamp and return True
    def shouldPrintMessage(self, timestamp, message):
        if message not in self._msg_dict:
            self._msg_dict[message] = timestamp
            return True
        
        # if the message is in the dictionary, check if the timestamp is greater than or equal to 10 from the last time it was received
        if timestamp - self._msg_dict[message] >= 10:
            self._msg_dict[message] = timestamp
            return True
        else:
            return False
