from html.parser import HTMLParser
from http import client as httplib
import urllib
import ssl

#https://10.0.127.14/
username="oschokchai"
password="Nov2018!"
# Reset Password https://myid.dtac.co.th/showLogin.cc


# Authentication choices -- NOT SUPPORT "Specific Sign-on"
# 1: Standard Sign-on
# 2: Sign-off
selected_choice = 1
authen_choices = ["Standard Sign-on", "Sign-off"]
if hasattr(ssl, '_create_unverified_context'):
	ssl._create_default_https_context = ssl._create_unverified_context

loginIP = "10.0.127.14"
header = {
	"Host": "10.0.127.14",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Language": "en-us,en;q=0.5",
	"Accept-Encoding": "gzip, deflate",
	"Connection": "keep-alive",
	"Referer": "https://10.0.127.14/",
	"Content-Type" : "application/x-www-form-urlencoded"
}

header["Content-Length"] = 0

class Parser(HTMLParser):
	foundIDAttr = False
	input_id = ""
	foundFirstParagraphTag = False
	result = ""

	def handle_starttag(self, tag, attrs):
		if tag == "input":
			for attr in attrs:
				if attr[1] == "ID":
					self.foundIDAttr = True
				elif self.foundIDAttr and self.input_id == "":
					self.input_id = attr[1]
		elif tag == "p":
			self.foundFirstParagraphTag = True

	def handle_data(self, data):
		if self.foundFirstParagraphTag and self.result == "":
			self.result = data

# Get request the Login form
print("Connecting authen server ...")
conn = httplib.HTTPSConnection(loginIP)
conn.request("GET","/")
res = conn.getresponse()
data = res.read()
parser = Parser()
parser.feed(str(data))
input_id = parser.input_id

# Post Username
body = "ID=" + input_id + "&STATE=1&DATA=" + username
header["Content-Length"] = len(body)
print("sending Username ...")
conn.request("POST","/",body,header)
res = conn.getresponse()
data = res.read()
parser = Parser()
parser.feed(str(data))
input_id = parser.input_id
response_text = parser.result

if response_text.find("Unable to activate") == -1:
	# Post Password
	escapePassword = urllib.parse.quote(password)
	body = "ID=" + input_id + "&STATE=2&DATA=" + escapePassword
	header["Content-Length"] = len(body)
	print("sending Password ...")
	conn.request("POST","/",body,header)
	res = conn.getresponse()
	data = res.read()
	parser = Parser()
	parser.feed(str(data))
	input_id = parser.input_id
	response_text = parser.result
	# If Password is correct
	if response_text.find("Access denied") == -1:
		# Post Authen type
		body = "ID=" + input_id + "&STATE=3&DATA=" + str(selected_choice)
		header["Content-Length"] = len(body)
		print("authen with " + authen_choices[selected_choice - 1] + " ...")
		conn.request("POST","/",body,header)
		res = conn.getresponse()
		data = res.read()
		parser = Parser()
		parser.feed(str(data))
		print(parser.result)
	else:
		print(response_text)
else:
	print(response_text + "Please check your username")

import platform
plat = platform.system()
if plat == 'Windows' or plat == 'Microsoft':
	raw_input("Press Enter to continue...")
