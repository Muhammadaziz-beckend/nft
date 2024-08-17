from django.db import models
from django.contrib.auth.models import User


class Nft(models.Model):
    img = models.ImageField(verbose_name='Изображения')
    name = models.CharField(verbose_name='Названия',max_length=15)
    created_by = models.ForeignKey(to='UserModel', verbose_name='Владелец', on_delete=models.CASCADE,related_name='created_by',)
    description = models.TextField(verbose_name='Описания')
    collection = models.ForeignKey(verbose_name='Катигория',to='Category',on_delete=models.SET_NULL,null=True,related_name='collection')
    tegs = models.ManyToManyField(to='Tegs',verbose_name='Теги',)
    prise = models.DecimalField( verbose_name='Цена', max_digits=10, decimal_places=2)
    create_date = models.DateField(verbose_name='Дата создания',auto_now_add=True)
    is_sold = models.BooleanField(verbose_name='Продаётся',default=True)


    class Meta:
        verbose_name = 'Nft'
        verbose_name_plural = 'Nft'

    def __str__(self) -> str:
        return self.name


class Tegs(models.Model):
    name = models.CharField(verbose_name='Тег',max_length=10)
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self) -> str:
        return self.name
    

class UserModel(models.Model):
    user = models.OneToOneField(to=User,verbose_name='Пользователь',on_delete=models.CASCADE,related_name='user')
    photo = models.ImageField(upload_to='photo',verbose_name='Фото',default='img/user_1.png')
    created = models.PositiveBigIntegerField(verbose_name='Созданно',default=0)
    nfts_sold = models.DecimalField(verbose_name='Проданно',max_digits=10, decimal_places=0,default=0.00)
    balans = models.DecimalField(verbose_name='Баланс', max_digits=10, decimal_places=2,default=0.00)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Category(models.Model):
    photo = models.ImageField(verbose_name='Изображения',upload_to='colection/')
    name = models.CharField(verbose_name='Названия катигории',max_length=15)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Kатигория'
        verbose_name_plural = 'Kатигории'