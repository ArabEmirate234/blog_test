# from django.test import TestCase
# from django.urls import reverse
# from website.models import SiteInfo, SocialCount, Newsletter
# from elenizado.models import Publication, Evenement
# from about.models import Gallerie
# from django.core.files.uploadedfile import SimpleUploadedFile

# # SiteInfo Model Tests
# class SiteInfoModelTests(TestCase):
#     def setUp(self):
#         # Create a SiteInfo object for testing
#         self.site_info = SiteInfo.objects.create(
#             nom="Test Site",
#             email="test@example.com",
#             telephone=123456789,
#             description="This is a test site.",
#             logo=SimpleUploadedFile('logo.jpg', b'file_content', content_type='image/jpeg'),
#             status=True
#         )

#     def test_site_info_creation(self):
#         """Test if the SiteInfo model object is created correctly."""
#         self.assertEqual(self.site_info.nom, "Test Site")
#         self.assertEqual(self.site_info.email, "test@example.com")
#         self.assertTrue(self.site_info.status)

#     def test_site_info_str(self):
#         """Test the string representation of the SiteInfo model."""
#         self.assertEqual(str(self.site_info), "Test Site")


# # SocialCount Model Tests
# class SocialCountModelTests(TestCase):
#     def setUp(self):
#         # Create a SocialCount object for testing
#         self.social_count = SocialCount.objects.create(
#             nom="Facebook",
#             lien="https://facebook.com/test",
#             icones="fa-facebook-f",
#             status=True
#         )

#     def test_social_count_creation(self):
#         """Test if the SocialCount model object is created correctly."""
#         self.assertEqual(self.social_count.nom, "Facebook")
#         self.assertEqual(self.social_count.lien, "https://facebook.com/test")
#         self.assertEqual(self.social_count.icones, "fa-facebook-f")
#         self.assertTrue(self.social_count.status)

#     def test_social_count_str(self):
#         """Test the string representation of the SocialCount model."""
#         self.assertEqual(str(self.social_count), "Facebook")


# # Newsletter Model Tests
# class NewsletterModelTests(TestCase):
#     def setUp(self):
#         # Create a Newsletter object for testing
#         self.newsletter = Newsletter.objects.create(
#             email="newsletter@example.com",
#             status=True
#         )

#     def test_newsletter_creation(self):
#         """Test if the Newsletter model object is created correctly."""
#         self.assertEqual(self.newsletter.email, "newsletter@example.com")
#         self.assertTrue(self.newsletter.status)

#     def test_newsletter_str(self):
#         """Test the string representation of the Newsletter model."""
#         self.assertEqual(str(self.newsletter), "newsletter@example.com")


# # Index View Tests
# class IndexViewTests(TestCase):
#     def setUp(self):
#         """Create the necessary objects for the view tests."""
#         self.site_info = SiteInfo.objects.create(
#             nom="Test Site",
#             email="test@example.com",
#             telephone=123456789,
#             description="Test Description",
#             logo=SimpleUploadedFile('logo.jpg', b'file_content', content_type='image/jpeg'),
#             status=True
#         )

#         # Create some related objects (Publications, Events, Galleries)
#         self.publication = Publication.objects.create(
#             titre="Test Publication",
#             description="Test Description",
#             image="image/test.jpg",
#             status=True
#         )

#         self.event = Evenement.objects.create(
#             titre="Test Event",
#             description="Test Description",
#             status=True
#         )

#         self.gallerie = Gallerie.objects.create(
#             titre="Test Gallery",
#             gallerie="image/test.jpg",
#             status=True
#         )

#     def test_index_view_status_code(self):
#         """Test if the index view returns a 200 status code."""
#         response = self.client.get(reverse('index'))
#         self.assertEqual(response.status_code, 200)

#     def test_index_view_template_used(self):
#         """Test if the correct template is used for the index view."""
#         response = self.client.get(reverse('index'))
#         self.assertTemplateUsed(response, "pages/index.html")

#     def test_index_view_context(self):
#         """Test if the context contains the expected objects."""
#         response = self.client.get(reverse('index'))
#         self.assertIn('site_info', response.context)
#         self.assertIn('publication_r', response.context)
#         self.assertIn('events_r', response.context)
#         self.assertIn('gallerie', response.context)


# # Newsletter View Tests
# class NewsletterViewTests(TestCase):
#     def setUp(self):
#         """Create required objects for the newsletter view tests."""
#         self.site_info = SiteInfo.objects.create(
#             nom="Test Site",
#             email="test@example.com",
#             telephone=123456789,
#             description="Test Description",
#             logo=SimpleUploadedFile('logo.jpg', b'file_content', content_type='image/jpeg'),
#             status=True
#         )

#     def test_is_newsletter_view_success(self):
#         """Test the successful submission of the newsletter."""
#         data = {'email': 'testnewsletter@example.com'}
#         response = self.client.post(reverse('is_newsletter'), data)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('success', response.json())
#         self.assertTrue(response.json()['success'])

#     def test_is_newsletter_view_failure(self):
#         """Test the failed submission of the newsletter with invalid email."""
#         data = {'email': 'invalid-email'}
#         response = self.client.post(reverse('is_newsletter'), data)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('success', response.json())
#         self.assertFalse(response.json()['success'])
