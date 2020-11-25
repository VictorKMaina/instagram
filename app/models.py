from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    """
    Class to define Profile instances. Inherits from models.Model.
    """
    user = models.OneToOneField(User, primary_key = True, on_delete=models.CASCADE)
    profile_photo = CloudinaryField(default = 'image/upload/v1606300231/gzwpgegxjpsonlkjrviq.svg')
    bio = models.CharField(max_length = 350)

    def __str__(self):
        return f"Profile for  {self.user.username}"

    def save_profile(self):
        """
        Method to save profile to database
        """
        self.save()
        print(f'Profile ID {self.user.id} saved.')

    def delete_profile(self):
        self.delete()

    def update_bio(self, bio):
        self.bio = bio
        self.save_profile()

class Image(models.Model):
    """
    Class to define Image instances. Inherits from models.Model.
    """
    image = CloudinaryField('image')
    image_name = models.CharField(max_length = 255)
    image_caption = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.IntegerField(default = 0)

    def __str__(self):
        return f'Image {self.image_name} ID {self.id}'

    def save_image(self):
        """
        Method to save profile to database
        """
        self.save()
        print(f'Image ID {self.id} saved.')

    def delete_image(self):
        self.delete()

    def update_caption(self, image_caption):
        self.image_caption = image_caption
        self.save_image()
    
    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def find_by_id(cls, id):
        image = cls.objects.filter(id = id).first()
        return image


class Comment(models.Model):
    """
    Class to define Comment instances. Inherits from models.Model.
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f'Comment ID {self.id}'

    def save_comment(self):
        """
        Method to save profile to database
        """
        self.save()
        print(f'Comment ID {self.id} saved.')

    def delete_comment(self):
        self.delete()