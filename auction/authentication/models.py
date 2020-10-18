from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileDetails(models.Model):
    user_type = models.SmallIntegerField(default=1)     # please check DEFAULT_USER_TYPE in config.py file
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    company_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    address_lane_1 = models.TextField()
    address_lane_2 = models.TextField()
    city = models.CharField(max_length=255)
    postal_zip = models.IntegerField()
    country = models.SmallIntegerField(default=0)
    state = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_user_type'
