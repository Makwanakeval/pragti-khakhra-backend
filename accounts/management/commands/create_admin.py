from django.core.management.base import BaseCommand
from accounts.models import CustomUser
import os

class Command(BaseCommand):
    help = 'Creates a superuser automatically from environment variables if one does not exist'

    def handle(self, *args, **options):
        username = os.environ.get('ADMIN_USERNAME')
        password = os.environ.get('ADMIN_PASSWORD')
        mobile = os.environ.get('ADMIN_MOBILE')
        email = os.environ.get('ADMIN_EMAIL', '')

        if not username or not password or not mobile:
            self.stdout.write(self.style.WARNING('ADMIN_USERNAME, ADMIN_PASSWORD, or ADMIN_MOBILE not set — skipping superuser creation.'))
            return

        if CustomUser.objects.filter(username=username).exists():
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" already exists — skipping.'))
            return

        CustomUser.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            mobile_number=mobile,
        )
        self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully!'))