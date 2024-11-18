from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fl', views.fl, name='fl'),
    path('test',views.test,name='test'),
    path('check/<int:id>/', views.check, name='check'),
    # path('fldata', views.fldata, name='fldata'),
]