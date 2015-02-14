#modified code from zross at https://gist.github.com/zross. Big thanks to zross 

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import time

path = "/Users/MJ/Documents/idhack/Volume III -as passed 2014-15.pdf"

pattern = '(?<=<span style="font-family: UQGGBU\+GaramondPremrPro-LtDisp; font-size:12px">)(.*?)(?=<br></span></div>)'
# createDirectory(alltext, outpath, pattern)

def convert_pdf_to_html(path):
	rsrcmgr = PDFResourceManager()
	retstr = StringIO()
	codec = 'utf-8'
	laparams = LAParams()
	device = HTMLConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
	fp = file(path, 'rb')
	interpreter = PDFPageInterpreter(rsrcmgr, device)
	password = ""
	maxpages = 0 #is for all
	caching = True
	pagenos=set()
	for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
		interpreter.process_page(page)
	fp.close()
	device.close()
	str = retstr.getvalue()
	with open('volume_III.html', 'w') as f:
    		f.write(str) 
	retstr.close()
	# return str
	

# def getresult(theinfo):
# 	if theinfo:
# 		theinfo = theinfo.group(0)
# 	else:
# 		theinfo = ''
# 	return theinfo 

time1 = time.time()
alltext = convert_pdf_to_html(path)
time2 = time.time()
print time2-time1 	