# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np

from . import models
import socket

web_port = 18008
con_flag = False
# http://127.0.0.1:8000/all_off
# TERMINATION_CHAR = '\n'

# try :
#     #localhost_to_backend = socket.gethostname() 
#     #print(localhost_to_backend)
#     localhost_to_backend = "192.168.30.111"
#     to_backend_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     to_backend_sock.connect((localhost_to_backend, web_port))
#     print("socket estabished")
#     con_flag = True
# except:
#      print("socket failed to estabish")
#      pass


def index(request):
    return HttpResponse('this is first page')

def fl(request):
    # return HttpResponse('this is test for fl')
    data = models.Fl_test.objects.all()
    return render(request, 'fl_test.html', {'data_list':data})

# def check(request,id):
#     print("it is in check")
#     # return HttpResponse('this is test for fl')
#     # id = request.GET.get("id")
#     # print(f"id is {id}")
#     # data = models.Fl_test.objects.get(ID=id)
#     data = models.Fl_test.objects.filter(ID = id).all()
#     print(data)
#     # data = models.Fl_voltage.objects.get(ID=id)
#     # data = models.Fl_test.objects.all()
#     return render(request, 'fl_test.html', {'data_list':data})

def check(request,id):
    print("it is in check")
    data1 = models.Fl_test.objects.filter(ID = id).all()
    data2 = models.Voltage_data.objects.filter(ID = 1).all()

    # data3 = models.Laser_data.objects.filter(ID = 1).only("TOP_VALUE")

    values = models.Laser_data.objects.filter(ID = 1)
    ids = ""
    mac =""
    top = ""
    btm = ""

    for i in values:
        ids = ids + " " + str(i.ID)     
        mac = mac + " " + i.MAC_ADDRESS    
        top = top + " " + str(i.TOP_VALUE)  
        btm = btm + " " + str(i.BTM_VALUE) 


    data0 = btm.split(",")
    data3 = [ int(x) for x in data0 ]
    print(f"this is bottom data {data3}")

    bottom_y = data3
    bottom_x = []

    for n in range(len(data3)):
        bottom_x.append(n);
    print(bottom_x)
        
    data5 = top.split(",")
    data6 = [ int(x) for x in data5 ]
    print(f"top data {data6}")

    top_y = data6
    top_x = []

    for n in range(len(data6)):
        top_x.append(n);
    print(top_x)

    plt.plot(top_x, top_y, color='red',label="top")
    # plt.plot(bottom_x, bottom_y, color='green',label="btm")
    plt.tick_params(axis='x',colors='blue')
    plt.tick_params(axis='y',colors='red')

    plt.xlabel('list')
    plt.ylabel('AC value')
    plt.legend()
    
    # plt.savefig('./fl_app/templates/jasper0.png',format="png")
    plt.savefig('./fl_app/static/images/jasper0.png',format="png")
    # plt.show()

    plt.plot(bottom_x, bottom_y, color='green',label="btm")
    plt.tick_params(axis='x',colors='blue')
    plt.tick_params(axis='y',colors='red')

    plt.xlabel('list')
    plt.ylabel('AC value')
    plt.legend()
    
    # plt.savefig('./fl_app/templates/jasper0.png',format="png")
    plt.savefig('./fl_app/static/images/jasper1.png',format="png")
    # plt.show()

    # render(request, 'data_table.html', {'data_list1':data1})
    return render(request, 'data_table.html', {'data_list1':data1,'data_list2':data2})

def test(request):
    global on_flag
    if con_flag == True:
        command = "START_TEST"
        try:    
            to_backend_sock.send(command.encode())
            print(f"send to {command}  backend ")
        except:
            print("command failed to send out")
            pass
    data_all = models.Fl_test.objects.all()
    length= data_all.count()
    if length >= 11:
        data = data_all[length-10:length]
    else:
        data = data_all
    return render(request, 'fl_test.html', {'data_list':data})