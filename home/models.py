from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import vping
import re

class ping():
    def __init__(self, host = [], timeout = 2, count = 4):
        self.host = host
        if not self.host:
            self.host = settings.CHECK_HOSTS
        self.timeout = timeout
        self.count = count
        for i in self.host:
            #print "host =", i
            self.ping = self.pinging(i)
            attr_host1 = re.sub('http:|https:|www.|/', '', i)
            if len(attr_host1.split(".")) == 4:
                attr_host = "ip_" + re.sub("\.", "_", attr_host1)
            else:
                attr_host = re.sub("\.", "_", attr_host1)
            setattr(self, attr_host, self.ping)
        print "local =", locals()

    def pinging(self, host):
        return vping.vping(host, self.timeout, self.count)

class singup(models.Model):
    #username = models.CharField(max_length = 50)
    #password = models.CharField(max_length = 50)
    #email = models.EmailField(max_length = 50)
    first_name = models.CharField(max_length = 50, blank = True, null = True)
    last_name = models.CharField(max_length = 50, blank = True, null = True)
    street = models.CharField(max_length = 50, blank = True, null = True)
    city = models.CharField(max_length = 20, blank = True, null = True)
    district = models.CharField(max_length = 20, blank = True, null = True)
    country = models.CharField(max_length = 20, blank = True, null = True)
    zipcode = models.CharField(max_length = 10, blank = True, null = True)
    facebook = models.CharField(max_length = 50, blank = True, null = True)
    twitter = models.CharField(max_length = 50, blank = True, null = True)
    #image = models.ImageField(width_field= 300, height_field= 300, upload_to = 'profile')
    image = models.ImageField(upload_to = 'profile')
    user = models.ForeignKey(User, on_delete= models.CASCADE, default = 0)
    
    class Meta:
        db_table = 'singup'
            
class guess(models.Model):
    access_time = models.DateTimeField(auto_now_add= True)
    download_times = models.IntegerField()
    ipaddress = models.GenericIPAddressField()
    user_agent = models.CharField(max_length = 200)
    
    class Meta:
        db_table = 'guess'

class search_history(models.Model):
    access_time = models.DateTimeField(auto_now_add= True)
    download_times = models.IntegerField()
    ipaddress = models.GenericIPAddressField()
    user_agent = models.CharField(max_length = 200, null= True, blank= True)
    
    class Meta:
        db_table = 'search_history'    

class logs(models.Model):
    date_create = models.DateTimeField(auto_now_add= True)
    level = models.IntegerField()
    facility = models.IntegerField(null= True, blank= True)
    ipaddress = models.GenericIPAddressField()
    message = models.TextField(null= True, blank= True)
    tag = models.CharField(max_length = 50)
    
    class Meta:
        db_table = 'logs'

class config(models.Model):
    static_url = models.URLField()
    media_url = models.URLField()
    
    class Meta:
        db_table = 'config'
        
    def __unicode__(self):
        return self.static_url + ";" + self.media_url