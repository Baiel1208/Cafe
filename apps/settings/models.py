from django.db import models
from apps.settings.contacnts import ICONS

# Create your models here.
class Settings(models.Model):
    logo1 = models.ImageField(
        upload_to="settings",
        verbose_name='Логотип'
    )
    logo2=models.ImageField(
        upload_to="settings",
        verbose_name='Логотип-2'
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовка"
    )
    context=models.TextField(
        verbose_name="Описание Заголовки"
    )
    image = models.ImageField(
        upload_to='settings',
        verbose_name='Фото'
    )
    image_about = models.ImageField(
        upload_to='about',
        verbose_name='Фото'
    )
    description_about= models.TextField(
        verbose_name='Описание О нас'
    )
    title2=models.CharField(
        max_length=155,
        verbose_name="Заголовка-2"
    )
    title3=models.CharField(
        max_length=155,
        verbose_name="Заголовка-3"
    )
    title4 = models.CharField(
        max_length=155,
        verbose_name="Заголовка-4"
    )
    title5 = models.CharField(
        max_length=155,
        verbose_name="Заголовка-5"
    )
    title6 = models.CharField(
        max_length=155,
        verbose_name="Заголовка-6"
    )

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name=""
        verbose_name_plural="Настройка Главного Строницы"


class About(models.Model):
    settings = models.ForeignKey(
        Settings,
        related_name="main", 
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовка"
    )
    context = models.CharField(
        max_length=255,
        verbose_name = 'Описание'
    )
    icon=models.CharField(
        choices=ICONS,
        max_length=155,
        verbose_name="Иконки"
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'О нас'


class Stati(models.Model):
    settings = models.ForeignKey(
        Settings, 
        related_name="stati",
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовка"
    )
    context = models.CharField(
        max_length=255,
        verbose_name = 'Описание'
    )
    number = models.CharField(
        max_length=50,
        verbose_name="Статистика",
        blank=True, null=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Статистика'


class Product(models.Model):
    settings = models.ForeignKey(
        Settings, 
        related_name="products",
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to="product",
        verbose_name='Фото'
    )
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовка"
    )
    context = models.CharField(
        max_length=255,
        verbose_name = 'Описание'
    )
    price=models.CharField(
        max_length=20,
        verbose_name="Цена"
    )
    cart = models.CharField(
        max_length=20,
        verbose_name='Корзина'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Наши продукты'


class Interesting(models.Model):
    settings = models.ForeignKey(
        Product, 
        related_name="interesting",
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to="interesting",
        verbose_name="Фото"
    )
    title = models.CharField(
        max_length=155,
        verbose_name = "Заголовка"
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Интересные факторы'


#######################################################################################################################
        
class AboutMain(models.Model):
    title1 = models.CharField(
        max_length=155,
        verbose_name = 'Заголовка-1'
    )
    title2 = models.CharField(
        max_length=155,
        verbose_name = 'Заголовка-2'
    )
    title3 = models.CharField(
        max_length=155,
        verbose_name = 'Заголовка-3'
    )
    descriptions = models.TextField(
        verbose_name= "Описание"
    )

    def __str__(self):
        return self.title1
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Строница о нас'


##########################################################################################################################
        
class Сontacts(models.Model):
    message = models.CharField(
        max_length=300,
        verbose_name='Имя'
    )
    email = models.CharField(
        max_length=100,
        verbose_name='Почта'
    )
    text = models.TextField(
        verbose_name='Сообщение'
    )
    name = models.CharField(
        max_length=100,
        verbose_name = 'Имя'
    )

    def __str__(self):
        return self.message
    
    class Meta:
        verbose_name=''
        verbose_name_plural='Контакты'


#############################################################################################################################

class Blog(models.Model):
    image = models.ImageField(
        upload_to='blog',
        verbose_name='Фото'
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )
    interesting_text = models.TextField(
        verbose_name = 'Интересный текст'
    )
    text = models.TextField(
        verbose_name = 'Текст'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовка'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Блог'

