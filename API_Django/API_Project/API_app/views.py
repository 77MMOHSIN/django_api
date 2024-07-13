from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from .form import Student
from .models import User
# Create your views here.
def thank(request):
    return render(request,'thank.html')
def show(request):
    if request.method=='POST':
        fm=Student(request.POST)
        account=User.objects.acount()
        if fm.is_valid():
            # simple safe method
            # fm.save()
            
            # cleaner data safe method
           nam= fm.cleaned_data['name']
           em= fm.cleaned_data['email']
           pa= fm.cleaned_data['password']
           reg=User(name=nam,email=em,password=pa)
           reg.save() 
           fm=Student()
        #    messages.SUCCESS(request,"form is submitted successfully!!!")
        return HttpResponse("add items is successfully")
        
    else:
        fm=Student()
        account=User.objects.acount()
        stud=User.objects.all()     
        return render(request,'addendshow.html ',{'form':fm,'stu':stud,'account':account})
    #this function will update/Edit
def update_date(request,id):
    if request.method=='POST':
        p=User.objects.get(pk=id)
        fm= Student(request.POST,instance=p)
        if fm.is_valid():
            fm.save()
    else:
        p=User.objects.get(pk=id)
        fm= Student(request.POST,instance =p)   
        return render(request ,'udatestudent.html',{'form':fm})
    return HttpResponseRedirect("/update")
    
       
# delete data
def delete_data(request,  id):
    if request.method =='POST':
     p=User.objects.get(pk=id)
     p.delete()
    return HttpResponse('/delete is successfully')   
    
         
        
