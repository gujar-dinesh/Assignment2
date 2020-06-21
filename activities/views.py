from django.shortcuts import render,get_object_or_404
import json
from django.http import HttpResponse
from .models import user,activity_period

# Create your views here.
def index(request):
	us=user.objects.all()
	user_data=dict()   #dictionary used in order to create json objects of user
	l=list() # primary list which contains the all the json objects
	l2=list() #list to store the activity of the user 
	activity_data=dict()  
	members=dict() #contains the list of json objects 

	ac=activity_period.objects.all()
	for i in us:
		user_data['id']=i.user_id
		user_data['real=name']=i.real_name
		user_data['tz']=str(i.tz)
		for j in ac:
			if j.user_id==get_object_or_404(us,user_id__startswith=i.user_id):
				activity_data['start_time']=str(j.start_time)
				activity_data['end_time']=str(j.stop_time)
				l2.append(activity_data)
		user_data['activity_period']=l2



		x=json.dumps(user_data) #json object is created
		l.append(x)#json object is appended to list
	print(l)

	members["members"]=json.dumps(l,indent=4) #final dictionary Containing list of JSON Objects

	print(members)
	return render(request,'index.html',{"members":members})