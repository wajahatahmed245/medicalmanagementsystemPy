# Generated by Django 2.2.1 on 2019-05-23 00:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0005_visit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='doctor',
            field=models.ForeignKey(on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='visit',
            name='patient',
            field=models.ForeignKey(on_delete='models.CASCADE', to='patient.Patient'),
        ),
    ]
