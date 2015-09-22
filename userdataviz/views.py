"""
Author : Soumyaranjan
Email : soumya.raula@gmail.com
Created : 19 Sep 2015

"""
from django.shortcuts import render_to_response
from userdataviz.models import UserDataUpload


# Create your views here.
def user_fetch_all_data(request):
    return render_to_response('userdata_all.html', 
                              {'userdata_all': UserDataUpload.objects.all()})
def user_current_data(request, uploaded_id=1):
    return render_to_response('userdata.html', 
                              {'userdata': UserDataUpload.objects.get(id=uploaded_id)})