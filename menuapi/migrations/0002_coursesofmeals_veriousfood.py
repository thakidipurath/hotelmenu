# Generated by Django 4.0.1 on 2022-05-13 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesofmeals',
            name='veriousfood',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
