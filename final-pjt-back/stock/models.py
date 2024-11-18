from django.db import models

# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)

class ChartPeriod(models.TextChoices):
    DAY = 'D', '일'
    WEEK = 'W', '주'
    MONTH = 'M', '월'
    YEAR = 'Y', '년'

class ThemeChart(models.Model):
    f_price = models.DecimalField(max_digits=2)
    period = models.CharField(
        max_length=1,
        choices=ChartPeriod.choices,
        default=ChartPeriod.DAY
    )
    
