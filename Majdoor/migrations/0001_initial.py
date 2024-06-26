# Generated by Django 5.0.2 on 2024-04-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Majdoor_db',
            fields=[
                ('m_id', models.CharField(editable=False, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('father_name', models.CharField(blank=True, max_length=255, null=True, verbose_name="Father's Name")),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('mobile_number', models.CharField(max_length=15)),
                ('permanent_address', models.TextField()),
                ('aadhar_no', models.CharField(max_length=12, unique=True)),
                ('experience_year', models.PositiveIntegerField()),
                ('type_of_works', models.CharField(choices=[('Workers..', 'Workers..'), ('Plumber...', 'Plumber...'), ('car mechanic', 'car mechanic'), ('Electrician', 'Electrician'), ('Bike Machanic', 'Bike Machanic'), ('Carpenters', 'Carpenters'), ('Teachers', 'Teachers'), ('IT Professionals', 'IT Professionals')], max_length=255)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('password', models.CharField(max_length=255, null=True, verbose_name='Password')),
                ('re_password', models.CharField(max_length=255, null=True, verbose_name='Re-enter Password')),
            ],
        ),
        migrations.CreateModel(
            name='Users_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('aadhar_no', models.CharField(max_length=12)),
            ],
        ),
    ]
