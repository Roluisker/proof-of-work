import md5

string = "Hello, blockchain!"

complete = False
n = 0

while complete == False:
	curr_string = string + str(n)
	curr_hash = md5.new(curr_string).hexdigest()
	n = n + 1
  
	if curr_hash.startswith('000000'):
		print curr_hash
		print curr_string
		complete = True
