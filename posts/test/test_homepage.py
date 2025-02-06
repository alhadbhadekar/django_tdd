from django.test import TestCase
from posts.models import Post
from http import HTTPStatus
from model_bakery import baker

# Create your tests here.
class HomePageTest(TestCase):
    def setUp(self) -> None:
        # self.post1 = Post.objects.create(
        #     title="sample post 1",
        #     body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown",
        # )


        # self.post2 = Post.objects.create(
        #     title="sample post 2",
        #     body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown",
        # )

        self.post1 = baker.make(Post)
        self.post2 = baker.make(Post)

    def test_homepage_returns_correct_response(self):
        response = self.client.get("/")

        self.assertTemplateUsed(response, "posts/index.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_returns_post_list(self):
        response = self.client.get("/")

        self.assertContains(response, self.post1.title)
        self.assertContains(response,  self.post2.title)