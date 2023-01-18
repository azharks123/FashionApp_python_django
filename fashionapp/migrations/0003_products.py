# Generated by Django 4.1.2 on 2023-01-02 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionapp', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=25, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Brand', models.CharField(blank=True, max_length=250, null=True)),
                ('Description', models.CharField(blank=True, max_length=250, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('Categry', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]