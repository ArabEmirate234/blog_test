# from django.test import TestCase
# from django.urls import reverse
# from oeuvre.models import Poesie
# from website.models import SiteInfo
# from elenizado.models import Evenement
# from about.models import Gallerie
# from tinymce.models import HTMLField
# from django.core.files.uploadedfile import SimpleUploadedFile

# # Poesie Model Tests
# class PoesieModelTests(TestCase):
#     def setUp(self):
#         # Create a Poesie object for testing
#         self.poeme = Poesie.objects.create(
#             titre="Test Poem",
#             description="This is a test description of the poem.",
#             poeme="<p>This is the body of the poem.</p>",  # Using HTMLField for poem content
#             status=True
#         )

#     def test_poeme_creation(self):
#         """Test if the Poesie model object is created correctly."""
#         self.assertEqual(self.poeme.titre, "Test Poem")
#         self.assertEqual(self.poeme.description, "This is a test description of the poem.")
#         self.assertTrue(self.poeme.status)

#     def test_poeme_str(self):
#         """Test the string representation of the Poesie model."""
#         self.assertEqual(str(self.poeme), "Test Poem")


# # Poeme View Tests
# class PoemeViewTests(TestCase):
#     def setUp(self):
#         """Create the necessary objects for the view tests."""
#         # Create a site info object for the context
#         SiteInfo.objects.create(
#             nom="Test Site",
#             email="test@example.com",
#             telephone=123456789,
#             description="Test Description",
#             status=True
#         )

#         # Create a Poesie object for testing the view
#         self.poeme = Poesie.objects.create(
#             titre="Test Poem",
#             description="This is a test description of the poem.",
#             poeme="<p>This is the body of the poem.</p>",  # HTML content
#             status=True
#         )

#         # Create an event for the view context
#         Evenement.objects.create(
#             titre="Test Event",
#             description="This is a test event.",
#             status=True
#         )

#         # Create a gallery object for the view context
#         Gallerie.objects.create(
#             titre="Test Gallery",
#             gallerie="image/test.jpg",  # Mock image path
#             status=True
#         )

#     def test_poeme_view_status_code(self):
#         """Test the status code of the Poeme view."""
#         response = self.client.get(reverse('poeme'))
#         self.assertEqual(response.status_code, 200)

#     def test_poeme_view_template_used(self):
#         """Test if the correct template is used for the Poeme view."""
#         response = self.client.get(reverse('poeme'))
#         self.assertTemplateUsed(response, "pages/poesie.html")

#     def test_poeme_view_context(self):
#         """Test if the context contains the expected objects."""
#         response = self.client.get(reverse('poeme'))
#         self.assertIn('poeme', response.context)
#         self.assertIn('events_r', response.context)
#         self.assertIn('gallerie', response.context)
#         self.assertEqual(response.context['poeme'][0], self.poeme)
