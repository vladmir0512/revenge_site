from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

class Person(models.Model):
    
    class Meta:
        db_table = 'persons'
        verbose_name = 'Персона'
        verbose_name_plural = 'Персоны'
    
    def __str__(self):
        return self.first_name + " " + self.second_name
    
    id_person = models.AutoField(primary_key=True, unique=True) # id
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    vk_ref = models.CharField(max_length=100)
    birthday = models.DateField()
    occupation = ... # list_choices '''Админ, зам, дизайнер, художник, хелпер'''
    is_singer = models.BooleanField() # bool
    

class Rank(models.Model):
    
    class Meta:
        db_table = 'ranks'
        verbose_name = 'Ранг'
        verbose_name_plural = 'Ранги'
    
    def __str__(self):
        return str(self.score)
    
    #rank = models.TextChoices('Пятый Ранг', 'Четвёртый Ранг', 'Третий Ранг', 'Второй Ранг', 'Первый Ранг', 'Первый Ранг', 'Epic Singer','Master of Singing')
    score = models.PositiveIntegerField(validators=[MinValueValidator(0)]) # int
    blood = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)]) # list_choices (капельки) 
    is_pass_exam = models.BooleanField() # bool
    is_blood = models.BooleanField() # bool

   
class Singer(models.Model):
    
    class Meta:
        db_table = 'singers'
        verbose_name = 'Вокалист'
        verbose_name_plural = 'Вокалисты'
    
    def __str__(self):
        return self.smule_nickname
    
    id_person = models.ForeignKey(Person, on_delete=models.PROTECT) # fkey_field id_person
    smule_ref = models.CharField(max_length=100)
    smule_nickname = models.CharField(max_length=50)
    rank = models.ForeignKey(Rank, on_delete=models.PROTECT) # fkey_field rank
    warnings = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)]) # int
    status = ... # list_choices
    points = models.PositiveIntegerField(validators=[MinValueValidator(0)]) # int 
    
   

