from django.test import TestCase
from posts.models import Post
from http import HTTPStatus
from model_bakery import baker

class DetailPageTest(TestCase):
    def setUp(self) -> None:
        # self.post = Post.objects.create(
        #     title = "sample post 3",
        #     body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown",
        # )

        self.post = baker.make(Post)

    def test_detailpage_returns_correct_response(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "posts/detail.html")
    
    def test_detailpage_returns_correct_content(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertContains(response, self.post.title)