# Generated by Django 3.2.3 on 2021-06-07 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0013_alter_classes_class_pub_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='Alldays',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
