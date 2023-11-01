from django.db import models as m

#class All_Section(m.Model):
    

class Section(m.Model):
    name_section = m.CharField(max_length= 255,)#Вопрос чтобы всегда заполнялась
    message = m.CharField(max_length=10000)
    comment = m.CharField(max_length=5000)
    #message_element = m.ForeignKey(All_Section, on_delete=m.SET_DEFAULT, default=None, null=True, blank=True)



    
# Create your models here.
