# Generated by Django 5.0.4 on 2024-11-18 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fl_app', '0006_laser_data_voltage_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='voltage_data',
            name='voltage5v',
            field=models.CharField(default=None, max_length=32, verbose_name='voltage5v'),
        ),
    ]