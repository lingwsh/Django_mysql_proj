from django.shortcuts import render, HttpResponse, redirect
from app01.models import UserInfor


# Create your views here.
def index(request):
    return HttpResponse('hello world! BB')


def user_list(request):
    return render(request, 'user_list.html')


def info_list(request):
    data_list = UserInfor.objects.all()
    return render(request, 'info_list.html', {"data_list": data_list})


def detail(request):
    '''

    :param request: go to detail by id
    :return: go to detail page
    '''
    info_id = request.GET.get('id')
    data_detail = UserInfor.objects.get(id=info_id)
    return render(request, 'user_list.html', {"obj": data_detail})


def add_detail(request):
    return render(request, 'user_add_detail.html')


def add(request):
    # info_id = request.POST['id']
    name = request.POST['name']
    password = request.POST['password']
    age = request.POST['age']
    data_add = UserInfor(name=name, password=password, age=age)
    data_add.save()
    return redirect('/info/list/')


def delete(request):
    info_id = request.GET.get('id')
    data_delete = UserInfor.objects.get(id=info_id)
    data_delete.delete()
    # data_list = UserInfor.objects.all()
    # return render(request, 'info_list.html', {"data_list": data_list})
    return redirect('/info/list/')


def edit(request):
    info_id = request.POST['id']
    name = request.POST['name']
    password = request.POST['password']
    age = request.POST['age']
    data_edit = UserInfor.objects.get(id=info_id)
    data_edit.name = name
    data_edit.password = password
    data_edit.age = age
    data_edit.save()
    return redirect('/info/list/')