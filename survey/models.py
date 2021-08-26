from django.db import models
from datetime import date

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Survey(models.Model):
    q_01 = models.CharField(name="Full Name", max_length=40, default="")
    q_02 = models.CharField(name="Nick name", max_length=40, default="")
    q_03 = models.CharField(name="Gender", choices=(
        (1, "Male"), (2, "Female"), (3, "Other")), max_length=10, default="Male")
    q_04 = models.DateField(name="Date of Birth", default=date(1111, 11, 11))
    q_05 = models.CharField(name="Relation to the Family", choices=(
        (1, "Father"),
        (2, "Mother"),
        (3, "Husband"),
        (4, "Wife"),
        (5, "Son"),
        (6, "Daughter"),
        (7, "Brother"),
        (8, "Sister"),
    ), max_length=10, default="Father")
    q_06 = models.CharField(name="Father's Name", max_length=40, default="")
    q_07 = models.CharField(name="Mother's Name", max_length=40, default="")
    q_08 = models.CharField(name="Guardian's Name", max_length=40, default="")
    q_09 = PhoneNumberField(name="Mobile Number")
    q_10 = models.EmailField(name="Email Address",
                             max_length=60, default="")

    def __str__(self):
        return self.q_01
