import requests

from django.core.management.base import BaseCommand, CommandError
from api.models import Member, Contact, Technology, Contributor

GITHUB_API = "https://api.github.com/"

ORGANIZATION_ID = "o-d-i-n"
ORGANIZATION_NAME = "ODIN"

GTIHUB_MEMB_API = GITHUB_API + "orgs/" + ORGANIZATION_ID + "/members"

setup_msg = "Setuping up " + ORGANIZATION_NAME + " {0} for you..."

class Command(BaseCommand):
	help = "Inital setup " + ORGANIZATION_NAME + " organization (Need to run only one time)"

	def handle(self, *args, **options):

		self.stdout.write(self.style.SUCCESS(setup_msg.format("Members")))
		
		try:
			response = requests.get(GTIHUB_MEMB_API)
			
			for member in response.json():
				member_url = member['url']

				member_response = requests.get(member_url)
				member_response = member_response.json()
				m = Member()

				m.name = member_response['name']
				m.post = "Collaborator"
				m.img = member_response['avatar_url']

				# save each member
				m.save()
				
				if member_response['blog']:
					blog = Contact.objects.create(name="blog",link=member_response['blog'])
					m.contacts.add(blog)

				if member_response['email']:
					email = Contact.objects.create(name="email",link=member_response['email'])
					m.contacts.add(email)

				github = Contact.objects.create(name="github",link=member_response['html_url'])
				m.contacts.add(github)

				print "\t{0} loves you!".format(m.name)

			self.stdout.write(self.style.SUCCESS("Everybody loves you!"))
		except requests.exceptions.ConnectionError:
			raise CommandError("You need internet to setup " + ORGANIZATION_NAME + " locally!")
