# Generated by Django 3.2.3 on 2021-05-31 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_userlinks_short_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Ссылки', 'verbose_name_plural': 'Ссылки'},
        ),
        migrations.AlterField(
            model_name='person',
            name='short_link',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.DeleteModel(
            name='Userlinks',
        ),
    ]
