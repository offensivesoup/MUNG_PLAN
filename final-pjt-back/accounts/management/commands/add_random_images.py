from django.core.management.base import BaseCommand
from django.core.files import File
from accounts.models import User, Dog
import os
import random

class Command(BaseCommand):
    help = 'Assigns a random image to each user and dog in the database'

    def handle(self, *args, **options):
        # User images
        user_image_dir = 'media/user_images'
        user_image_paths = [os.path.join(user_image_dir, filename) for filename in os.listdir(user_image_dir) if filename.endswith('.png')]

        users = User.objects.all()

        for user in users:
            random_image_path = random.choice(user_image_paths)

            with open(random_image_path, 'rb') as img_file:
                django_file = File(img_file)
                user.profile_img.save(django_file.name, django_file)
                user.save()

        # Dog images
        dog_image_dir = 'media/dog_images'
        dog_image_paths = [os.path.join(dog_image_dir, filename) for filename in os.listdir(dog_image_dir) if filename.endswith('.png')]

        dogs = Dog.objects.all()

        for dog in dogs:
            random_image_path = random.choice(dog_image_paths)

            with open(random_image_path, 'rb') as img_file:
                django_file = File(img_file)
                dog.dog_img.save(django_file.name, django_file)
                dog.save()

        self.stdout.write(self.style.SUCCESS('Successfully assigned random images to all users and dogs'))