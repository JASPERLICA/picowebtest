# Generated by Django 5.0.4 on 2024-11-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fl_app', '0002_remove_fl_test_date_remove_fl_test_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fl_test',
            name='GPI0_24V_SM',
        ),
        migrations.RemoveField(
            model_name='fl_test',
            name='GPI0_BLUE',
        ),
        migrations.RemoveField(
            model_name='fl_test',
            name='GPI0_GREEN',
        ),
        migrations.RemoveField(
            model_name='fl_test',
            name='GPI0_LASER_BTM',
        ),
        migrations.RemoveField(
            model_name='fl_test',
            name='GPI0_LASER_T3D',
        ),
        migrations.RemoveField(
            model_name='fl_test',
            name='GPI0_LASER_TOP',
        ),
        migrations.RemoveField(
            model_name='fl_test',
            name='GPI0_LED1',
        ),
        migrations.RemoveField(
            model_name='fl_test',
            name='GPI0_LED2',
        ),
        migrations.RemoveField(
            model_name='fl_test',
            name='GPI0_LED3',
        ),
        migrations.RemoveField(
            model_name='fl_test',
            name='GPI0_LED4',
        ),
        migrations.RemoveField(
            model_name='fl_test',
            name='GPI0_POES',
        ),
        migrations.RemoveField(
            model_name='fl_test',
            name='GPI0_RED',
        ),
        migrations.AddField(
            model_name='fl_test',
            name='GPIO_24V_SM',
            field=models.CharField(default=None, max_length=16, verbose_name='GPIO_24V_SM'),
        ),
        migrations.AddField(
            model_name='fl_test',
            name='GPIO_BLUE',
            field=models.CharField(default=None, max_length=16, verbose_name='GPIO_BLUE'),
        ),
        migrations.AddField(
            model_name='fl_test',
            name='GPIO_GREEN',
            field=models.CharField(default=None, max_length=16, verbose_name='GPIO_GREEN'),
        ),
        migrations.AddField(
            model_name='fl_test',
            name='GPIO_LASER_BTM',
            field=models.CharField(default=None, max_length=16, verbose_name='GPIO_LASER_BTM'),
        ),
        migrations.AddField(
            model_name='fl_test',
            name='GPIO_LASER_T3D',
            field=models.CharField(default=None, max_length=16, verbose_name='GPIO_LASER_T3D'),
        ),
        migrations.AddField(
            model_name='fl_test',
            name='GPIO_LASER_TOP',
            field=models.CharField(default=None, max_length=16, verbose_name='GPIO_LASER_TOP'),
        ),
        migrations.AddField(
            model_name='fl_test',
            name='GPIO_LED1',
            field=models.CharField(default=None, max_length=16, verbose_name='GPIO_LED1'),
        ),
        migrations.AddField(
            model_name='fl_test',
            name='GPIO_LED2',
            field=models.CharField(default=None, max_length=16, verbose_name='GPIO_LED2'),
        ),
        migrations.AddField(
            model_name='fl_test',
            name='GPIO_LED3',
            field=models.CharField(default=None, max_length=16, verbose_name='GPIO_LED3'),
        ),
        migrations.AddField(
            model_name='fl_test',
            name='GPIO_LED4',
            field=models.CharField(default=None, max_length=16, verbose_name='GPIO_LED4'),
        ),
        migrations.AddField(
            model_name='fl_test',
            name='GPIO_POES',
            field=models.CharField(default=None, max_length=16, verbose_name='GPIO_POES'),
        ),
        migrations.AddField(
            model_name='fl_test',
            name='GPIO_RED',
            field=models.CharField(default=None, max_length=16, verbose_name='GPIO_RED'),
        ),
    ]