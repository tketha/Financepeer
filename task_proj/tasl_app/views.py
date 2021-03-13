from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from sqlalchemy import create_engine
from .models import *
import json


def homepageview(request):
    return render(request, "task/homepage.html")

def signupuser(request):
    username = request.POST['username']
    password = request.POST['password']
    phoneno = request.POST['phoneno']
    # if usename already exists
    if User.objects.filter(username = username).exists():
        messages.add_message(request,messages.ERROR,"{0} Already Exists".format(username))
        return redirect('homepage')

    # if new username
    User.objects.create_user(username=username, password=password).save()
    lastobject = len(User.objects.all())-1
    CustomerModel(userid = User.objects.all()[int(lastobject)].id, phoneno = phoneno).save()
    messages.add_message(request, messages.ERROR, "{0} Successfully Created".format(username))
    return redirect('homepage')

def userloginview(request):
    return render(request,"task/userlogin.html")

def userauthenticate(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    # case-1 user exists
    if user is not None:
        login(request, user)
        return redirect('upload')

    # case-2 user doesn't exists
    if user is None:
        messages.add_message(request, messages.ERROR, "invalid credentials")
        return redirect('userloginpage')


def userlogout(request):
    logout(request)
    return redirect('userloginpage')


def profile_upload(request):


        prompt = {
            'order': 'Upload given json file',
            # 'profiles': data
                  }
        # GET request returns the value of the data with the specified key.
        if request.user.is_authenticated and request.method == "GET":
            return render(request, 'task/upload.html', prompt)
        return redirect('userloginpage')
        csv_file = request.FILES['file']
        # let's check if it is a csv file
        if  csv_file.name.endswith('.json'):
            # messages.error(request,'THIS IS NOT A CSV FILE')
        # data_set = csv_file.read().decode('UTF-8')
            data_set=pd.read_json(csv_file)
            engine = create_engine('postgresql://postgres:12345@localhost:5432/task')
            data_set.to_sql('tasl_app_upload', engine,if_exists='replace')

            context = {}
            return render(request, 'task/upload.html', context)
        else:
            return HttpResponse(json.dumps({"Note":"Please enter a valid json file"}))

def get_data(request):
    username = request.user.username
    datas = Upload.objects.all()
    return render(request,'task/data.html',{'datas':datas,'username':username})