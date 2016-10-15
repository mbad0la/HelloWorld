import requests

from models import Member, Contact

def my_func():
	GTIHUB_URL = "https://api.github.com/orgs/o-d-i-n/members"
	TEST_URL = "https://api.myjson.com/bins/331qk"
	return_resp = []

	response = requests.get(TEST_URL)
	
	for member in response.json():
		member_url = member['url']
		print member_url

		member_response = requests.get(member_url)
		member_response = member_response.json()
		m = Member()

		m.name = member_response['name']
		m.post = member['type']
		m.img = member_response['avatar_url']

		m.save()
		# member saved
		
		if member_response['blog']:
			print member_response['blog']
			blog = Contact.objects.create(name="Blog",link=member_response['blog'])
			m.contacts.add(blog)

		github = Contact.objects.create(name="GitHub",link=member_response['html_url'])
		m.contacts.add(github)

		return_resp.append(member_response['name'])

	return return_resp
