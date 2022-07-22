from logging import raiseExceptions
from telnetlib import STATUS
from turtle import title
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from sport_news.forms import Contact_Form,Order_Form
from .models import  Contact, Gallery, League_Table, Order, Podcast, Pro_soccer_info,Next_matches,\
    Latest_result, Product, Sport_fields, Team,Team_honors,News,Nutrition, Transfer, Users_count,Video
from django.db.models import Q


# Create your views here.
def index(request):
    pro = Pro_soccer_info.objects.all().last()
    next = Next_matches.objects.all().first()
    next_all = Next_matches.objects.all().order_by('id')[:5]
    latest = Latest_result.objects.all().last()
    latest_list = Latest_result.objects.all().order_by('-id')[:7]
    honor = Team_honors.objects.all().last()
    news = News.objects.all().order_by('-id')[:2]
    first_match = Next_matches.objects.all().first()
    product = Product.objects.all().order_by('-id')[:4]
    # For ip address
    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    ip = get_ip(request)
    u = Users_count(user=ip)
    results = Users_count.objects.filter(Q(user__icontains=ip))
    if len(results)==1:
        pass
    else:
        u.save()
    count = Users_count.objects.all().count()
    
    context = {
        'next': next,
        'next_all' : next_all,
        'pro' : pro, 
        'latest' : latest, 
        'last' : latest_list,
        'honor' : honor,
        'news' : news,
        'first_match':first_match,
        'count':count,
        'product':product
    }
    return render(request,'sport_news/index.html',context)


def contact_us(request):
    product = Product.objects.all().order_by('-id')[:4]
    if request.method != 'POST':
        form = Contact_Form()
    else:
        form = Contact_Form(request.POST)
        if form.is_valid():
            new_contact = form.save(commit=False)
            new_contact.save()
            return redirect('sport_news:contact')
    context = {'form':form,'product':product}
    return render(request,'sport_news/contact_us.html',context) 


def nutrition(request):
    nut = Nutrition.objects.all().order_by('-id')
    product = Product.objects.all().order_by('-id')[:4]
    context = {'nut':nut,'product':product}
    return render(request,'sport_news/nutrition.html',context)

def news(request):
    all = News.objects.all().filter(season__contains='current_season',type__contains='news').order_by('-id')
    hot = News.objects.all().reverse().filter(season__contains='current_season').order_by('id')[:3]
    product = Product.objects.all().order_by('-id')[:4]
    context = {'all':all,'hot':hot,'product':product}
    return render(request,'sport_news/current_blog.html',context)

def blogdetail(request,myid):
    blog = News.objects.get(id=myid)
    hot = News.objects.all().reverse().filter(season__contains='current_season').order_by('id')[:3]
    product1 = Product.objects.all()[:6]
    product2 = Product.objects.all()[6:12]
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/blogdetail.html',{'blog':blog,'hot':hot,'product1':product1,'product2':product2,'product':product})

def search(request):
    if request.method == 'POST':
        searched = request.POST['q']
        result = News.objects.filter(Q(title__contains=searched)|Q(explain__contains=searched))
        product_search = Product.objects.filter(Q(title__contains=searched)|Q(description__contains=searched))
        product = Product.objects.all().order_by('-id')[:4]
        return render(request, 'sport_news/search.html', {'searched':searched,'result':result,'product':product,'product_search':product_search})

def video_us(request):
    video = Video.objects.all().order_by('id')
    laliga = Video.objects.all().filter(league_type__contains='LA_LAGA')
    product = Product.objects.all().order_by('-id')[:4]
    context = {
        'video':video,
        'laliga':laliga,
        'product':product
    }
    return render(request,'sport_news/video.html',context)

def gallery_us(request):
    gallery = Gallery.objects.filter(location__contains='gallery').order_by('-id')
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/gallery.html',{'gallery':gallery,'product':product})

def last_fix(request):
    last = Latest_result.objects.all().order_by('-id')
    last_match = Latest_result.objects.all().order_by('-id')[0]
    fix = Next_matches.objects.all().order_by('id')
    product = Product.objects.all().order_by('-id')[:4] 
    return render(request,'sport_news/matchresult.html',{'last':last,'fix':fix,'last_match':last_match,'product':product})

def fix(request,myid):
    show = Latest_result.objects.get(id=myid) 
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/matchresult.html',{'show':show,'product':product})

def last_news(request):
    last_n = News.objects.all().filter(season__contains='last_season',type__contains='news').order_by('-id')
    hot = News.objects.all().reverse().filter(season__contains='current_season').order_by('id')[:3]
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/last_blog.html',{'last_n':last_n,'hot':hot,'product':product})

def margins(request):
    frin = News.objects.all().filter(season__contains='current_season',type__contains='fringes').order_by('-id')
    hot = News.objects.all().reverse().filter(season__contains='current_season').order_by('id')[:3]
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/fringes.html',{'frin':frin,'hot':hot,'product':product})

def point_table(request):
    league = League_Table.objects.all().order_by('pos')
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/league_table.html',{'league':league,'product':product})

def transfer_table(request):
    tran = Transfer.objects.all().order_by('-id')
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/transfer.html',{'tran':tran,'product':product})

def podcast(request):
    pod = Podcast.objects.all().order_by('-id')
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/podcast.html',{'pod':pod,'product':product})

def sport_fields(request):
    fields = Sport_fields.objects.all().order_by('-id')
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/sport_fields.html',{'fields':fields,'product':product})

def frequently_questions(request):
    freq = Contact.objects.all().filter(message_type__contains='question',answer__isnull=False)
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/question.html',{'freq':freq,'product':product})

def nutrition_counseling(request):
    counsel = Contact.objects.all().filter(message_type__contains='counseling',answer__isnull=False)
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/counseling.html',{'counsel':counsel,'product':product})

def martial(request):
    all = Sport_fields.objects.all().filter(field__contains='martial')
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/martial.html',{'all':all,'product':product})

def bodybuilding(request):
    all = Sport_fields.objects.all().filter(field__contains='Bodybuilding')
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/bodybuilding.html',{'all':all,'product':product})

def group(request):
    all = Sport_fields.objects.all().filter(field__contains='Group')
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/group.html',{'all':all,'product':product})

def water_hall(request):
    all = Sport_fields.objects.all().filter(field__contains='water hall')
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/water_hall.html',{'all':all,'product':product})

def wrestling_hall(request):
    all = Sport_fields.objects.all().filter(field__contains='Wrestling hall')
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/wrestling.html',{'all':all,'product':product})

def salon(request):
    all = Sport_fields.objects.all().filter(field__contains='Salon')
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/salon.html',{'all':all,'product':product})

def team(request):
    men = Team.objects.all().filter(team__contains='men')
    ladies = Team.objects.all().filter(team__contains='ladies')
    academy = Team.objects.all().filter(team__contains='academy')
    product = Product.objects.all().order_by('-id')[:4]
    context = {
        'men':men,
        'ladies':ladies,
        'academy':academy,
        'product':product
    }
    return render(request,'sport_news/team.html',context)

def about_us(request):
    pro = Pro_soccer_info.objects.all().last()
    honor = Team_honors.objects.all().last()
    video = Video.objects.all().filter(type__contains='history')
    men = Team.objects.all().filter(team__contains='men')
    veteran = Team.objects.all().filter(team__contains='veterans')
    product = Product.objects.all().order_by('-id')[:4]
    context = {
        'pro' : pro,
        'honor':honor,
        'video':video,
        'men':men,
        'veteran':veteran,
        'product':product
    }
    return render(request,'sport_news/aboutus.html',context)

def academy(request):
    academy = Team.objects.all().filter(team__contains='academy')
    video = Video.objects.all().filter(type__contains='academy')
    news = News.objects.all().filter(season__contains='current_season',type__contains='academy').order_by('-id')[:2]
    product = Product.objects.all().order_by('-id')[:4]
    context = {
        'academy':academy,
        'video':video,
        'news':news,
        'product':product
    }
    return render(request,'sport_news/academy.html',context)

def club(request):
    video = Video.objects.all().filter(type__contains='among people')
    product = Product.objects.all().order_by('-id')[:4]
    context = {
        'video':video,
        'product':product
    }
    return render(request,'sport_news/club.html',context)

def archive_gallery(request):
    gallery = Gallery.objects.all().filter(location__contains='archive').order_by('-id')
    product = Product.objects.all().order_by('-id')[:4]
    context = {
        'gallery':gallery,
        'product':product
    }
    return render(request,'sport_news/archive_gallery.html',context)

def archive_video(request):
    video = Video.objects.all().filter(type__contains='archive')
    product = Product.objects.all().order_by('-id')[:4]
    context = {
        'video':video,
        'product':product
    }
    return render(request,'sport_news/archive_video.html',context)

def museum(request):
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/museum.html',{'product':product})

def shop(request):
    all = Product.objects.all().order_by('-id')
    offer = Product.objects.all().filter(last_price__isnull=False)
    hot = News.objects.all().reverse().filter(season__contains='current_season').order_by('id')[:3]
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/shopgrid.html',{'all':all,'offer':offer,'hot':hot,'product':product})

def club_kit(request):
    all = Product.objects.all().filter(tag__contains='club_kit').order_by('-id')
    offer = Product.objects.all().filter(last_price__isnull=False)
    hot = News.objects.all().reverse().filter(season__contains='current_season').order_by('id')[:3]
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/shopgrid.html',{'all':all,'offer':offer,'hot':hot,'product':product})

def accessories(request):
    all = Product.objects.all().filter(tag__contains='accessories').order_by('-id')
    offer = Product.objects.all().filter(last_price__isnull=False)
    hot = News.objects.all().reverse().filter(season__contains='current_season').order_by('id')[:3]
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/shopgrid.html',{'all':all,'offer':offer,'hot':hot,'product':product})
    
# def Bust(request):
#     all = Product.objects.all().filter(tag__contains='bust').order_by('-id')
#     offer = Product.objects.all().filter(last_price__isnull=False)
#     hot = News.objects.all().reverse().filter(season__contains='current_season').order_by('id')[:3]
#     product = Product.objects.all().order_by('-id')[:4]
#     return render(request,'sport_news/shopgrid.html',{'all':all,'offer':offer,'hot':hot,'product':product})

def Sports_set(request):
    all = Product.objects.all().filter(tag__contains='sport_set').order_by('-id')
    offer = Product.objects.all().filter(last_price__isnull=False)
    hot = News.objects.all().reverse().filter(season__contains='current_season').order_by('id')[:3]
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/shopgrid.html',{'all':all,'offer':offer,'hot':hot,'product':product})

# def dumbbells(request):
#     all = Product.objects.all().filter(tag__contains='dumbbells').order_by('-id')
#     offer = Product.objects.all().filter(last_price__isnull=False)
#     hot = News.objects.all().reverse().filter(season__contains='current_season').order_by('id')[:3]
#     product = Product.objects.all().order_by('-id')[:4]
#     return render(request,'sport_news/shopgrid.html',{'all':all,'offer':offer,'hot':hot,'product':product})

def shoplist(request,myid):
    detail = Product.objects.get(id=myid)
    # offer = Product.objects.all().filter(last_price__isnull=False)
    hot = News.objects.all().reverse().filter(season__contains='current_season').order_by('id')[:3]
    all = Product.objects.all().order_by('-id')[:10]
    product = Product.objects.all().order_by('-id')[:4]
    if request.method != 'POST':
        form = Order_Form()
    else:
        form = Order_Form(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.owner = request.user
            if Order.objects.filter(product_id=myid):
                return redirect('sport_news:shop-list',myid)    
            new_form.save()
            return redirect('sport_news:cart')
    return render(request,'sport_news/shoplist.html',{'detail':detail,'form':form,'hot':hot,'all':all,'product':product})

@login_required
def cart(request):    
    
    order = Order.objects.filter(owner=request.user).order_by('-id')
    total = Order.objects.filter(owner=request.user).aggregate(count=Sum('product__price'))
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/cart.html',{'order':order,'total':total,'product':product}) 
    

def delete_cart(request,myid):
    query = Order.objects.get(id=myid)
    query.delete()
    return redirect('sport_news:cart')

def buyticket(request,myid):
    info = Next_matches.objects.get(id=myid)
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'sport_news/buyticket.html',{'info':info,'product':product})

def payment(request):
    return HttpResponse("Payment Complete! Thank You.")