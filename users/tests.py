from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.core import mail
from django.contrib.auth.models import User

class EmailTest(APITestCase):
    def test_send_mail(self):
        with self.settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'):

            email_test_url = reverse('list-users')
            user_data = {'email': 'username_test@gmail.com', 'username': 'username_test', 'password': '123456'}
            
            create_user_res = self.client.post(email_test_url, user_data, format='json')
            self.assertEquals(create_user_res.status_code, status.HTTP_201_CREATED)

            username = 'username_test'
            email = 'username_test@gmail.com'
            
            self.assertEquals(
                mail.outbox[0].subject, f'Your account was created!')

            self.assertEquals(
                mail.outbox[0].body, f'Hello, {username}! \n Welcome to The Silver Wall! \n Now you can login with your email ({email}) and your password to post a lot in our Wall! \n Best regards, The Silver Wall.')


class CreateUserTest(APITestCase):
    def test_create_user(self):

        create_user_url = reverse('list-users')
        user_data = {'email': 'username_test@gmail.com', 'username': 'username_test', 'password': '123456'}

        res = self.client.post(create_user_url, user_data, format='json')

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'username_test')
        self.assertEqual(User.objects.get().email, 'username_test@gmail.com')
