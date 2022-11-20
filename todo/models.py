from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True) #данный атрибут не сможем изменять вручную
    datecompleted = models.DateTimeField(null=True, blank=True)  # либо Null, либо строго необходимого типа (дата время)
    important = models.BooleanField(default=False) # по умолчанию не обязательный
    # создаем привязку к пользователю - внешний ключ (импортировали User)
    user = models.ForeignKey(User, on_delete=models.CASCADE) #берет id пользователя и помещает в этот ключ

    def __str__(self):
        return self.title


