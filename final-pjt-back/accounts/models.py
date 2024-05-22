import os
import random
import glob
from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.conf import settings
from django.db import models
from allauth.account.adapter import DefaultAccountAdapter

class User(AbstractUser):
    nickname = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True, null=True)
    profile_img = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    def __str__(self):
        return self.username 
    
    def save(self, *args, **kwargs):
        if not self.profile_img:
            self.profile_img = self.get_random_profile_img()
        super().save(*args, **kwargs)

    @staticmethod
    def get_random_profile_img():
        user_image_dir = 'accounts/static/accounts/user_images'
        user_image_urls = glob.glob(os.path.join(user_image_dir, '*.png'))
        random_image_url = random.choice(user_image_urls)
        return 'static/user_images/' + os.path.basename(random_image_url)

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        from allauth.account.utils import user_email, user_field, user_username

        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        phone_number = data.get('phone_number')
        address = data.get('address')
        birth_date = data.get('birth_date')
        profile_img = data.get('profile_img')
        # nickname 
        nickname = data.get("nickname")
        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if nickname:
            user_field(user, "nickname", nickname)
        if phone_number:
            user_field(user, "phone_number", phone_number)
        if address:
            user_field(user, "address", address)
        if birth_date:
            user_field(user, "birth_date", birth_date)
        # 프로필 이미지 설정
        if not profile_img:
            user.profile_img = User.get_random_profile_img()
        else:
            user.profile_img = profile_img
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user
    
GENDERS = (('M', '남성(Man)'),('W', '여성(Woman)'),('Q', '중성'))
TYPES   = ((1, '말티즈'),(2, '푸들'),(3, '포메라니안'),(4, '시츄'),(5, '비숑프리제'),(6, '요크셔테리어'),(7, '진도견'),(8, '치와와'),(9, '스피츠'),(10, '닥스훈트'),(11, '리트리버'),(12, '기타'))

class Dog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    name = models.CharField(max_length = 10)
    age = models.IntegerField()
    gender = models.CharField(max_length = 1, choices = GENDERS)
    birth_date = models.DateField()
    Type = models.CharField(max_length = 10, choices = TYPES)
    dog_img = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.dog_img:
            self.dog_img = self.get_random_dog_img()
        super().save(*args, **kwargs)

    @staticmethod
    def get_random_dog_img():
        dog_image_dir = 'accounts/static/accounts/dog_images'
        dog_image_urls = glob.glob(os.path.join(dog_image_dir, '*.png'))
        random_image_url = random.choice(dog_image_urls)
        return 'static/dog_images/' + os.path.basename(random_image_url)