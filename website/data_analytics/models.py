from django.db import models

# Create your models here.

data_choices = (
    ('blank',''),
    ('int','Int'),
    ('sex','Sex'),
    ('datetime','DateTime'),
)

class DropDown(models.Model):
    data_drop = models.CharField(max_length=15,choices=data_choices, default='int')
