from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import Laboratorio

# Create your tests here.

class SimpleLabTests(SimpleTestCase):
    databases = "__all__"
    
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/laboratorios/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "laboratorio/index.html")

    def test_template_content(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, "<h1>Informacion de Laboratorios</h1>")
        self.assertNotContains(response, "No es la pagina")

class LaboratorioTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(
            id=123, 
            name="Laboratorio Prueba", 
            city="Ciudad Prueba", 
            country="Pais Prueba"
            )
    
    def test_model_content(self):
        self.assertEqual(self.laboratorio.id, 123)
        self.assertEqual(self.laboratorio.name, "Laboratorio Prueba")
        self.assertEqual(self.laboratorio.city, "Ciudad Prueba")
        self.assertEqual(self.laboratorio.country, "Pais Prueba")