from .views import * #adminloginview,adminhomepageview,authenticateadmin,logoutadmin,addpizza
from django.urls import path

urlpatterns = [
    path('',homepageview, name = 'homepage'),
    path('signupuser/',signupuser),
    path('loginuser/',userloginview, name = 'userloginpage'),
    path('customer/authenticate/',userauthenticate),
    path('userlogout/', userlogout),
    path('upload/', profile_upload, name='upload'),
    path('data/', get_data,name='data'),
]

