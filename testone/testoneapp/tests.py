from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Actor


class ActorViewTests(TestCase):
    """Tests for actor list and create views."""

    def setUp(self):
        self.list_url = reverse("testoneapp:actor_list")
        self.create_url = reverse("testoneapp:actor_create")
        self.user = User.objects.create_user(
            username="tester", password="password"
        )

    def test_actor_list_view(self):
        Actor.objects.create(
            actorname="Actor One",
            slug="actor-one",
            actor_email="actor@example.com",
            actor_description="An actor",
            author=self.user,
        )

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "actor_list.html")
        self.assertContains(response, "Actor One")

    def test_actor_create_view_authenticated_get(self):
        self.client.login(username="tester", password="password")
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "actor_create.html")

    def test_actor_create_view_authenticated_post(self):
        self.client.login(username="tester", password="password")
        data = {
            "actorname": "New Actor",
            "slug": "new-actor",
            "actor_email": "new@example.com",
            "actor_description": "A new actor",
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.list_url)
        self.assertTrue(Actor.objects.filter(actorname="New Actor").exists())

    def test_actor_create_view_redirects_anonymous_user(self):
        response = self.client.get(self.create_url)
        login_url = reverse("signup:login")
        self.assertRedirects(response, f"{login_url}?next={self.create_url}")

