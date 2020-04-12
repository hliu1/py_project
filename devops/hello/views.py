import traceback

from django.shortcuts import render
from django.http import  HttpResponse, QueryDict
#from hello.models import User
from django.shortcuts import render
from django.contrib import messages
from .models import User
import sys

# def index(request, **kwargs):
#     #return HttpResponse("<p>Hello world,Hello,Django</p>")
#     #year = request.GET.get("year", "2020")
#     #month = request.GET.get("month", "03")
#     print(kwargs)
#     year = kwargs.get("year")
#     month = kwargs.get("month")
#     return HttpResponse("year is %s, month is %s" %(year, month))
# Create your views here.
# def index(request, month, year):
#     return HttpResponse("year is %s ,month is %s "% (year, month))

# def index(request):
#     print('=' * 30)
#     print(request.scheme)
#     print(request.method)
#     print(request.headers)
#     print(request.path)
#     print(request.META)
#     print(request.GET)
#     data = request.GET
#     year = data.get("year", "2019")
#     month = data.get("month", "10")
#     if request.method == "POST":
#         print("@" * 30)
#         print(request.method)
#         print(request.body)
#         print(QueryDict(request.body).dict())
#         print(request.POST)
#         data = request.POST
#         year = data.get("year", "2020")
#         print("*" * 30)
#         month = data.get("month", "04")
#         print(year)
#         print(month)
#     return HttpResponse("year is %s, month is %s" % (year, month))

def index(request):
    classname = "DevOps"
    books = ['Python', 'Java', 'Django']
    user = {'name': 'kk', 'age': 18}
    userlist = [{'name': 'kk', 'age': 18}, {'name': 'rock', 'age': 19},
                {'name': 'mage', 'age': 20}]
    return render(request, 'hello/hello.html', {'classname': classname, "books": books, "user":user, "userlist": userlist})

def list(request):
    value = ['python','django','java']
    messages = ['1','2','3','4','5']
    users = [
        {"username": 'kk1', 'name_cn': 'kk1', 'age': 18},
        {"username": 'kk2', 'name_cn': 'kk2', 'age': 19},
        {"username": 'kk3', 'name_cn': 'kk3', 'age': 20},
    ]
    print("=" * 30 )
    print(users)
    return render(request, 'hello/userlist.html', {'users': users , 'messages':messages , 'value':value})

def userlist_work(request):
    # result = User.objects.all()
    # print("=" * 30 )
    # print(result)
    # # data = {'name': 't1','password': '123'}
    # # result.objects.create(**data)
    # # u = User()
    # # u.name = 'kk'
    # # u.password = '123'
    # # u.save()
    # print(result)
    # return render(request, 'hello/userlist_work.html', {'users': result})
    keyword = request.GET.get("keyword","")
    users = User.objects.all()
    if keyword:
        users = users.filter(name_icontains=keyword)
    print(users)
    return render(request,'hello/userlist_work.html' ,{"users":users ,"keyword":keyword})

# def add(request):
#     return render(request ,'hello/add.html')
#
# def addaction(request):
#     print("="*30)
#     print(request.POST)
#     data = request.POST
#     name = data.get("name")
#     password = data.get("password")
#     sex = data.get("sex")
#     User.objects.create(**data)
#     return render(request ,'hello/addaction.html')

def useradd(request):    #改进版，将add代码复用
    msg = {}
    print("调用useradd")
    print(request.method)
    if request.method == "POST":
        try:
            data = request.POST.dict()  #将提交的数据转为字典，一次性入库
            print("useradd测试")
            print(type(data),data)
            #data.pop('csrfmiddlewaretoken')  #pop掉字典中的csrf
            User.objects.create(**data)
            print(User.objects.all)
            msg = {"code" :0 ,"result":"添加用户成功"}
        except:
            print("ERROR")
            msg = {"code" :1 ,"errmsg":"添加用户失败：%s" % traceback.format_exc()}
    return render(request ,"hello/add.html" ,{ "msg" : msg })


def mod(request ,id):
    user = User.objects.all().filter(id=id)
    print(type(id))
    return render(request ,'hello/mod.html', {'user': user})

def modaction(request ,id):
    print(request.POST)
    data = request.POST
    name = data.get("name")
    password = data.get("password")
    sex = data.get("sex")
    print(id,name,password)
    u = User.objects.all()
    print(u)
    User.objects.filter(id=id).update(name=name ,password=password ,sex=sex)
    return render(request, 'hello/modaction.html' ,{'user': name})

def delete(requeset ,id):
    print(type(id))
    user = User.objects.all().filter(id=id)
    print(type(requeset))
    print(type(user),user)
    return render(requeset ,'hello/delete.html', {'user': user})

def deleaction(request ,id):
    User.objects.filter(id=id).delete()
    return render(request, 'hello/deleaction.html')



