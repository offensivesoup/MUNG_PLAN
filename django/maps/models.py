from django.db import models

# Create your models here.
class Map(models.Model):
    facility_name = models.CharField(max_length = 255, blank = True, null = True)
    facility_explain = models.CharField(max_length = 255, blank = True, null = True)
    facility_parking = models.CharField(max_length = 255, blank = True, null = True)
    facility_province = models.CharField(max_length = 255, blank = True, null = True)
    facility_location = models.CharField(max_length = 255, blank = True, null = True)
    facility_lat = models.CharField(max_length = 255, blank = True, null = True)
    facility_lng = models.CharField(max_length = 255, blank = True, null = True)
    facility_new_address = models.CharField(max_length = 255, blank = True, null = True)
    facility_old_address = models.CharField(max_length = 255, blank = True, null = True)
    facility_holiday = models.CharField(max_length = 255, blank = True, null = True)
    facility_category1 = models.CharField(max_length = 255, blank = True, null = True)
    facility_category2 = models.CharField(max_length = 255, blank = True, null = True)
    facility_category3 = models.CharField(max_length = 255, blank = True, null = True)
    facility_link = models.CharField(max_length = 255, blank = True, null = True)
    pass
