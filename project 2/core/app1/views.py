
from django.shortcuts import render

def index(request):
    return render(request, 'app1/index.html', {})


text = " i think we alwase forgat to say thanks god "
def var2(request):
    return render(request, 'app1/111.html',{'text':text})


name = "mohammad amin"
def var1(request):
    return render(request, 'app1/222.html', {'name': name})


lst = ['man', 'to', 'ow','ma','shoma','anha']
def var4(request):
    return render(request, 'app1/333.html',{'list':lst})


num = 73
def var5(request):
    return render(request, 'app1/444.html', {'number': num})


empty = ''
def var3(request):
    return render(request, 'app1/555.html', {'nothing': empty})

