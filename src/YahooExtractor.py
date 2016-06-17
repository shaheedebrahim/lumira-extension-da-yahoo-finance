import easygui
import sys
import urllib

mode = 0
size = 0
paramsList = []

class Mode:
	PREVIEW, EDIT, REFRESH = range(3)

def setSize(arg):
	global size
	size = arg

def setMode(arg):
	global mode
	mode = arg

def setParams(arg):
	global paramsList
	paramsList = arg

def configureURL(stockSymbol, startDateVals, endDateVals):
#http://ichart.finance.yahoo.com/table.csv?s=WU&a=01&b=19&c=2010&d=01&e=19&f=2010&g=d&ignore=.csv
	url = "http://ichart.finance.yahoo.com/table.csv?s="+stockSymbol+"&a="+startDateVals[0]+"&b="+startDateVals[1]+"&c="+startDateVals[2]+"&d="+endDateVals[0]+"&e="+endDateVals[1]+"&f="+endDateVals[2]+"&g=d&ignore=.csv"
	return url


def parseArgs():
	for i in range(len(sys.argv)):
		if str(sys.argv[i]).lower() == "-mode" and i+1 < len(sys.argv):
			if (str(sys.argv[i+1].lower()) == "preview"): setMode(Mode.PREVIEW)
			elif (str(sys.argv[i+1].lower()) == "edit"): setMode(Mode.EDIT)
			elif (str(sys.argv[i+1].lower()) == "refresh"): setMode(Mode.REFRESH)
		elif str(sys.argv[i].lower()) == "-size" and i+1 < len(sys.argv): setSize(int(sys.argv[i+1]))
		elif str(sys.argv[i]).lower() == "-params": setParams(str(sys.argv[i+1]).split(';'))

def parseDSBlock():
	fieldValues = [None]*3
	global paramsList
	
	for i in range(len(paramsList)):
		splitVals = paramsList[i].split('=')
		if splitVals[0] == "stockSymbol": fieldValues[0] = splitVals[1]
		elif splitVals[0] == "startDate": fieldValues[1] = splitVals[1]
		elif splitVals[0] == "endDate": fieldValues[2] = splitVals[1]
	
	return fieldValues
		
	

def sendDSBlock(fieldValues):
	print ("beginDSInfo")
	
	print("stockSymbol;"+fieldValues[0]+";true;")
	print("startDate;"+fieldValues[1]+";true;")
	print("endDate;"+fieldValues[2]+";true;")
	
	print ("endDSInfo")

def sendDataBlock(fieldValues):
	stockSymbol = fieldValues[0]
	startDateVals = fieldValues[1].split('-')
	endDateVals = fieldValues[2].split('-')
	url = configureURL(stockSymbol, startDateVals, endDateVals)
	
	print ("beginData")
	
	f = urllib.urlopen(url)
	for line in f:
		print (line.strip())
	
	print("endData")
	

def preview(fieldValues):

	msg = "Enter Required Information"
	title = "Yahoo Finance Extractor"
	fieldNames = ["Stock Symbol", "Start Date (dd-mm-yyyy)", "End Date (dd-mm-yyyy)"]
	
	fieldValues = easygui.multenterbox(msg,title,fieldNames,)
	errorMsg = ""
	while 1:
		if fieldValues == None: break
		for i in range(len(fieldNames)):
			if fieldValues[i] == "": errorMsg = "Please enter information into all fields"
			if i == 1 or i == 2:
				if len(fieldValues[i].split('-')) != 3:
					errorMsg = "Please enter dates in valid form"
		if errorMsg == "": break 
		fieldValues = easygui.multenterbox(errmsg, title, fieldNames, fieldValues)
		
	sendDSBlock(fieldValues)
	sendDataBlock(fieldValues)

def refresh():
	fieldValues = parseDSBlock()
	sendDataBlock(fieldValues)
	

	
def main():
	global mode
	global paramsList
	
	fieldValues = []
	
	parseArgs()
	
	if mode == Mode.PREVIEW: preview(fieldValues)	
	elif mode == Mode.EDIT or mode == Mode.REFRESH: refresh()

main()
		
	
	
	
	
	
	
	