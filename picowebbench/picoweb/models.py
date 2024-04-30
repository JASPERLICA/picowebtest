from django.db import models

# Create your models here.
class PicoMaster(models.Model):
    id = models.AutoField('id', primary_key=True)

    date = models.DateField('date',default=None)
    time = models.TimeField('time',default=None)
    photoeye    = models.CharField('photoeye',max_length=16)
    computer    = models.CharField('computer',max_length=16)
    poe_sw      = models.CharField('poe_sw',max_length=16)
    channel0    = models.CharField('channel0',max_length=16)
    channel1    = models.CharField('channel1',max_length=16)
    channel2    = models.CharField('channel2',max_length=16)
    channel3    = models.CharField('channel3',max_length=16)
    temper      = models.CharField('temper', default=None,max_length=64)
    humidity    = models.CharField('humidity', default=None,max_length=64)
    version     = models.CharField('version', max_length=64)



    # photoeye    = models.BooleanField('photoeye',default=False)
    # computer    = models.BooleanField('computer',default=False)
    # poe_sw      = models.BooleanField('poe_sw',default=False)