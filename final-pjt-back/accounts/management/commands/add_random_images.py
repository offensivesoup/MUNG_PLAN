import os
import random
import glob
from django.core.management.base import BaseCommand
from accounts.models import User, Dog

class Command(BaseCommand):
    help = 'Adds random images to User and Dog models'

    def handle(self, *args, **options):
        self.add_random_images()

    def add_random_images(self):
        # User images
        user_image_dir = 'accounts/static/accounts/user_images'
        user_image_urls = glob.glob(os.path.join(user_image_dir, '*.png'))

        users = User.objects.all()

        for user in users:
            random_image_url = random.choice(user_image_urls)
            user.profile_img = 'static/user_images/' + os.path.basename(random_image_url)
            user.save()

        # Dog images
        dog_image_dir = 'accounts/static/accounts/dog_images'
        dog_image_urls = glob.glob(os.path.join(dog_image_dir, '*.png'))

        dogs = Dog.objects.all()

        for dog in dogs:
            random_image_url = random.choice(dog_image_urls)
            dog.dog_img = 'static/dog_images/' + os.path.basename(random_image_url)
            dog.save()