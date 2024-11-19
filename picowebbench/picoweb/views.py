from django.shortcuts import render,redirect
from django.http import HttpResponse

from . import models
import socket

web_port = 18001
con_flag = False

# http://127.0.0.1:8000/all_off
# TERMINATION_CHAR = '\n'

# try :
#     #localhost_to_backend = socket.gethostname() 
#     #print(localhost_to_backend)
#     localhost_to_backend = "192.168.30.1"
#     to_backend_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     to_backend_sock.connect((localhost_to_backend, web_port))
#     print("socket estabished")
#     con_flag = True
# except:
#      print("socket failed to estabish")
#      pass


# def index(request):
#     return HttpResponse('this is first page')



# Create your views here.
# def write_in(request):
#     if request.method == 'GET':
#         return render(request, 'write.html')


# def show(request):
#     data = models.Manager.objects.all()
#     return render(request, 'master_test.html', {'data_list':data})


def index(request):
    data_all = models.PicoMaster.objects.all()
    length= data_all.count()
    data = data_all[length-10:length]
    return render(request, 'master_test.html', {'data_list':data})


def table_cmd(request):
    data = models.Addnewtablefromcmd.objects.all()
    return render(request, 'show_table_from_cmd.html', {'data_list':data})

def fldata(request):
    return HttpResponse('this is test for Fl_data')
    # data = models.FLtester.objects.all()
    # return render(request, 'fl_data.html', {'data_list':data})


def write(request):
    if request.method == "GET":
        return render(request, 'write.html')

    elif request.method == "POST":
        id = request.POST.get('id')
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')

        models.Manager.objects.create(id=id, name=name, date=date, time=time)
        # return render(request, 'write.html')
        return redirect('/show')

def all_on(request):
    global on_flag
    if con_flag == True:
        command = "all_on" 
        try:    
            to_backend_sock.send(command.encode())
            print(f"send to {command}  backend ")
        except:
            print("command failed to send out")
            pass
    data_all = models.PicoMaster.objects.all()
    length= data_all.count()
    data = data_all[length-10:length]
    return render(request, 'master_test.html', {'data_list':data})

def all_off(request):
    global on_flag
    if con_flag == True:
        command = "all_off"    
        try:    
            to_backend_sock.send(command.encode())
            print(f"send to {command}  backend ")
        except:
            print("command failed to send out")
            pass
    data_all = models.PicoMaster.objects.all()
    length= data_all.count()
    data = data_all[length-10:length]
    return render(request, 'master_test.html', {'data_list':data})

def reset_poe(request):
    global on_flag
    if con_flag == True:
        command = "poe_reset"     
        try:    
            to_backend_sock.send(command.encode())
            print(f"send to {command}  backend ")
        except:
            print("command failed to send out")
            pass
    return render(request, 'master_test.html')

def reset_nuc(request):
    global on_flag
    if con_flag == True:
        command = "nuc_reset"     
        try:    
            to_backend_sock.send(command.encode())
            print(f"send to {command}  backend ")
        except:
            print("command failed to send out")
            pass
    return render(request, 'master_test.html')

def reset_master(request):
    global on_flag
    if con_flag == True:
        command = "reset"     
        try:    
            to_backend_sock.send(command.encode())
            print(f"send to {command}  backend ")
        except:
            print("command failed to send out")
            pass
    return render(request, 'master_test.html')


def channel0_on(request):
    global on_flag
    if con_flag == True:
        command = "channel0_on" 
        try:    
            to_backend_sock.send(command.encode())
            print(f"send to {command}  backend ")
        except:
            print("command failed to send out")
            pass
    data_all = models.PicoMaster.objects.all()
    length= data_all.count()
    data = data_all[length-10:length]
    return render(request, 'master_test.html', {'data_list':data})

def channel0_off(request):
    global on_flag
    if con_flag == True:
        command = "channel0_off"    
        try:    
            to_backend_sock.send(command.encode())
            print(f"send to {command}  backend ")
        except:
            print("command failed to send out")
            pass
    data_all = models.PicoMaster.objects.all()
    length= data_all.count()
    data = data_all[length-10:length]
    return render(request, 'master_test.html', {'data_list':data})


def channel1_on(request):
    global on_flag
    if con_flag == True:
        command = "channel1_on" 
        try:    
            to_backend_sock.send(command.encode())
            print(f"send to {command}  backend ")
        except:
            print("command failed to send out")
            pass
    data_all = models.PicoMaster.objects.all()
    length= data_all.count()
    data = data_all[length-10:length]
    return render(request, 'master_test.html', {'data_list':data})

def channel1_off(request):
    global on_flag
    if con_flag == True:
        command = "channel1_off"    
        try:    
            to_backend_sock.send(command.encode())
            print(f"send to {command}  backend ")
        except:
            print("command failed to send out")
            pass
    data_all = models.PicoMaster.objects.all()
    length= data_all.count()
    data = data_all[length-10:length]
    return render(request, 'master_test.html', {'data_list':data})


def channel2_on(request):
    global on_flag
    if con_flag == True:
        command = "channel2_on" 
        try:    
            to_backend_sock.send(command.encode())
            print(f"send to {command}  backend ")
        except:
            print("command failed to send out")
            pass
    data_all = models.PicoMaster.objects.all()
    length= data_all.count()
    data = data_all[length-10:length]
    return render(request, 'master_test.html', {'data_list':data})

def channel2_off(request):
    global on_flag
    if con_flag == True:
        command = "channel2_off"    
        try:    
            to_backend_sock.send(command.encode())
            print(f"send to {command}  backend ")
        except:
            print("command failed to send out")
            pass
    data_all = models.PicoMaster.objects.all()
    length= data_all.count()
    data = data_all[length-10:length]
    return render(request, 'master_test.html', {'data_list':data})


def channel3_on(request):
    global on_flag
    if con_flag == True:
        command = "channel3_on" 
        try:    
            to_backend_sock.send(command.encode())
            print(f"send to {command}  backend ")
        except:
            print("command failed to send out")
            pass
    data_all = models.PicoMaster.objects.all()
    length= data_all.count()
    data = data_all[length-10:length]
    return render(request, 'master_test.html', {'data_list':data})

def channel3_off(request):
    global on_flag
    if con_flag == True:
        command = "channel3_off"    
        try:    
            to_backend_sock.send(command.encode())
            print(f"send to {command}  backend ")
        except:
            print("command failed to send out")
            pass
    data_all = models.PicoMaster.objects.all()
    length= data_all.count()
    data = data_all[length-10:length]
    return render(request, 'master_test.html', {'data_list':data})



def update_main(request):
    global on_flag
    if con_flag == True:
        command = "update_main"    
        try:    
            to_backend_sock.send(command.encode())
            print(f"send to {command}  backend ")
        except:
            print("command failed to send out")
            pass
    data_all = models.PicoMaster.objects.all()
    length= data_all.count()
    data = data_all[length-10:length]
    return render(request, 'master_test.html', {'data_list':data})


def led_brighter(request):
    global on_flag
    if con_flag == True:
        command = "led_brighter"    
        try:    
            to_backend_sock.send(command.encode())
            print(f"send to {command}  backend ")
        except:
            print("command failed to send out")
            pass
    data_all = models.PicoMaster.objects.all()
    length= data_all.count()
    data = data_all[length-10:length]
    return render(request, 'master_test.html', {'data_list':data})

def led_dim(request):
    global on_flag
    if con_flag == True:
        command = "led_dim"    
        try:    
            to_backend_sock.send(command.encode())
            print(f"send to {command}  backend ")
        except:
            print("command failed to send out")
            pass
        
    data_all = models.PicoMaster.objects.all()
    length= data_all.count()
    data = data_all[length-10:length]

    return render(request, 'master_test.html', {'data_list':data})

def fun_on(request):
    global on_flag
    if con_flag == True:
        command = "fun_on" 
        try:    
            to_backend_sock.send(command.encode())
            print(f"send to {command}  backend ")
        except:
            print("command failed to send out")
            pass
    data_all = models.PicoMaster.objects.all()
    length= data_all.count()
    data = data_all[length-10:length]
    return render(request, 'master_test.html', {'data_list':data})

def fun_off(request):
    global on_flag
    if con_flag == True:
        command = "fun_off" 
        try:    
            to_backend_sock.send(command.encode())
            print(f"send to {command}  backend ")
        except:
            print("command failed to send out")
            pass
    data_all = models.PicoMaster.objects.all()
    length= data_all.count()
    data = data_all[length-10:length]
    return render(request, 'master_test.html', {'data_list':data})

def serial_test(request):
    global on_flag
    if con_flag == True:
        command = "serial_test" 
        try:    
            to_backend_sock.send(command.encode())
            print(f"send to {command}  backend ")
        except:
            print("command failed to send out")
            pass
    data_all = models.PicoMaster.objects.all()
    length= data_all.count()
    data = data_all[length-10:length]
    return render(request, 'master_test.html', {'data_list':data})

# def all_off(request):
#     global on_flag
#         # global socket
#         # print("Sending request signup …")
#         # socket.send(b"signup")
#         # return render(request, 'master_test.html')
#         # context = zmq.Context()
#         # socket = context.socket(zmq.REQ)
#         # socket.connect("tcp://localhost:15555")      
#         # print("Sending request signup …")
#         # socket.send(b"signup")
#         # socket.close()
#         # context.term()
#     if con_flag == True:
#         to_backend_sock.send(b"all_off")
#         print("send back end ")


#     return render(request, 'master_test.html')

# def signin(request):
#     global on_flag
#     if con_flag == True:
#         to_backend_sock.send(b"signin")
#         print("send back end ")
#         # global socket
#         # print("Sending request signin …")
#         # socket.send(b"signin")
#         # return render(request, 'master_test.html')
#         # context = zmq.Context()
#         # socket = context.socket(zmq.REQ)
#         # socket.connect("tcp://localhost:15555")      
#         # print("Sending request signin …")
#         # socket.send(b"signin")
#         # socket.close()
#         # context.term()

#     return render(request, 'master_test.html')