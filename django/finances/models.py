from django.db import models

# Create your models here.
class Deposit(models.Model):
    category = models.CharField(max_length = 100, blank = True, null = True)
    company_name = models.CharField(max_length = 150, blank = True, null = True)
    product_num = models.CharField(max_length = 150, blank = True, null = True)
    product_name = models.CharField(max_length = 225, blank = True, null = True)
    product_explain = models.CharField(max_length = 225, blank = True, null = True)
    special_explain = models.CharField(max_length = 225, blank = True, null = True)
    special_condition = models.CharField(max_length = 225, blank = True, null = True)
    join_member = models.CharField(max_length = 225, blank = True, null = True)
    limit = models.CharField(max_length = 225, blank = True, null = True)
    save_term = models.CharField(max_length = 5, blank = True, null = True)
    interate_type = models.CharField(max_length = 15, blank = True, null = True)
    interate_rate = models.FloatField(blank = True, null = True)
    maxi_interate_rate = models.FloatField(blank = True, null = True)

class Insurance(models.Model):
    product_name = models.CharField(max_length = 225)
    product_summary = models.CharField(max_length = 225)
    company_name = models.CharField(max_length = 225)
    average_pay = models.CharField(max_length = 225)
    product_explain = models.CharField(max_length = 225)
    join_age = models.CharField(max_length = 225)
    renewal_age = models.CharField(max_length = 225)
    deductible = models.CharField(max_length = 225)
    coverage_ratio = models.CharField(max_length = 225)
    patella_luxation = models.BooleanField()
    skin_disease = models.BooleanField()
    oral_disease = models.BooleanField()
    funeral = models.BooleanField()
    accident_wound = models.BooleanField()
    admission = models.CharField(max_length = 225)
    liability = models.CharField(max_length = 225)
    surgery = models.BooleanField()

