# Generated by Django 3.2.3 on 2021-05-31 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlinks',
            name='short_link',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
