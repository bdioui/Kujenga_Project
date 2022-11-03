from django.db import models
import uuid
from datetime import *

identifier = uuid.uuid4()

def get_image_filepath(self, filename):
	return 'portfolio_images/' + str(self.titre[0]) + '/' + str(identifier) + '/illustration.jpg'

class Projet(models.Model):
	titre = models.TextField()
	description = models.TextField()
	date = models.DateField(default=datetime.today())
	image = models.FileField(upload_to=get_image_filepath, null=True, blank=True)
	image_2 = models.FileField(upload_to=get_image_filepath, null=True, blank=True)
	image_3 = models.FileField(upload_to=get_image_filepath, null=True, blank=True)

	def __str__(self):
		return self.titre

class Message(models.Model):
	prénom = models.TextField()
	nom = models.TextField()
	message = models.TextField()
	email = models.EmailField()
	date = models.DateField(default=datetime.today())

	def __str__(self):
		return 'message de '+ self.prénom + ' ' + self.nom

