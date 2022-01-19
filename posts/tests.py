from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post



class GetPostsTests(APITestCase):
    def test_list_posts(self):

        posts_list_url = reverse('list-posts')
        res = self.client.get(posts_list_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
class CreatePostsTest(APITestCase):
    def test_visitors_cannot_post(self):
        
        posts_list_url = reverse('list-posts')
        post_data = {'title': 'test', 'body': 'test body'}
        res = self.client.post(posts_list_url, post_data, format='json')
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_users_can_post(self):
        users_url = reverse('list-users')
        user_data = {'email': 'username_test@gmail.com', 'username': 'username_test', 'password': '123456'}
        
        created_res = self.client.post(users_url, user_data, format='json')
        
        self.assertEqual(created_res.status_code, status.HTTP_201_CREATED)

        get_token_url = reverse('api-token-auth')
        token_data = {'username': 'username_test', 'password': '123456'}
        token_res = self.client.post(get_token_url, token_data, format='json')
        
        self.assertEqual(token_res.status_code, status.HTTP_200_OK)
        
        user_token = token_res.data['token']
        posts_url = reverse('list-posts')
        post_data = {'title': 'test', 'body': 'test body'}
        post_res = self.client.post(posts_url, post_data, HTTP_AUTHORIZATION=f'Token {user_token}')
        
        self.assertEqual(post_res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'test')
        self.assertEqual(Post.objects.get().body, 'test body')

class MyPostsTest(APITestCase):
    def test_list_my_posts(self):
        users_url = reverse('list-users')
        user_data = {'email': 'username_test@gmail.com', 'username': 'username_test', 'password': '123456'}
        self.client.post(users_url, user_data, format='json')
        
        get_token_url = reverse('api-token-auth')
        token_data = {'username': 'username_test', 'password': '123456'}
        token_res = self.client.post(get_token_url, token_data, format='json')
                
        user_token = token_res.data['token']
        posts_url = reverse('list-posts')
        post_data = {'title': 'test', 'body': 'test body'}
        post_res = self.client.post(posts_url, post_data, HTTP_AUTHORIZATION=f'Token {user_token}')
        
        self.assertEqual(post_res.status_code, status.HTTP_201_CREATED)
        
        my_posts_url = reverse('my-posts')
        my_posts_res = self.client.get(my_posts_url, HTTP_AUTHORIZATION=f'Token {user_token}')
        
        self.assertEqual(my_posts_res.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'test')
        self.assertEqual(Post.objects.get().body, 'test body')
