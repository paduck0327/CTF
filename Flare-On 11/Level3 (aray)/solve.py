import struct

def conv_uint32(val):
	return list(struct.pack("<I", val))

filesize = 85
flag = [0 for i in range(filesize)]

# uint32
flag[52:52+4] = conv_uint32(1495724241 ^ 425706662)
flag[17:17+4] = conv_uint32(1412131772 + 323157430)
flag[59:59+4] = conv_uint32(1908304943 ^ 512952669)
flag[28:28+4] = conv_uint32(959764852 + 419186860)
flag[66:66+4] = conv_uint32(849718389 ^ 310886682)
flag[10:10+4] = conv_uint32(2448764514 - 383041523)
flag[37:37+4] = conv_uint32(1228527996 - 367943707)
flag[22:22+4] = conv_uint32(1879700858 ^ 372102464)
flag[46:46+4] = conv_uint32(1503714457 + 412326611)
flag[70:70+4] = conv_uint32(2034162376 - 349203301)
flag[80:80+4] = conv_uint32(69677856 + 473886976)
flag[3:3+4] = conv_uint32(2108416586 ^ 298697263)
flag[41:41+4] = conv_uint32(1699114335 - 404880684)

# uint8
flag[58] = 122 - 25 
flag[36] = 72 - 4 
flag[27] = 40 ^ 21 
flag[65] = 70 + 29 
flag[45] = 104 ^ 9 
flag[74] = 116 - 11 
flag[75] = 86 + 30 
flag[2] = 119 - 11 
flag[7] = 82 + 15 
flag[21] = 94 + 21 
flag[16] = 115 ^ 7 
flag[26] = 25 + 7 
flag[84] = 128 - 3 
print(''.join(map(chr,flag)))


# heur
flag[0] = ord('r')
flag[1] = ord('u')

flag[8] = ord('r')
flag[9] = ord('e')

flag[14]= ord(' ') # maybe
flag[15]= ord('s')

flag[56]= ord('f')
flag[57]= ord('l')

flag[63]= ord('n')
flag[64]= ord('.')

flag[76]= ord('i')
flag[77]= ord('o')
flag[78]= ord('n')
flag[79]= ord(':')

# hash (657dae0913ee12be6fb2a6f687aae1c7)
flag[50] = ord('3')
flag[51] = ord('A')

# hash (738a656e8e8ec272ca17cd51e12f558b)
flag[32] = ord('u')
flag[33] = ord('l')

# crc(0x5888fc1b)
from zlib import crc32
for i in range(0x20, 0x80):
	for j in range(0x20, 0x80):
		if(crc32(bytes([i, j])) == 0x5888fc1b):
			flag[34] = i
			flag[35] = j

print(''.join(map(chr,flag)))

