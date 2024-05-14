from django.db import models

# Create your models here.
class Market(models.Model):
  item_name = models.CharField(max_length = 200)
  item_img  = models.URLField(max_length = 255)
  item_low_price = models.IntegerField()
  item_high_price = models.IntegerField()
  item_seller = models.CharField(max_length = 255)
  item_brand = models.CharField(max_length = 255)
  item_maker = models.CharField(max_length = 255)
  item_link = models.URLField(max_length = 255)
  item_seller = models.CharField(max_length = 200)
  item_type = models.CharField(max_length = 200)
  item_cateogry_1 = models.CharField(max_length = 200)
  item_cateogry_2 = models.CharField(max_length = 200)
  item_cateogry_3 = models.CharField(max_length = 200)