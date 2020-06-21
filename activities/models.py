from django.db import models
from django.utils import timezone

# Create your models here.
class user(models.Model):
	user_id= models.CharField(max_length=9,primary_key=True)
	real_name=models.CharField(max_length=50)
	tz=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'user_id {self.user_id} User_name {self.real_name}' 

class activity_period(models.Model):
	user_id=models.ForeignKey(user, on_delete=models.CASCADE)
	start_time=models.DateTimeField()
	stop_time=models.DateTimeField()

	

