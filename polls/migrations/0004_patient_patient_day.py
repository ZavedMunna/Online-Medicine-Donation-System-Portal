# Generated by Django 2.2.5 on 2019-11-28 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_patient_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Patient_Day',
            field=models.BooleanField(default=False),
        ),
    ]