import urllib.request
import json

'''
Taking username and repo name to reach out to the repo data using github's
REST API v3
'''
username = input("Enter your username: ")
repo = input("Enter your repository name: ")
url = "https://api.github.com/repos/%s/%s/stats/contributors"%(username, repo)

'''
Open the specified url and bring back the json object in this case.
json.loads() converts the json object as a string into a python dict or list.
'''
with urllib.request.urlopen(url) as response:
	stats_contributors = json.loads(response.read().decode())

'''
just some html stuff

head is what comes at the top and is used only once per file. It contains the
column headings.

row is the recurring part that creates each row of the table.

foot is the last part of the html table. It contains only the closing table
tag. 
'''
head = """<html>
	<head></head>
	<body>
		<table>
			<tr>
				<th rowspan="2">S. No.</th>
				<th colspan="3">Contributors</th>
				<th rowspan="2">Commits</th>
			</tr>
			<tr>
				<th>Avatar</th>
				<th>Name</th>
				<th>User name</th>
			</tr>"""
row = """
			<tr>
				<td align="center"><counter>.</td>
				<td><img src="<avatar_url>" width="100" height="100" alt="<name>'s avatars"></td>
				<td align="center"><name></td>
				<td align="center"><a href="<html_url>"><login></a></td>
				<td align="center"><a href="https://github.com/%s/%s/commits?author=<login>"><name>'s<br>commits</a></td>
			</tr>"""%(username, repo)
foot = """
		</table>
	</body>
</html>"""


#open the file in write mode.
with open('contributors.md', 'w') as outfile:
	outfile.write(head)
	'''
	for every element in the list returned by stats_contributors, get the url
	of the user in that element. Use this url to further get another JSON 
	object and use this new object to get the details you want about the user.
	'''
	for i in range(len(stats_contributors)):
		row_temp = row

		user_url = stats_contributors[i]['author']['url']
		with urllib.request.urlopen(user_url) as response:
			user_data = json.loads(response.read().decode())

		row_temp = row_temp.replace('<counter>', str(i+1))
		row_temp = row_temp.replace('<avatar_url>', user_data['avatar_url'])
		row_temp = row_temp.replace('<name>', user_data['name'])
		row_temp = row_temp.replace('<html_url>', user_data['html_url'])
		row_temp = row_temp.replace('<login>', user_data['login'])

		outfile.write(row_temp)
	outfile.write(foot)

input("contributors.md has been created.\nPress enter to exit.")

'''
P.S.: The stats_contributors contains list of dictionaries containing
dictionaries.
'''
