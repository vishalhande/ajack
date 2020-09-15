from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User


def phone_validation(phone):
    if len(phone) != 10:   #
        raise ValidationError('This is not a valid phone')

def pincode_validation(pincode):
    if len(phone) != 6:   #
        raise ValidationError('This is not a valid pincode')
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.BigIntegerField('phone',validators=[phone_validation])
    address = models.CharField('address',max_length=300)
    city = models.CharField('city',max_length=50)
    state = models.CharField('state',max_length=50)
    country = models.CharField('country',max_length=50)
    pincode = models.IntegerField('pincode',validators=[pincode_validation])

class Content(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=300)
    summary = models.CharField(max_length=60)
    document = models.FileField(upload_to='pdf')

class Categories(models.Model):
    id = models.IntegerField('id',primary_key=True)
    conref = models.ForeignKey(Content ,on_delete=models.CASCADE,related_name='catref')

