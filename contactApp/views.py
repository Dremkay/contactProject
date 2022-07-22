from django.shortcuts import redirect, render

from .models import Contact

# Create your views here.

def index(request):
    contacts=Contact.objects.all()
    return render(request,'contactApp/index.html',{'contacts':contacts})

def create(request):
    if request.method=='POST':
        # print(request.POST)
        name=request.POST['fullname']
        relation=request.POST['relationship']
        phone=request.POST['phone-number']
        email=request.POST['email']
        address=request.POST['address']
        new_contact=Contact(fullname=name,relationship=relation,phone=phone,email=email,address=address)
        new_contact.save()
        return redirect('/')
        # print('name: ',name)
    return render(request,'contactApp/create.html')



def edit_contact(request,pk):
    contact=Contact.objects.get(id=pk)
    if request.method=='POST':
        contact.fullname=request.POST['fullname']
        contact.relationship=request.POST['relationship']
        contact.phone=request.POST['phone-number']
        contact.email=request.POST['email']
        contact.address=request.POST['address']
        contact.save()


    return render(request,'contactApp/edit.html',{'contact':contact})

def profile(request,pk):
    contact=Contact.objects.get(id=pk)
    return render(request,'contactApp/contact-profile.html',{'contact':contact})

def delete(request,pk):
    contact=Contact.objects.get(id=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('/')
    return render(request,'contactApp/delete.html',{'contact':contact})
    