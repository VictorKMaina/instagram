from django.test import TestCase
from .models import Profile, Image, Comment, User

# Create your tests here.
class ProfileTest(TestCase):
    """
    Class for testing Profile methods and properties. Inherits from TestCase.
    """
    def setUp(self):
        """
        Runs before each test
        """
        self.new_user = User(username = 'vkm', email = 'user@example.com')
        self.new_user.save()

        self.new_profile = Profile(user = self.new_user, profile_photo = '/path/to/image/', bio = "I'm a leo.")
    
    def tearDown(self):
        """
        Runs after each test
        """
        Profile.objects.all().delete()

    def test_instance(self):
        """
        Test case to check if self.new_profile is instance of Profile Class
        """
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_profile(self):
        """
        Test case to check if profile object is being saved to database
        """
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        """
        Test case to check if method deletes profile
        """
        self.new_profile.save_profile()
        self.new_profile.delete_profile()

        profiles = Profile.objects.all()

        self.assertTrue(len(profiles) == 0)

        
        

class ImageTest(TestCase):
    """
    Class for testing Image methods and properties. Inherits from TestCase.
    """
    def setUp(self):
        """
        Runs before each test
        """
        self.new_user = User(username = 'vkm', email = 'user@example.com')
        self.new_user.save()

        self.new_profile = Profile(user = User.objects.all().first(), profile_photo = '/path/to/image/', bio = "I'm a leo.")
        self.new_profile.save()

        self.new_image = Image(image = '/path/to/image/', image_name = 'Test image', image_caption='This is a really nice image.', profile = self.new_profile)
    
    def tearDown(self):
        """
        Runs after each test
        """
        Profile.objects.all().delete()
        Image.objects.all().delete()

    def test_instance(self):
        """
        Test case to check if self.new_image is instance of  Image Class
        """
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_image(self):
        """
        Test case to check if image object is being saved to database
        """
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
    
    def test_delete_image(self):
        """
        Test case to check if method deletes image
        """
        self.new_image.save_image()
        self.new_image.delete_image()

        images = Image.objects.all()

        self.assertTrue(len(images) == 0)

class CommentTest(TestCase):
    """
    Class for testing Comment methods and properties. Inherits from TestCase.
    """
    def setUp(self):
        """
        Runs before each test
        """
        self.new_user = User(username = 'vkm', email = 'user@example.com')
        self.new_user.save()
        
        self.new_profile = Profile(user = User.objects.all().first(), profile_photo = '/path/to/image/', bio = "I'm a leo.")
        self.new_profile.save()

        self.new_image = Image(image = '/path/to/image/', image_name = 'Test image', image_caption='This is a really nice image.', profile = self.new_profile)
        self.new_image.save()

        self.new_comment = Comment(profile = self.new_profile, image = self.new_image, comment = "I love this picture.")
    
    def tearDown(self):
        """
        Runs after each test
        """
        Profile.objects.all().delete()
        Image.objects.all().delete()
        Comment.objects.all().delete()


    def test_instance(self):
        """
        Test case to check if self.new_comment is instance of Comment Class
        """
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_save_comment(self):
        """
        Test case to check if profile object is being saved to database
        """
        self.new_comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0)

    def test_delete_profile(self):
        """
        Test case to check if method deletes comment
        """
        self.new_comment.save_comment()
        self.new_comment.delete_comment()

        comments = Comment.objects.all()

        self.assertTrue(len(comments) == 0)