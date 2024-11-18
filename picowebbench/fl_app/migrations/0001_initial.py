# Generated by Django 5.0.4 on 2024-11-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fl_test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('date', models.DateField(default=None, verbose_name='date')),
                ('time', models.TimeField(default=None, verbose_name='time')),
                ('FL_IP', models.CharField(max_length=16, verbose_name='FL_IP')),
                ('MAC_ADDRESS', models.CharField(max_length=16, verbose_name='MAC_ADDRESS')),
                ('VERSION', models.CharField(max_length=16, verbose_name='VERSION')),
                ('GPI0_RED', models.CharField(max_length=16, verbose_name='GPI0_RED')),
                ('GPI0_GREEN', models.CharField(max_length=16, verbose_name='GPI0_GREEN')),
                ('GPI0_BLUE', models.CharField(max_length=16, verbose_name='GPI0_BLUE')),
                ('GPI0_LED1', models.CharField(max_length=16, verbose_name='GPI0_LED1')),
                ('GPI0_LED2', models.CharField(max_length=16, verbose_name='GPI0_LED2')),
                ('GPI0_LED3', models.CharField(max_length=16, verbose_name='GPI0_LED3')),
                ('GPI0_LED4', models.CharField(max_length=16, verbose_name='GPI0_LED4')),
                ('GPI0_LASER_TOP', models.CharField(max_length=16, verbose_name='GPI0_LASER_TOP')),
                ('GPI0_LASER_BTM', models.CharField(max_length=16, verbose_name='GPI0_LASER_BTM')),
                ('GPI0_LASER_T3D', models.CharField(max_length=16, verbose_name='GPI0_LASER_T3D')),
                ('GPI0_24V_SM', models.CharField(max_length=16, verbose_name='GPI0_24V_SM')),
                ('TOP_VALUE', models.CharField(max_length=2048, verbose_name='TOP_VALUE')),
                ('BTM_VALUE', models.CharField(max_length=2048, verbose_name='BTM_VALUE')),
            ],
        ),
    ]
