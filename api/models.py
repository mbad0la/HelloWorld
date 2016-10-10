from __future__ import unicode_literals

from django.db import models
from django_mysql.models import JSONField, Model
from django.template.defaultfilters import slugify

##########################################################
# MEMBERS
##########################################################
# {
#   name: "Abhinav Bansal",
#   post: "Collaborator",
#   img: "https://avatars3.githubusercontent.com/u/10768588?v=3&s=466",
#   contacts: [
#       {
#           name: "github",
#           link: "http://www.github.com/ab-decoded"
#       },
#       {
#           name: "facebook",
#           link: "http://facebook.com/abhinavbansal.1217"
#       }
#   ]
# }

class Contact(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=100)

    def __str__(self):
        contact_string = "{0}({1})".format(self.link, self.name)
        return contact_string

class Member(models.Model):
    name = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    img = models.URLField(null=True)
    contacts = models.ManyToManyField(Contact)

    def __str__(self):
        name_post_string = "{0}({1})".format(self.name, self.post)
        return name_post_string


##########################################################
# PROJECTS
##########################################################
# {
#     slug: "nyan-cat",
#     name: "Nyan Cat",
#     type: "Lol",
#     desc: "Short descrption",
#     icon: "/media/icons/cheater.jpg",
#     technologies: [
#         "Meteor",
#         "Mongo"
#     ],
#     long_desc: "Long description...",
#     contributors: [
#         {
#             name: "Abhinav Bansal",
#             github: "ab-decoded"
#         }
#     ],
#     "meta": {
#         "updated": "20-Jul-2016",
#         "size": "3M",
#         "version": "1.0.0",
#         "platform": "All"
#     }
# }

class Technology(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    
    def __str__(self):
        return self.name

class Contributor(models.Model):
    name = models.CharField(max_length=50)
    github = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name + "(" + self.github + ")"

class Project(models.Model):
    slug = models.CharField(max_length=100, blank=True, primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    desc = models.TextField()
    icon = models.ImageField(upload_to="icons", null=True)
    technologies = models.ManyToManyField(Technology, blank=True)
    long_desc = models.TextField(blank=True)
    contributors = models.ManyToManyField(Contributor)
    meta = JSONField()

    def __str__(self):
        return self.name+"("+self.desc+")"
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Project,self).save(*args,**kwargs)
