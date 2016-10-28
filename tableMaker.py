def parseFile(workFile, instructionsDic, memDic):

	for addrLine in workFile:
		inst = addrLine.split(",")
		pageNum = int(inst[0],16)/ 4096
		localAddr = int(inst[0],16)% 4096
		newEntry = hex(localAddr)

		if inst[1][0] in ['I']:
			if newEntry in instructionsDic:
				instructionsDic[newEntry] += 1
			else:
				instructionsDic[newEntry] = 1  		
		else:
			if newEntry in memDic:
				memDic[newEntry] += 1
			else:
				memDic[newEntry] = 1 

def writeDictToFile(name, instructionsDic, MemDic):
	outFile = open(name, "w+")

	outFile.write("Intructions Access:\n")
	for key, value in instructionsDic.iteritems():
		outFile.write(str(key) + " " + str(value) + "\n")
	
	outFile.write("\n\nMemory Access:\n")
	for key, value in MemDic.iteritems():
		outFile.write(str(key) + " " + str(value) + "\n")

	outFile.close()
		

instructionsDic = {}
memDic = {}

heap = open("tr-heaploop.ref", "r")
stack = open("tr-matmul.ref", "r")


parseFile(heap, instructionsDic, memDic)
parseFile(stack, instructionsDic, memDic)

writeDictToFile("readme.txt", instructionsDic, memDic)


