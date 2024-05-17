from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from allauth.account.adapter import DefaultAccountAdapter


class User(AbstractUser):
    nickname = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True, null=True)
    profile_img = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    def __str__(self):
        return self.username
    

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
        profile_img = data.get('profile_img')
        birth_date = data.get('birth_date')
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
        if profile_img:
            user.profile_img = profile_img
        if birth_date:
            user.birth_date = birth_date
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user
    
GENDERS = (('M', '남성(Man)'),('W', '여성(Woman)'),('X', '중성'))
TYPES   = ((1, '말티즈'),(2, '푸들'),(3, '포메라니안'),(4, '시츄'),(5, '비숑프리제'),(6, '요크셔테리어'),(7, '진도견'),(8, '치와와'),(9, '스피츠'),(10, '닥스훈트'),(11, '리트리버'),(12, '기타'))
class Dog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    name = models.CharField(max_length = 10)
    age = models.IntegerField()
    gender = models.CharField(max_length = 1, choices = GENDERS)
    birth_date = models.DateField()
    Type = models.CharField(max_length = 10, choices = TYPES)
    