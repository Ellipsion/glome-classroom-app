# Generated by Django 3.2.3 on 2021-05-28 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0006_classes_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classes', to=settings.AUTH_USER_MODEL),
        ),
    ]
