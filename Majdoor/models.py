from django.db import models
from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ValidationError
from .utils import generate_auto_id, generate_auto_c_id

class Users_db(models.Model):
    c_id = models.CharField(max_length=8, unique=True, editable=False, primary_key=True)
    password = models.CharField(max_length=50, verbose_name='Password', null=True, blank=False,)
    name = models.CharField(max_length=100)
    aadhar_no = models.CharField(max_length=12)

    def __str__(self):
        return  f"{self.c_id}"
    
    def save(self, *args, **kwargs):
        if not self.c_id:
            self.c_id = generate_auto_c_id()
        super().save(*args, **kwargs)
    
class Majdoor_db(models.Model):
    m_id = models.CharField(max_length=8, unique=True, editable=False, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    father_name = models.CharField( max_length=255,  # Maximum length of the field
        verbose_name='Father\'s Name',  # Human-readable name
        blank=True,  # Allows the field to be left blank in forms
        null=True, ) # Allows the field to be nullable in the database
    date_of_birth = models.DateField(  verbose_name='Date of Birth',  # Human-readable name
        null=True,  # Allows the field to be nullable in the database
        blank=True, ) # Allows the field to be left blank in forms
    age=models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    mobile_number = models.CharField(max_length=15)
    permanent_address = models.TextField()
    aadhar_no = models.CharField(max_length=12, unique=True)
    experience_year = models.PositiveIntegerField()
    type_of_works = models.CharField(max_length=255, choices=[('Workers..', 'Workers..'), ('Plumber...', 'Plumber...'), ('car mechanic', 'car mechanic'), ('Electrician', 'Electrician'),('Bike Machanic', 'Bike Machanic'),('Carpenters', 'Carpenters'),('Teachers', 'Teachers'),('IT Professionals', 'IT Professionals')])
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    password = models.CharField( max_length=255,  # Maximum length of the field
        verbose_name='Password',  # Human-readable name
        null=True,  # Do not allow null values in the database
        blank=False,)  # Set your desired default password

    re_password = models.CharField( max_length=255,
        verbose_name='Re-enter Password',
        null=True,
        blank=False,)  # Set your desired default password
  # Set default value as timezone.now

    def save(self, *args, **kwargs):
        if not self.m_id:
            self.m_id = generate_auto_id()
        super().save(*args, **kwargs)

    def age(self):
        today = datetime.today()
        birthdate = self.date_of_birth
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    def clean(self):
        if self.password and self.re_password and self.password != self.re_password:
            raise ValidationError("Passwords do not match. Both fields should be blank.")


    def __str__(self):
        return f"{self.m_id} - {self.first_name} {self.last_name}"
