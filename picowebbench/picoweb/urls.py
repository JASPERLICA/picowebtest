from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('write', views.write, name='write'),
    path('show', views.show, name='show'),
    path('table', views.table_cmd, name='table_cmd'),
    path('fl', views.fl, name='fl'),
    path('fldata', views.fldata, name='fldata'),

    # path('signup',views.signup,name='signup'),
    # path('signin',views.signin,name='signin'),
    # path('signout',views.signout,name='signout'),

    path('all_on',views.all_on,name='all_on'),
    path('all_off',views.all_off,name='all_off'),
    path('reset_poe',views.reset_poe,name='reset_poe'),
    path('reset_master',views.reset_master,name='reset_master'),

    path('channel1_on',views.channel1_on,name='channel1_on'),
    path('channel2_on',views.channel2_on,name='channel2_on'),
    path('channel3_on',views.channel3_on,name='channel3_on'),
    path('channel0_on',views.channel0_on,name='channel0_on'),

    path('channel1_off',views.channel1_off,name='channel1_off'),
    path('channel2_off',views.channel2_off,name='channel2_off'),
    path('channel3_off',views.channel3_off,name='channel3_off'),
    path('channel0_off',views.channel0_off,name='channel0_off'),

    path('update_main',views.update_main,name='update_main'),
    path('led_brighter',views.led_brighter,name='led_brighter'),
    path('led_dim',views.led_dim,name='led_dim'),

    # re_path(r'^signup', views.signup,name='signup')
]

