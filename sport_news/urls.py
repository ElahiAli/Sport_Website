from django.urls import path
from .views import Sports_set, about_us, academy, accessories, archive_gallery, archive_video, blogdetail,\
     bodybuilding, buyticket, cart, club, club_kit, delete_cart, fix, frequently_questions, gallery_us, group, index,contact_us, last_fix,\
     last_news, margins, martial, museum,nutrition,news, nutrition_counseling, payment, podcast, point_table, salon,\
         search, shoplist, sport_fields, team, transfer_table,video_us, water_hall, wrestling_hall, shop

app_name = 'sport_news'

urlpatterns = [
    path('',index,name='index'),
    path('contact/',contact_us,name='contact'),
    path('nutrition/',nutrition,name='nutrition'),
    path('blog/',news,name='blog'),
    path('search/',search,name='search'),
    path('video/',video_us,name='video'),
    path('gallery/',gallery_us,name='gallery'),
    path('fixture/',last_fix,name='fixture'),
    path('fixture/<int:myid>/',fix,name='fixture-detail'),
    path('last-season/',last_news,name='last-season'),
    path('fringes/',margins,name='fringes'),
    path('table',point_table,name='table'),
    path('transfer/',transfer_table,name='transfer'),
    path('podcast/',podcast,name='podcast'),
    path('fields/',sport_fields,name='fields'),
    path('question/',frequently_questions,name='question'),
    path('counseling/',nutrition_counseling,name='counseling'),
    path('martial/',martial,name='martial'),
    path('bodybuilding/',bodybuilding,name='bodybuilding'),
    path('group/',group,name='group'),
    path('water_hall/',water_hall,name='water_hall'),
    path('wrestling/',wrestling_hall,name='wrestling'),
    path('salon/',salon,name='salon'),
    path('team/',team,name='team'),
    path('about_us/',about_us,name='about_us'),
    path('about_us/academy/',academy,name='academy'),
    path('about_us/club/',club,name='club'),
    path('archive/gallery/',archive_gallery,name='archive-gallery'),
    path('archive/video/',archive_video,name='archive-video'),
    path('museum',museum,name='museum'),
    path('blogdetail/<int:myid>/',blogdetail,name='blogdetail'),
    path('shop/',shop,name='shop'),
    path('shop/club_kit/',club_kit,name='club_kit'),
    path('shop-list/<int:myid>/',shoplist,name='shop-list'),
    path('shop/accessories/',accessories,name='accessories'),
    # path('shop/Bust/',Bust,name='Bust'),
    path('shop/Sports_set/',Sports_set,name='Sports-set'),
    # path('shop/dumbbells/',dumbbells,name='dumbbells'),
    path('shop/cart/',cart,name='cart'),
    path('delete/<int:myid>',delete_cart,name='cart-delete'),
    path('ticket/<int:myid>',buyticket,name='ticket'),
    path('payment/',payment,name='payment')
    
]