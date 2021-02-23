# Protocol Constants

CMD_FIELD_LENGTH = 16	# Exact length of cmd field (in bytes)
LENGTH_FIELD_LENGTH = 4   # Exact length of length field (in bytes)
MAX_DATA_LENGTH = 10**LENGTH_FIELD_LENGTH-1  # Max size of data field according to protocol
MSG_HEADER_LENGTH = CMD_FIELD_LENGTH + 1 + LENGTH_FIELD_LENGTH + 1  # Exact size of header (CMD+LENGTH fields)
MAX_MSG_LENGTH = MSG_HEADER_LENGTH + MAX_DATA_LENGTH  # Max size of total message
DELIMITER = "|"  # Delimiter character in protocol
DATA_DELIMITER = "#"  # Delimiter in the data part of the message

# Protocol Messages 
# In this dictionary we will have all the client and server command names

PROTOCOL_CLIENT = {
"login_msg" : "LOGIN",
"logout_msg" : "LOGOUT"
} # .. Add more commands if needed


PROTOCOL_SERVER = {
"login_ok_msg" : "LOGIN_OK",
"login_failed_msg" : "ERROR"
} # ..  Add more commands if needed


# Other constants

ERROR_RETURN = None  # What is returned in case of an error


def build_message(cmd, data):
	"""
	Gets command name (str) and data field (str) and creates a valid protocol message
	Returns: str, or None if error occured
	"""

	if (len(cmd) > CMD_FIELD_LENGTH or len (data) > MAX_DATA_LENGTH):
		return None

	fill_blank_str = 16 -len(cmd)
	blank_str = " "*fill_blank_str
	fill_blank_zero = 4 - number_of_characters(data)
	blank_zero = "0"*fill_blank_zero
	if (number_of_characters(data) == 0):
		full_msg = cmd + blank_str + "|" + blank_zero + "|"
		return full_msg
	str_number = str(len(data))
	full_msg = cmd + blank_str +"|"+ blank_zero + str_number +"|"+ data

	return full_msg



def number_of_characters(data):
	"""
	Gets: string
	Returns: int,  size of the string (number of characters)
	"""

	size = len(data)
	list_data = []
	if (size == 0):
		return 0;
	i = 1
	while (size>9):
		i += 1
		size = size /10

	return i
def parse_message(data):

	"""
	Parses protocol message and returns command name and data field
	Returns: cmd (str), data (str). If some error occured, returns None, None
	"""

	if (len (data) == 0):
		return None, None

	listdata = data.split('|')

	if (len(listdata)>2):

		number = listdata[1]
		print (number)
		cmd = listdata[0]
		cmd = cmd.replace(" ", "")
		msg = listdata [2]
		number = int(listdata[1])

		if (number < 0 ):
			return None,None
		if (cheek_number_equal_str(number,listdata [2])):
			return None, None

		return cmd,msg

	return None,None

def cheek_number_equal_str (number ,data):
	if (number != len(data)):
		return True
	return False

	
def split_data(msg, expected_fields):
	""""
	Helper method. gets a string and number of expected fields in it. Splits the string 
	using protocol's data field delimiter (|#) and validates that there are correct number of fields.
	Returns: list of fields if all ok. If some error occured, returns None
	"""



	listdata = msg.split("#")

	if (len(listdata) == expected_fields + 1):
		return listdata
	else:
		for i in range(len(listdata)):
			listdata[i] = None

	return listdata

def join_data(msg_fields):
	"""
	Helper method. Gets a list, joins all of it's fields to one string divided by the data delimiter. 
	Returns: string that looks like cell1#cell2#cell3
	"""

	if (msg_fields[0] != None):
		msg = "#".join(msg_fields)
		return msg
	return None

if __name__ == '__main__':
	msg = "davi#dgiladi#the#king"
	print(type(msg))
	expected_fields = 3

	str = build_message("LadadshIN ","aaaa#bbbb")
	print (str)
	print (parse_message("LOGIN           |	 -4|data"))
	i = 'z'
	print (isinstance(i, int))




