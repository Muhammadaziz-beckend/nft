from django.urls import path
from .views import *

urlpatterns = [
    # control ..
    path('nft/create/',create_nft,name='create'),
    # login ...
    path('register/',register,name='register'),
    path('logaut/',logaut_user,name='logaut'),
    path('login/',login_fun,name='login'),
    path('plas_balans/',plas_balans,name='plas_balans'),
    # registr ...
    path('',index,name='workspace'),
]
