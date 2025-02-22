from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import UserRegisterationForm
from django.contrib.auth import get_user_model

# Create your tests here.


class AccountCreationTest(TestCase):

    def setUp(self) -> None:
        self.form_class = UserRegisterationForm

    def test_signup_page_exists(self):
        response = self.client.get(reverse('signup_page'))

        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed('accounts/register.html')
        self.assertContains(response, "Create your account today")

    def test_signup_form_works_correctly(self):

        

        self.assertTrue(issubclass(self.form_class, UserCreationForm))
        self.assertTrue('email' in self.form_class.Meta.fields)
        self.assertTrue('username' in self.form_class.Meta.fields)
        self.assertTrue('password1' in self.form_class.Meta.fields)
        self.assertTrue('password2' in self.form_class.Meta.fields)

        sample_data = {
            "email": "testuser@app.com",
            "username": "testuser",
            "password1": "p4ssword134###",
            "password2": "p4ssword134###",
        }

        form = self.form_class(sample_data)

        self.assertTrue(form)

    def test_signup_form_creates_user_in_db(self):
        user = {
            "email": "testuser1@app.com",
            "username": "testuser1",
            "password1": "p4ssword134###",
            "password2": "p4ssword134###", 
        }

        form = self.form_class(user)

        if form.is_valid():
            form.save()
        
        User = get_user_model()
        
        self.assertEqual(User.objects.count(), 1)
