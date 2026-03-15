from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = "Creates a superuser if none exists, using environment variables"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write("Superuser already exists, skipping.")
            return

        username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if not password:
            self.stdout.write("DJANGO_SUPERUSER_PASSWORD not set, skipping.")
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        self.stdout.write(f"Superuser '{username}' created successfully.")