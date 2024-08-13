from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        email = 'admin@example.net'
        password = 'admin1'

        try:
            user = User.objects.get(email=email)
            self.stdout.write(f'User with email {email} already exists. Updating...')
        except User.DoesNotExist:
            user = User(email=email)
            self.stdout.write(f'Creating new user with email {email}')

        user.first_name = 'Aleks'
        user.last_name = 'Podlesnov'
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        self.stdout.write(self.style.SUCCESS(f'Superuser {email} has been created/updated successfully.'))