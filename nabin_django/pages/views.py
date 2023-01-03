from django.shortcuts import redirect,render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import random



def home(request):
    random_num = random.randint(1,10)
    context = {
        'random':random_num
    }
    return render(request,'pages/home.html',context)

def about(request):
    random_num = random.randint(1,10)
    return render(request,'pages/about.html')

# def send(request):
#     return render(request,'pages/send.html')

# def recieve(request):
#     if request.method == 'GET':
#         email = request.GET.get('email')
#         # password = request.GET.get('password')
#         return HttpResponse(f"HI i am from GET. {email=}")

#     if request.method == 'POST':
#         post = request.POST
#         email = post.get('email')
#         password = post.get('password')
#         return HttpResponse(f"HI i am from POST. {email=} {password=}")
def get_data():
    with open('data.txt','r') as file:
        lines = file.readlines()
    lines = [l.replace('\n','') for l in lines]
    return lines

def write_data(text):
    with open('data.txt','a+') as file:
            file.writelines(str(text)+'\n')

def clear_data():
    with open('data.txt','w+') as file:
        file.writelines('')

      
def todo(request):

    if request.method == "POST":
        text = request.POST.get('text')
        # print('/n'*10,request.POST.get('text'))
        write_data(text)
        
    data = get_data()


    return render(request,'pages/todo.html',context={'data':data})

def remove_todo(request, todo):
    #DELETE
    print('\n'*10, todo)
    
    previous_data = get_data()
    previous_data.remove(todo)

    clear_data()
    for data in previous_data:
        write_data(data)
    

    return redirect('todo')



