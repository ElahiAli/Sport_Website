from logging import raiseExceptions
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Pro_soccer_info(models.Model):
    header = models.CharField(max_length=100)
    explain = models.TextField()
    images =  models.ImageField(null=True,blank=True,upload_to='uplods/',  max_length=100)

    def __str__(self) -> str:
        return self.header
        
class Next_matches(models.Model):
    LA_LAGA = 'laliga'; BUNDESLIGA = 'bundesliga'; CHAMPIONSHIP = 'championship' 
    January='January'; February='February'; March='March'; April='April'; May='May'; June='June'; July='July'; August='August'; \
        September='September'; October='October'; November='November'; December='December'

    month_choice  = [(January,'January'),(February,'February'),(March,'March'),( April,'April'),(May,'May'),(June,'June'),(July,'July'),
        (August,'August'),(September,'September'),(October,'October'),(November,'November'),(December,'December')]
    league_choice = [(LA_LAGA,'laliga'),(CHAMPIONSHIP,'championship'),(BUNDESLIGA,'bundesliga')]
    player_image = models.ImageField(null=True,blank=True,upload_to='uplods/',  max_length=100)
    first_team_name = models.CharField(max_length=100)
    first_team_image = models.ImageField(upload_to='uplods/',  max_length=100)
    second_team_name = models.CharField(max_length=100)
    second_team_image = models.ImageField(upload_to='uplods/',  max_length=100)
    address = models.CharField(max_length=255)
    header = models.CharField(max_length=255)
    history_of_teams = models.TextField()
    explain_future_plan = models.TextField()
    clock = models.CharField(max_length=5)
    day = models.PositiveSmallIntegerField()
    month = models.CharField(max_length=20,choices=month_choice)
    league_type = models.CharField(max_length=12,choices=league_choice)
    def __str__(self) -> str:
        return self.first_team_name + " vs " +self.second_team_name

class Latest_result(models.Model):
    LA_LAGA = 'laliga'; BUNDESLIGA = 'bundesliga'; CHAMPIONSHIP = 'championship' 
    January='January'; February='February'; March='March'; April='April'; May='May'; June='June'; July='July'; August='August'; \
        September='September'; October='October'; November='November'; December='December' 
    win='win'; lose='lose'; draw='draw'

    stat_choice = [(win,'win'),(lose,'lose'),(draw,'draw')]
    month_choice  = [(January,'January'),(February,'February'),(March,'March'),( April,'April'),(May,'May'),(June,'June'),(July,'July'),
        (August,'August'),(September,'September'),(October,'October'),(November,'November'),(December,'December')]    
    league_choice = [(LA_LAGA,'laliga'),(CHAMPIONSHIP,'championship'),(BUNDESLIGA,'bundesliga')]
    first_team_name = models.CharField(max_length=255)
    first_team_image = models.ImageField(upload_to=None,  max_length=100)
    first_team_goals = models.PositiveIntegerField()
    first_team_stat = models.CharField(max_length=5,choices=stat_choice)
    second_team_name = models.CharField(max_length=255)
    second_team_image = models.ImageField(upload_to=None,  max_length=100)
    second_team_goals = models.PositiveIntegerField()
    second_team_stat = models.CharField(max_length=5,choices=stat_choice)
    address = models.CharField(max_length=200)
    clock = models.CharField(max_length=5)
    day = models.PositiveSmallIntegerField()
    month = models.CharField(max_length=20,choices=month_choice)
    league_type = models.CharField(max_length=12,choices=league_choice)
    first_team_stat = models.CharField(max_length=5,choices=stat_choice)

class Team_honors(models.Model):
    number_of_goals = models.PositiveIntegerField(null=True,blank=True)
    earned_awards = models.PositiveIntegerField(null=True,blank=True)
    active_teams = models.PositiveIntegerField(null=True,blank=True)
    active_player = models.PositiveIntegerField(null=True,blank=True)

class News(models.Model):
    NEWS = 'news'
    FRINGES = 'fringes'
    ACADEMY = 'academy'
    LAST_SEASON = 'last_season'
    CURRENT_SEASON = 'current_season'
    season_choice = [(LAST_SEASON,'last_season'),(CURRENT_SEASON,'current_season')]
    type_choice = [(NEWS,'news'),(FRINGES,'fringes'),(ACADEMY,'academy')]
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=None,  max_length=100)
    video_url = models.URLField(null=True,blank=True)
    abstract = models.TextField(null=True,blank=True)
    explain = models.TextField()
    type = models.CharField(max_length=10,choices=type_choice)
    season = models.CharField(max_length=20,choices=season_choice)
    author = models.CharField(max_length=255)
    author_detail = models.CharField(max_length=255)    
    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    MESSAGE_TYPE_DISCUSSION = 'Discussion'
    MESSAGE_TYPE_QUESTION = 'question'
    MESSAGE_TYPE_COUNSELING = 'counseling'
    message_choice = [(MESSAGE_TYPE_DISCUSSION , 'Discussion'),\
       (MESSAGE_TYPE_QUESTION,'question'),(MESSAGE_TYPE_COUNSELING ,'counseling')]
    name = models.CharField(max_length=255)
    e_mail = models.EmailField()
    message_type = models.CharField(max_length=12,choices=message_choice)
    message = models.CharField(max_length=5000)
    answer = models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name + " type: " + self.message_type

class Nutrition(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    image = image = models.ImageField(upload_to=None,  max_length=100, blank=True, null=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
    
class Video(models.Model):
    LA_LAGA = 'laliga'
    CHAMPIONSHIP = 'championship' 
    BUNDESLIGA = 'bundesliga'
    HISTORY = 'history'
    ARCHIVE = 'archive'
    VIDEO = 'video'
    ACADEMY = 'academy'
    AMONG = 'among people'
    type_choice = [(HISTORY,'history'),(ARCHIVE,'archive'),(VIDEO,'video'),(ACADEMY,'academy'),(AMONG,'among people')]
    league_choice = [(LA_LAGA,'laliga'),(CHAMPIONSHIP,'championship'),(BUNDESLIGA,'bundesliga')]
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    league_type = models.CharField(max_length=12,choices=league_choice,null=True,blank=True)
    type = models.CharField(max_length=15,choices=type_choice)
    description = models.CharField(max_length=255,null=True,blank=True)
    date = models.DateField(default=datetime.now)

    def __str__(self) -> str:
        return self.title

class Gallery(models.Model):
    ARCHIVE = 'archive'
    GALLERY = 'gallery'
    choice_type = [(ARCHIVE,'archive'),(GALLERY,'gallery')]
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=None,  max_length=100)
    location = models.CharField(max_length=10,choices=choice_type)
    date = models.DateField(default=datetime.now)

    def __str__(self) -> str:
        return self.title
    
class League_Table(models.Model):
    team_url = models.URLField()
    pos = models.PositiveIntegerField()
    team = models.CharField(max_length=255)
    P = models.PositiveIntegerField()
    W = models.PositiveIntegerField()
    D = models.PositiveIntegerField()
    L = models.PositiveIntegerField()
    F = models.PositiveIntegerField()
    A = models.PositiveIntegerField()
    GD = models.SmallIntegerField()
    Pts  =models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.team

    class Meta:
        ordering = ['Pts']

class Transfer(models.Model):
    name = models.CharField(max_length=255)
    nation = models.ImageField(upload_to=None,  max_length=100)
    age = models.PositiveIntegerField()
    left = models.ImageField(upload_to=None,  max_length=100)
    join = models.ImageField(upload_to=None,  max_length=100)
    fee = models.DecimalField(max_digits=2,decimal_places=1)

class Podcast(models.Model):
    title = models.CharField(max_length=255)
    audio = models.FileField(upload_to='uploads/')
    date = models.DateField(default=datetime.now)

    class Meta:
        db_table = 'demo_m_call'


class Sport_fields(models.Model):
    MARTIAL = 'martial'
    BODYBUILDING = 'Bodybuilding'
    GROUP = 'Group'
    WATER_HALL = 'water hall'
    WRESTLING_HALL = 'Wrestling hall'
    SALON = 'Salon'
    field_choice = [(MARTIAL,'martial'),(BODYBUILDING,'Bodybuilding'),(GROUP,'Group'),(WATER_HALL,'water hall'),\
        (WRESTLING_HALL,'Wrestling hall'),(SALON ,'Salon')]
    title = models.CharField(max_length=255)
    describe = models.TextField()
    image = models.ImageField(upload_to=None,  max_length=100, blank=True,null=True)
    field = models.CharField(max_length=20,choices=field_choice, blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    

class Team(models.Model):
    MEN = 'men'
    LADIES = 'ladies'
    ACADEMY = 'academy'
    VETERANS = 'veterans'
    team_choice = [(MEN,'men'),(LADIES,'ladies'),(ACADEMY,'academy'),(VETERANS,'veterans')]
    full_name = models.CharField(max_length=255)
    post = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=250,null=True,blank=True)
    image = models.ImageField(upload_to=None,  max_length=100, blank=True,null=True)
    team = models.CharField(max_length=10,choices=team_choice)


class Product(models.Model):
    Club_Kit = 'club_kit'; Accessories = 'accessories'; Bust = 'bust'; Sports_set = 'sport_set';  Dumbbells = 'dumbbells'
    tag_choice = [(Club_Kit,'club_kit'),(Accessories,'accessories'),(Bust,'bust'),(Sports_set,'sport_set'),(Dumbbells,'dumbbells')]
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    last_price = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to=None,  max_length=100)
    tag = models.CharField(max_length=15,choices=tag_choice)
    
    def __str__(self) -> str:
        return self.title
        
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    S = 'S'; M = 'M'; L = 'L'; XL = 'XL'; XXL = 'XXL' 
    size_choice = [(S,'S'),(M,'M'),(L,'L'),(XL,'XL'),(XXL,'XXL')]
    size = models.CharField(max_length=5,choices=size_choice,blank=True,null=True)
    count = models.PositiveSmallIntegerField(blank=True,null=True)
    owner = models.ForeignKey(User,on_delete= models.CASCADE)

    class Meta:
        unique_together = [['product','owner']]
        

    def __str__(self) -> str:
        return self.product.title
    
class Users_count(models.Model):
    user = models.TextField(default=None)
    def __str__(self) -> str:
        return self.user