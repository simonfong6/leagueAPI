import sys

args = sys.argv

api = str(args[1])
i = 0
for api in args:
	if(i==0):
		i+=1
		continue		
	
	length = len(api)

	start = False
	keys = []
	key = ""
	newApi = "\""
	for j in range(length):
		char = api[j]
		if(char == "}"):
			start = False
			keys.append(key)
			key=""

		if(start == False):
			newApi += char
		else:
			key += char

		if(char == "{"):
			start = True

	newApi += "\".format("

	first = True
	for key in keys:
		if(first == False):
			newApi += ", "	
		newApi += key	
		first = False

	newApi += ")"
	print newApi
