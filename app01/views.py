from django.shortcuts import render, HttpResponse,redirect


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

def news(request):
    import requests
    headers = {
        'Accept-Encoding':'gzip, deflate',
        'Connection':'keep-alive',
        'Content-Type':'text/plain;charset=UTF-8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    url = "http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2023/04/news"
    res = requests.get(url=url,headers=headers)
    data_list = res.json()

    print(data_list)
    return render(request,'news.html',{"news":data_list})

def something(request):

    print(request.method)

    print(request.GET)

    # return HttpResponse('helloworld')
    # return render(request,'something.html',{"title":"来了"})
    return redirect('https://www.baidu.com')

def login(request):

    if request.method == 'GET':
        return render(request,'login.html')

    print(request.POST)
    username = request.POST.get("user")
    password = request.POST.get("pwd")
    if username == 'root' and password == '123':
        return redirect("http://www.chinaunicom.com.cn/index.html")

    return render(request,'login.html',{"error_message":"账号密码错误！"})