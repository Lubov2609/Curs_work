from django.db import models

class Article(models.Model):
    title= models.CharField(max_length=200)
    text = models.TextField()
    user =models.TextField()

def _str_(self):
    return self.title


class Users:
    pass


class Users_type(models.Model):
    id=models.IntegerField(primary_key=True)
    type = models.BooleanField("Тип пользоваетля")


def _str_(self):
    return self.id

class Users(models.Model):
    id=models.IntegerField(primary_key=True)
    user_type_id =models.ForeignKey(Users_type,on_delete=models.CASCADE)
    parse_id=models.IntegerField()
    email= models.EmailField("Электронная почта",max_length=200)
    password = models.CharField("Пароль",max_length=30)
    logged_in =models.BooleanField()

def _str_(self):
    return self.id

class Tur(models.Model):
    id_tur = models.IntegerField(primary_key=True)
    place = models.CharField("Город",max_length=30)
    designation = models.CharField("Название",max_length=200)
    data = models.DateTimeField("Дата")
    descrition = models.TextField("Описание",max_length=5000)
    amount = models.IntegerField("количество дней")
    accompanying = models.CharField("Сопровождающий",max_length=30)
    image = models.ImageField("Фотография",upload_to="turs/")
    count = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
def _str_(self):
    return self.id_tur
class Meta:
    verbose_name= "Тур"
    verbose_name_ptural="Туры"

class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    id_user =models.ForeignKey(Users,on_delete=models.CASCADE)
    id_tura =models.ForeignKey(Tur,on_delete=models.CASCADE)
    email = models.EmailField("Электронная почта")
    phone = models.CharField("Телефон",max_length=12)
    socNetwork = models.CharField("Соц.Сеть",max_length=30)
def _str_(self):
    return self.id
class Meta:
    verbose_name= "Клиент"
    verbose_name_ptural="Клиенты"

class Reviews(models.Model):
    name = models.CharField("Имя",max_length=25)
    email= models.EmailField("Электронная почта")
    phone = models.IntegerField("Телефон")
    text = models.TextField("Отзыв",max_length=5000)
    parent = models. ForeignKey('self',verbose_name="", on_delete=models.CASCADE, blank=True,null=True)
    tur = models.ForeignKey(Tur, verbose_name="Тур", on_delete=models.CASCADE)
def _str_(self):
    return f"{self.name} - {self.tur}"

class Meta:
    verbose_name= "Отзыв"
    verbose_name_ptural="Отзывы"
class Contact(models.Model):
    first_name= models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    text = models.TextField(max_length=2000)
def _str_(self):
    return self.name

class Meta:
    verbose_name= "Контакт"
    verbose_name_ptural="Контакты"




