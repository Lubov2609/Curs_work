from django.test import TestCase

# Create your tests here.
from django.test import Client
from django.urls import reverse



from blog.models import Reviews, Contact


class TurModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Reviews.objects.create(name='qwert',phone='12345678910')

    def text_first_name_ladel(self):
        reviews=Reviews.objects.get(id=1)
        field_label =reviews._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_first_name_max_length(self):
        reviews =Reviews.objects.get(id=1)
        max_length = reviews._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)



class TestStudentContactForm(TestCase):
    def test_can_send_message(self):
        data = {
            "first_name": "Juliana",
            "last_name": " Crain",
            "message": "Would love to talk about Philip K. Dick",
        }
        response = self.client.get("/contact/")
        self.assertTemplateUsed(response, "library/contact_form.html")
        self.assertContains(response,"first_name")
        self.assertContains(response, "last_name")
        response = self.client.post("/contact/", data=data)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertRedirects(response, "/thanks/")