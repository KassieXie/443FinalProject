from django.db import models
from django.contrib.auth.models import User
from PTL import image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='Profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

#	def save(self, *args, **kwargs):
#
#
#
#
#
#
#
#
#
#
#
#
