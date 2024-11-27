# from django.test import TestCase
# from django.urls import reverse
# from django.core.files.uploadedfile import SimpleUploadedFile
# from about.models import Curriculum, Contact, Prestation, Presentation, Gallerie
# from website.models import SiteInfo

# # Curriculum Model Tests
# class CurriculumModelTests(TestCase):
#     def setUp(self):
#         self.curriculum = Curriculum.objects.create(
#             photo=SimpleUploadedFile('photo.jpg', b'file_content', content_type='image/jpeg'),
#             nom="Test Curriculum",
#             description="Test Description",
#             cv=SimpleUploadedFile('cv.pdf', b'file_content', content_type='application/pdf'),
#             status=True
#         )

#     def test_curriculum_creation(self):
#         self.assertEqual(self.curriculum.nom, "Test Curriculum")
#         self.assertTrue(self.curriculum.status)

#     def test_curriculum_str(self):
#         self.assertEqual(str(self.curriculum), "Test Curriculum")


# # Contact Model Tests
# class ContactModelTests(TestCase):
#     def setUp(self):
#         self.contact = Contact.objects.create(
#             nom="Test User",
#             email="test@example.com",
#             subject="Test Subject",
#             telephone=123456789,
#             message="Test message",
#             status=True
#         )

#     def test_contact_creation(self):
#         self.assertEqual(self.contact.nom, "Test User")
#         self.assertEqual(self.contact.email, "test@example.com")
#         self.assertTrue(self.contact.status)

#     def test_contact_str(self):
#         self.assertEqual(str(self.contact), "Test User")


# # Prestation Model Tests
# class PrestationModelTests(TestCase):
#     def setUp(self):
#         self.prestation = Prestation.objects.create(
#             titre="Test Prestation",
#             description="Test Description",
#             image=SimpleUploadedFile('prest.jpg', b'file_content', content_type='image/jpeg'),
#             status=True
#         )

#     def test_prestation_creation(self):
#         self.assertEqual(self.prestation.titre, "Test Prestation")
#         self.assertTrue(self.prestation.status)

#     def test_prestation_str(self):
#         self.assertEqual(str(self.prestation), "Test Prestation")


# # Presentation Model Tests
# class PresentationModelTests(TestCase):
#     def setUp(self):
#         self.presentation = Presentation.objects.create(
#             titre="Test Presentation",
#             image=SimpleUploadedFile('presentation.jpg', b'file_content', content_type='image/jpeg'),
#             description="Test Description",
#             status=True
#         )

#     def test_presentation_creation(self):
#         self.assertEqual(self.presentation.titre, "Test Presentation")
#         self.assertTrue(self.presentation.status)

#     def test_presentation_str(self):
#         self.assertEqual(str(self.presentation), "Test Presentation")


# # Gallerie Model Tests
# class GallerieModelTests(TestCase):
#     def setUp(self):
#         self.gallerie = Gallerie.objects.create(
#             gallerie=SimpleUploadedFile('image.jpg', b'file_content', content_type='image/jpeg'),
#             titre="Test Gallery",
#             status=True
#         )

#     def test_gallerie_creation(self):
#         self.assertEqual(self.gallerie.titre, "Test Gallery")
#         self.assertTrue(self.gallerie.status)

#     def test_gallerie_str(self):
#         self.assertEqual(str(self.gallerie), "Test Gallery")


# # Views Tests

# class AboutViewTests(TestCase):
#     def setUp(self):
#         # Create required objects
#         SiteInfo.objects.create(
#             nom="Test Site",
#             email="test@example.com",
#             telephone=123456789,
#             description="Test Description",
#             status=True
#         )
#         self.presentation = Presentation.objects.create(
#             titre="Test Presentation",
#             description="Test Description",
#             image=SimpleUploadedFile('presentation.jpg', b'file_content', content_type='image/jpeg'),
#             status=True
#         )

#     def test_about_view_status_code(self):
#         response = self.client.get(reverse('about'))
#         self.assertEqual(response.status_code, 200)

#     def test_about_view_template_used(self):
#         response = self.client.get(reverse('about'))
#         self.assertTemplateUsed(response, "pages/about-us.html")

#     def test_about_view_context(self):
#         response = self.client.get(reverse('about'))
#         self.assertIn('about', response.context)
#         self.assertEqual(response.context['about'][0], self.presentation)


# class ContactViewTests(TestCase):
#     def setUp(self):
#         # Create required objects
#         SiteInfo.objects.create(
#             nom="Test Site",
#             email="test@example.com",
#             telephone=123456789,
#             description="Test Description",
#             status=True
#         )

#     def test_contact_view_status_code(self):
#         response = self.client.get(reverse('contact'))
#         self.assertEqual(response.status_code, 200)

#     def test_contact_view_template_used(self):
#         response = self.client.get(reverse('contact'))
#         self.assertTemplateUsed(response, "pages/contact.html")


# class AuthorViewTests(TestCase):
#     def setUp(self):
#         # Create required objects
#         SiteInfo.objects.create(
#             nom="Test Site",
#             email="test@example.com",
#             telephone=123456789,
#             description="Test Description",
#             status=True
#         )
#         self.curriculum = Curriculum.objects.create(
#             nom="Test Author",
#             description="Test Author Description",
#             photo=SimpleUploadedFile('photo.jpg', b'file_content', content_type='image/jpeg'),
#             cv=SimpleUploadedFile('cv.pdf', b'file_content', content_type='application/pdf'),
#             status=True
#         )

#     def test_author_view_status_code(self):
#         response = self.client.get(reverse('author'))
#         self.assertEqual(response.status_code, 200)

#     def test_author_view_template_used(self):
#         response = self.client.get(reverse('author'))
#         self.assertTemplateUsed(response, "pages/author-posts-2.html")

#     def test_author_view_context(self):
#         response = self.client.get(reverse('author'))
#         self.assertIn('curriculum', response.context)
#         self.assertEqual(response.context['curriculum'], self.curriculum)


# class IsContactViewTests(TestCase):
#     def setUp(self):
#         # Create required objects
#         SiteInfo.objects.create(
#             nom="Test Site",
#             email="test@example.com",
#             telephone=123456789,
#             description="Test Description",
#             status=True
#         )

#     def test_is_contact_view(self):
#         data = {
#             'name': 'Test User',
#             'email': 'test@example.com',
#             'subject': 'Test Subject',
#             'tel': '123456789',
#             'messages': 'This is a test message.',
#         }
#         response = self.client.post(reverse('is_contact'), data)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('success', response.json())
#         self.assertTrue(response.json()['success'])
