from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def homepage(request):
    return render(request,'homepage.html')

# def loginpage(request):
#     if request.method=='POST':
#         email=request.POST.get("email")
#         password=request.POST.get("password")
#         record=MyTable.objects.filter(email=email,password=password)
#         if record is not None:
#             request.session['email']=email
#             return render(request,'userhome.html')
#         else:
#             return HttpResponse("invalid user")
#     return render (request,'loginpage.html')
    

def loginpage(request):
    if request.method=='POST':
       
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        record=MyTable.objects.get(email=email,password=password)
        
        # return HttpResponse(record)
        if record :
            request.session['userid']=record.id
            request.session['username']=email
            if(record.email=='admin@gmail.com'):
                record=MyTable.objects.all()
                return render (request,'display.html',{"r":record})
            else:
                print(request.session['username'])
                usr=request.session['username']
                return render(request,'userhome.html',{'usr':usr})
        else:
            return HttpResponse("invalid user")
    return render(request,'loginpage.html')


def adminheader(request):
    return render(request,'adminheader.html')

# def registration(request):
#     if request.method=="POST":
#         record=MyTable()
#         record.name=request.POST.get("name")
#         record.address=request.POST.get("address")
#         record.phone=request.POST.get("phone")
#         record.email=request.POST.get("email")
#         record.password=request.POST.get("password")
#         record.save()
#         return HttpResponse("Data Saved Successfully")
#     return render(request,'registration.html')
        

def registration(request):
    if request.method=="POST":
        email=request.POST.get("email")
        if MyTable.objects.filter(email=email).exists():
            m="Username already exist"
            return render(request,"registration.html",{"m":m})
        else:
            record=MyTable()
            record.name=request.POST.get("name")
            record.address=request.POST.get("address")
            record.phone=request.POST.get("phone")
            record.email=email
            record.password=request.POST.get("password")
            record.save()
            msg="Registration Completed Successfully"
            return render(request,'loginpage.html',{"msg":msg})
    return render(request,'registration.html')

def display(request):
    record=MyTable.objects.all()
    print(record.values())
    return render (request,'display.html',{"r":record})
def delete(request,cid):
    record=MyTable.objects.get(id=cid)
    record.delete()
    record=MyTable.objects.all()
    return render(request,'display.html',{'r':record})
def edit(request,cid):
    record=MyTable.objects.get(id=cid)
    return render(request,'edit.html',{'r':record})
def update(request):
    if request.method =='POST':
        cid=request.POST.get("id")
        record=MyTable.objects.get(id=cid)
        record.name=request.POST.get("name")
        record.address=request.POST.get("address")
        record.address=request.POST.get("phone")
        record.address=request.POST.get("email")
        record.save()
        records=MyTable.objects.all()
        return render(request,'display.html',{'r':records})


def addcontact(request):
    user=request.session['username']
    if request.method=="POST":
        record=PersonalDetails()
        record.regid_id=request.session['userid']
        record.name=request.POST.get("name")
        record.phone=request.POST.get("phone")
        record.email=request.POST.get("email")
        record.save()
        return HttpResponse("Your Details are Saved Successfully")
    return render(request,'addcontact.html',{"usr":user})


# def displaycontact(request):
#     uid=request.session['userid']
#     record=PersonalDetails.objects.filter(regid_id=uid)
#     return render(request,"displaycontact.html",{"r":record, "uid":uid})


 


def displaycontact(request):
    uid=request.session['userid']
    usr=request.session['username']
    record=PersonalDetails.objects.filter(regid_id=uid)
    return render(request,"displaycontact.html",{"r":record,"usr":usr})

def deletecontact(request,cid):
    record=PersonalDetails.objects.get(id=cid)
    record.delete()
    record=PersonalDetails.objects.all()
    return render(request,'displaycontact.html',{'r':record})

def editcontact(request,cid):
    record=PersonalDetails.objects.get(id=cid)
    return render(request,'editcontact.html',{'r':record})

def updatecontact(request):
    if request.method == 'POST':
        cid=request.POST.get('id')
        record=PersonalDetails.objects.get(id=cid)
        record.name=request.POST.get("name")
        record.phone=request.POST.get("phone")
        record.email=request.POST.get("email")
        record.save()
        record=PersonalDetails.objects.all()
        return render(request,'displaycontact.html',{'r':record})


def displaycontact(request):
    uid=request.session['userid']
    usr=request.session['username']
    record=PersonalDetails.objects.filter(regid_id=uid)
    return render(request,"displaycontact.html",{"r":record,"usr":usr})




def searchname(request):
    uid=request.session['userid']
    usr=request.session['username']
    if request.method == 'POST':
        name = request.POST.get("name")
        record = PersonalDetails.objects.filter(name__icontains=name,regid_id=uid)
        if not record.exists():
            return render(request, 'searchname.html', {'error': "No records found"})
        return render(request, 'searchname.html', {'record': record,"usr":usr})
    return render(request, 'searchname.html', {"usr":usr})


# def searchname(request):
#     if request.method == 'POST':
#         name = request.POST.get("name")
#         uid=request.session['userid']
#         usr=request.session['username']
#         record = PersonalDetails.objects.filter(name=name,regid_id=uid)
#         if not record.exists():
#             return render(request, 'searchname.html', {'error': "No records found"})
#         return render(request, 'searchname.html', {'record': record,"usr":usr})
#     return render(request, 'searchname.html')


def logout(request):
    request.session['userid']=None
    request.session['username']=None
    return render (request,'logout.html')

def userhomepage(request):
    usr=request.session['username']
    print(usr)
    return render(request,'userhome.html',{'usr':usr})

def Gallery(request):
    usr=request.session['username']
    if request.method=='POST':
        image=gallery()
        image.regid_id=request.session['userid']
        image.photo=request.FILES['photo']
        image.save()
        return render(request,'gallery.html',{"usr":usr})
    return render(request,'gallery.html',{"usr":usr})


def viewgallery(request):
    usr=request.session['username']
    
    id=request.session['userid']
    images = gallery.objects.filter(regid_id=id)
    return render(request, 'viewgallery.html', {'images': images,"usr":usr})



def updatepassword(request):    
    if request.method == 'POST':
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")     
        uid = request.session.get('userid')   
        if not uid:
            return render(request, 'updatepassword.html', {'error': "User session expired or invalid. Please log in again."})     
        user = MyTable.objects.filter(id=uid).first()  
        if not user:
            return render(request, 'updatepassword.html', {'error': "User not found in database."})
        print(user.password)
        print(old_password)      
        if (old_password != user.password):  
            return render(request, 'updatepassword.html', {'error': "Old password is incorrect."})      
        if new_password != confirm_password:
            return render(request, 'updatepassword.html', {'error': "New passwords do not match."})    
        user.password = new_password
        user.save()
        return redirect('userhomepageurl')  
    return render(request, 'updatepassword.html')


# def editprofile(request):
#     return render(request,'editprofile.html')


def editprofile(request):
    uid=request.session['userid']
    usr=request.session['username']
    uid=request.session['userid']
    record=MyTable.objects.get(id=uid)
    return render(request,'editprofile.html',{'r':record,"usr":usr})



def updateprofile(request):
    usr=request.session['username']
    uid=request.session['userid']

    if request.method == "POST":
        record=MyTable.objects.get(id=uid)
        record.name=request.POST.get('name')
        record.address=request.POST.get('address')
        record.phone=request.POST.get('phone')
        record.email=request.POST.get('email')
        record.save()
        records=MyTable.objects.all()
        m="Profile Updated Successfully"
        return render(request,'userhome.html',{"r":records,"m":m,"usr":usr})


def adminhome(request):
    usr=request.session['username']
    print(usr)
    return render(request,"adminhome.html",{"usr":usr})

def adminpassword(request):
     if request.method == 'POST':
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")     
        uid = request.session.get('userid')   
        if not uid:
            return render(request, 'adminpassword.html', {'error': "User session expired or invalid. Please log in again."})     
        user = MyTable.objects.filter(id=uid).first()  
        if not user:
            return render(request, 'adminpassword.html', {'error': "User not found in database."})
        print(user.password)
        print(old_password)      
        if (old_password != user.password):  
            return render(request, 'adminpassword.html', {'error': "Old password is incorrect."})      
        if new_password != confirm_password:
            return render(request, 'adminpassword.html', {'error': "New passwords do not match."})    
        user.password = new_password
        user.save()
        return redirect('loginurl')  
     return render(request, 'adminpassword.html')
 

def aboutus(request):
    return render(request,'aboutus.html')
def contactus(request):
    return render(request,'contactus.html')