# Import dependencies
from subprocess import Popen, PIPE
import requests
import webbrowser

# We are going to write code to read and run python
# file, and store its output or error.
def execute_return(cmd):
	args = cmd.split()
	proc = Popen(args, stdout=PIPE, stderr=PIPE)
	out, err = proc.communicate()
	return out, err

# This function will make an HTTP request using StackOverflow
# API and the error we get from the 1st function and finally
# returns the JSON file.
def mak_req(error):
	resp = requests.get("https://api.stackexchange.com/" +
						"/2.2/search?order=desc&tagged=python&sort=activity&intitle={}&site=stackoverflow".format(error))
	return resp.json()

# This function takes the JSON from the 2nd function, and
# fetches and stores the URLs of those solutions which are
# marked as "answered" by StackOverflow. And then finally
# open up the tabs containing answers from StackOverflow on
# the browser.
def get_urls(json_dict):
	url_list = []
	count = 0
	
	for i in json_dict['items']:
		if i['is_answered']:
			url_list.append(i["link"])
		count += 1
		if count == 3 or count == len(i):
			break
	
	for i in url_list:
		webbrowser.open(i)


# Below line will go through the provided python file
# And stores the output and error.
out, err = execute_return("python C:\Users\Nishant Singh\Desktop\Stack_Over_Auto_Search\testpg.py")

# This line is used to store that part of error we are interested in.
erro = err.decode("utf-8").strip().split("\r\n")[-1]
print(erro)


# A simple if condition, if error is found then execute 2nd and
# 3rd function, otherwise print "No error".
if erro:
	filter_error = erro.split(":")
	json1 = mak_req(filter_error[0])
	json2 = mak_req(filter_error[1])
	json = mak_req(erro)
	get_urls(json1)
	get_urls(json2)
	get_urls(json)
	
else:
	print("No error")
