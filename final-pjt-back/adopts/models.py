from django.db import models

# Create your models here.
class Adopt(models.Model):
  start_date = models.DateField()
  end_date = models.DateField()
  state = models.CharField(max_length = 20)
  img = models.URLField(max_length=200)
  gender = models.CharField(max_length = 1)
  notice = models.CharField(max_length = 200)
  kind = models.CharField(max_length = 50)
  center_name = models.CharField(max_length = 50)
  center_telephone = models.CharField(max_length = 20)
  center_address = models.CharField(max_length = 200)
  
