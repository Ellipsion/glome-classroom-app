# Generated by Django 3.2.3 on 2021-05-30 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0007_alter_classes_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='class_day',
            field=models.CharField(choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday'), ('7', 'Sunday')], max_length=1),
        ),
    ]