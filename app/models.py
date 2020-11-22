from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    """
    Class to define Profile instances. Inherits from models.Model.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField()
    bio = models.CharField(max_length = 350)

class Image(models.Model):
    """
    Class to define Image instances. Inherits from models.Model.
    """
    image = CloudinaryField('image')
    image_name = models.CharField(max_length = 255)
    image_caption = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.IntegerField(null=True)

class Comment(models.Model):
    """
    Class to define Comment instances. Inherits from models.Model.
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    comment = models.TextField()