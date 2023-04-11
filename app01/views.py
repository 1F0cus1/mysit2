from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('欢迎使用')


def user_list(request):
    # 去app目录下的templates目录寻找user_list.html
    return render(request, "user_list.html")


def user_add(request):
    return render(request, 'user_add.html')


def user_tpl(request):
    name = 'cyf1'
    roles = ['管理员','CEO','保安']
    user_info = {"name":"cyf","salary":1000,"role":"CTO"}

    data_list = [
        {"name": "cyf", "salary": 1000, "role": "CTO"},
        {"name": "cyf1", "salary": 2000, "role": "CFO"},
        {"name": "cyf2", "salary": 3000, "role": "CEO"}
    ]

    return render(request, 'tpl.html',
    {"n1": name,"n2":roles,"n3":user_info,"n4":data_list})
