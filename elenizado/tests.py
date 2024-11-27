# from django.test import TestCase
# from django.urls import reverse
# from elenizado.models import (
#     Categorie, Publication, Commentaire, ReponseCommentaire,
#     Evenement, Cours, Textes, Video
# )
# from website.models import SiteInfo

# # Model Tests
# class CategorieModelTests(TestCase):
#     def setUp(self):
#         self.categorie = Categorie.objects.create(
#             nom="Test Category",
#             description="This is a test category.",
#             status=True
#         )

#     def test_categorie_creation(self):
#         self.assertEqual(self.categorie.nom, "Test Category")
#         self.assertTrue(self.categorie.status)

#     def test_categorie_str(self):
#         self.assertEqual(str(self.categorie), "Test Category")


# class PublicationModelTests(TestCase):
#     def setUp(self):
#         self.categorie = Categorie.objects.create(nom="Test Category", description="Test", status=True)
#         self.publication = Publication.objects.create(
#             titre="Test Publication",
#             description="This is a test publication.",
#             image="image/test.jpg",
#             categorie=self.categorie,
#             status=True
#         )

#     def test_publication_creation(self):
#         self.assertEqual(self.publication.titre, "Test Publication")
#         self.assertEqual(self.publication.categorie, self.categorie)
#         self.assertTrue(self.publication.status)

#     def test_publication_slug(self):
#         self.publication.save()
#         self.assertTrue(self.publication.slug.startswith("test-publication"))


# class CommentaireModelTests(TestCase):
#     def setUp(self):
#         self.categorie = Categorie.objects.create(nom="Test Category", description="Test", status=True)
#         self.publication = Publication.objects.create(
#             titre="Test Publication",
#             description="Test",
#             image="image/test.jpg",
#             categorie=self.categorie,
#             status=True
#         )
#         self.commentaire = Commentaire.objects.create(
#             publication=self.publication,
#             nom="Test User",
#             email="adebeeb@admin.com",
#             commentaire="This is a test comment.",
#             status=True
#         )

#     def test_commentaire_creation(self):
#         self.assertEqual(self.commentaire.nom, "Test User")
#         self.assertEqual(self.commentaire.publication, self.publication)
#         self.assertTrue(self.commentaire.status)

#     def test_commentaire_str(self):
#         self.assertEqual(str(self.commentaire), "Test User")


# class ReponseCommentaireModelTests(TestCase):
#     def setUp(self):
#         self.categorie = Categorie.objects.create(nom="Test Category", description="Test", status=True)
#         self.publication = Publication.objects.create(
#             titre="Test Publication",
#             description="Test",
#             image="image/test.jpg",
#             categorie=self.categorie,
#             status=True
#         )
#         self.commentaire = Commentaire.objects.create(
#             publication=self.publication,
#             nom="Test User",
#             email="adebeeb@admin.com",
#             commentaire="This is a test comment.",
#             status=True
#         )
#         self.reponse = ReponseCommentaire.objects.create(
#             commentaire=self.commentaire,
#             nom="Responder",
#             email="adebeeb@admin.com",
#             reponse="This is a test response.",
#             status=True
#         )

#     def test_reponse_creation(self):
#         self.assertEqual(self.reponse.nom, "Responder")
#         self.assertEqual(self.reponse.commentaire, self.commentaire)
#         self.assertTrue(self.reponse.status)

#     def test_reponse_str(self):
#         self.assertEqual(str(self.reponse), "Responder")


# # View Tests
# class TimelineViewTests(TestCase):
#     def setUp(self):
#         SiteInfo.objects.create(
#             nom="Test Site",
#             email="adebeeb@admin.com",
#             telephone=123456789,
#             description="Test Description",
#             status=True
#         )

#     def test_timeline_view_status_code(self):
#         response = self.client.get(reverse('timeline'))
#         self.assertEqual(response.status_code, 200)

#     def test_timeline_view_template_used(self):
#         response = self.client.get(reverse('timeline'))
#         self.assertTemplateUsed(response, "pages/list-two-column.html")

#     def test_timeline_view_context(self):
#         response = self.client.get(reverse('timeline'))
#         self.assertIn('publication', response.context)
#         self.assertIn('events_r', response.context)


# class DetailViewTests(TestCase):
#     def setUp(self):
#         self.site_info = SiteInfo.objects.create(
#             nom="Test Site",
#             email="adebeeb@admin.com",
#             telephone=123456789,
#             description="Test Description",
#             status=True
#         )
#         self.categorie = Categorie.objects.create(
#             nom="Test Category",
#             description="Test Description",
#             status=True
#         )
#         self.publication = Publication.objects.create(
#             titre="Test Publication",
#             description="Test Content",
#             categorie=self.categorie,
#             status=True
#         )

#     def test_detail_view_status_code(self):
#         response = self.client.get(reverse('detail', kwargs={'slug': self.publication.slug}))
#         self.assertEqual(response.status_code, 200)

#     def test_detail_view_template_used(self):
#         response = self.client.get(reverse('detail', kwargs={'slug': self.publication.slug}))
#         self.assertTemplateUsed(response, "pages/detail-standart.html")

#     def test_detail_view_context(self):
#         response = self.client.get(reverse('detail', kwargs={'slug': self.publication.slug}))
#         self.assertIn('publication', response.context)
#         self.assertEqual(response.context['publication'], self.publication)


# class IsCommentaireViewTests(TestCase):
#     def setUp(self):
#         self.site_info = SiteInfo.objects.create(
#             nom="Test Site",
#             email="adebeeb@admin.com",
#             telephone=123456789,
#             description="Test Description",
#             status=True
#         )
#         self.categorie = Categorie.objects.create(
#             nom="Test Category",
#             description="Test Description",
#             status=True
#         )
#         self.publication = Publication.objects.create(
#             titre="Test Publication",
#             description="Test Content",
#             categorie=self.categorie,
#             status=True
#         )

#     def test_is_commentaire_view(self):
#         data = {
#             'id': self.publication.id,
#             'nom': 'Test User',
#             'email': "adebeeb@admin.com",
#             'commentaire': 'This is a test comment.',
#         }
#         response = self.client.post(reverse('is_commentaire'), data, content_type='application/json')
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('success', response.json())
#         self.assertTrue(response.json()['success'])
