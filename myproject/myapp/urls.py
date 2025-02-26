from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage,name="homepageurl"),
    path('loginpage/',views.loginpage,name='loginurl'),
    path('registration/',views.registration,name='registrationurl'),
    path('aboutus/',views.aboutus,name="abouturl"),
    path('contactus/',views.contactus,name="contacturl"), 
    path('addcontact/',views.addcontact,name="addcontacturl"),
    path('display/',views.display,name='displayurl'),
    path('delete/<int:cid>/',views.delete,name="deleteurl"),
    path('edit/<int:cid>/',views.edit,name="editurl"),
    path('update/',views.update,name="updateurl"),
    path('addcontact/',views.addcontact,name="addcontacturl"),
    path('displaycontact/',views.displaycontact,name="displaydetailsurl"),
    path('userhomepage/',views.userhomepage,name="userhomepageurl"),
    path('deletecontact/<int:cid>/',views.deletecontact,name="deletecontacturl"),
    path('editcontact/<int:cid>/',views.editcontact,name="editcontacturl"),
    path('updatecontact/',views.updatecontact,name="updatecontacturl"),
    path('searchname/', views.searchname, name='searchnameurl'),
    path('logout/',views.logout,name='logouturl'),
    path('gallery/',views.Gallery,name='galleryurl'),
    path('viewgallery',views.viewgallery,name='viewgalleryurl'),
    path('updatepassword/',views.updatepassword,name='updatepasswordurl'),
    path('editprofile/',views.editprofile,name='editprofileurl'),
    path('updateprofile/',views.updateprofile,name='updateprofilepassword'),
    path('adminheader/',views.adminheader,name='adminheaderurl'),
    path('adminhome/',views.adminhome,name='adminhomeurl'),
    path('adminpassword/',views.adminpassword,name='adminpasswordurl'),
    
    
]
    