from django.urls import path
from .views import index,marketplace,marketplace_collection,deteil_nft,deteil_user,bey

urlpatterns = [
    path('marketplace/collections',marketplace_collection,name='market_collections'),
    path('marketplace',marketplace,name='market'),
    path('bey/<int:id>',bey,name='bey'),
    path('user/<int:id>',deteil_user,name='deteil_user'),
    path('nft/<int:id>',deteil_nft,name='deteil_nft'),
    path('',index,name='main')
]