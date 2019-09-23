from django.shortcuts import render, HttpResponse,redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,"my_app/index.html")

def index2(request):
    msg=''
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
            # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
                print("dfghjhhhhhhhhhhhhhhhh", value)
                msg+=value+"\n"
        else:           
            name=request.POST["name"]
            email=request.POST["email"]
            password=request.POST["password"]
            hash1 = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            User.objects.create(name=name, email=email, password=hash1)

    context={
        "users":User.objects.all(),
        "msg": msg
    }
    emails=User.objects.values('email')
    print(emails)
    # for email in emails:
    #     print(email.email)


    #print(User.objects.all().values())  
    return render(request,"my_app/login.html",context)

def contact(request):
    return render(request,"my_app/contact.html")

def records(request):
    return render(request,"my_app/records.html")

def check(request):
    return render(request,"my_app/check.html")



def login(request):
    user = User.objects.get(email=request.POST['email'])
    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):  
        print("password match")
    else:
        print("failed password")

    return render(request,"my_app/home.html")


def admin(request):
    context={}
    if User.objects.filter(actived=False).exists():
            unacitvated=User.objects.filter(actived=False)
        
        
    if User.objects.filter(actived=True).exists():        
        acitvated=User.objects.filter(actived=True)
        

    context={
        "acitvated":acitvated,
        "unacitvated":unacitvated
    }
    print(context)
    return render(request,"my_app/admin.html", context)
    
def activate(request,id):
    user=User.objects.get(id=id)
    user.actived=True
    user.save()
    return redirect("/admin")
    
def deactivate(request,id):
    user=User.objects.get(id=id)
    user.actived=False
    user.save()
    return redirect("/admin")
    