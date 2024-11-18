from django.db import models

# Create your models here.
class Fl_test(models.Model):
    ID              = models.AutoField('ID', default=None,primary_key=True)
    DATE            = models.DateField('DATE',default=None)
    TIME            = models.TimeField('TIME',default=None)
    FL_IP           = models.CharField('FL_IP',default=None,max_length=32)
    MAC_ADDRESS     = models.CharField('MAC_ADDRESS',default=None,max_length=32)
    VERSION         = models.CharField('VERSION',default=None,max_length=32)
    GPIO_RED        = models.CharField('GPIO_RED',default=None,max_length=32)
    GPIO_GREEN      = models.CharField('GPIO_GREEN',default=None,max_length=32)
    GPIO_BLUE       = models.CharField('GPIO_BLUE',default=None,max_length=32)
    GPIO_LED1       = models.CharField('GPIO_LED1',default=None,max_length=32)
    GPIO_LED2       = models.CharField('GPIO_LED2',default=None,max_length=32)
    GPIO_LED3       = models.CharField('GPIO_LED3',default=None,max_length=32)
    GPIO_LED4       = models.CharField('GPIO_LED4',default=None,max_length=32)
    GPIO_POES       = models.CharField('GPIO_POES',default=None,max_length=32)
    GPIO_LASER_TOP  = models.CharField('GPIO_LASER_TOP',default=None,max_length=32)
    GPIO_LASER_BTM  = models.CharField('GPIO_LASER_BTM',default=None,max_length=32)
    GPIO_LASER_T3D  = models.CharField('GPIO_LASER_T3D',default=None,max_length=32)
    GPIO_24V_SM     = models.CharField('GPIO_24V_SM',default=None,max_length=32)
    TOP_VALUE       = models.CharField('TOP_VALUE',default=None,max_length=2048)
    BTM_VALUE       = models.CharField('BTM_VALUE',default=None,max_length=2048)


class Voltage_data(models.Model):
    ID              = models.AutoField('ID', default=None,primary_key=True)
    DATE            = models.DateField('DATE',default=None)
    TIME            = models.TimeField('TIME',default=None)
    MAC_ADDRESS     = models.CharField('MAC_ADDRESS',default=None,max_length=32)
    voltage5v      = models.CharField('voltage5v',default=None,max_length=32)
    voltage3v3      = models.CharField('voltage3v3',default=None,max_length=32)
    voltage3d       = models.CharField('voltage3d',default=None,max_length=32)
    voltage24s      = models.CharField('voltage24s',default=None,max_length=32)
    voltage48       = models.CharField('voltage48',default=None,max_length=32)
    voltage24lower  = models.CharField('voltage24lower',default=None,max_length=32)
    voltage24upper  = models.CharField('voltage24upper',default=None,max_length=32)

class Laser_data(models.Model):
    ID              = models.AutoField('ID', default=None,primary_key=True)
    DATE            = models.DateField('DATE',default=None)
    TIME            = models.TimeField('TIME',default=None)
    MAC_ADDRESS     = models.CharField('MAC_ADDRESS',default=None,max_length=32)
    TOP_VALUE       = models.CharField('TOP_VALUE',default=None,max_length=2048)
    BTM_VALUE       = models.CharField('BTM_VALUE',default=None,max_length=2048)




