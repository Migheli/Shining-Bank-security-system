from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

   
    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)
    

    def get_duration(self):
        now = localtime()
        duration = now - self.entered_at
        if self.leaved_at:
            duration = self.leaved_at - self.entered_at
        return duration
    
    
    def format_duration(self):
        seconds = self.get_duration().total_seconds()
        hours, minutes = int(seconds // 3600), int(seconds % 3600 // 60)
        return '{:0<2} час. {:0<2} мин.'.format(hours, minutes)


    def is_long(self):
        return self.get_duration().total_seconds() // 3600 > 1
            
        
    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= 'leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
         
        )