# Generated by Django 3.2.5 on 2022-04-05 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_rename_forum_ad'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]
