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
    
    def test_update_bio(self):
        """
        Test case to check if bio id updates
        """
        self.new_profile.save_profile()
        self.new_profile.update_bio("I'm a capricorn.")
        self.assertEqual(self.new_profile.bio, "I'm a capricorn.")
        

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

    def test_update_caption(self):
        """
        Test case to check if method updates caption of image
        """
        self.new_image.save_image()
        self.new_image.update_caption('This looks very cool.')
        self.assertEqual(self.new_image.image_caption, "This looks very cool.")

    def test_all_images(self):
        """
        Test case to check if all_images method returns QuerySet of all images
        """
        self.new_image.save_image()
        images = Image.all_images()
        self.assertTrue(len(images) > 0)

    def test_find_by_id(self):
        """
        Test case to check if find_by_id method returns single instance of image based on id
        """
        self.new_image.save_image()
        image = Image.find_by_id(self.new_image.id)

        self.assertTrue(image != None)
        self.assertTrue(isinstance(image, Image))

    def test_add_like(self):
        """
        Test case to check if add_like method adds one like to image model
        """
        self.new_image.save_image()
        self.new_image.add_like()

        self.assertEqual(self.new_image.likes, 1)

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

    def test_find_by_image(self):
        """
        Test case to check if find_by_image will return comments based on image instance
        """
        self.new_comment.save_comment()
        comments = Comment.find_by_image(self.new_image)

        self.assertTrue(len(comments) > 0)