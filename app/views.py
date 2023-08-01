from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.views.generic import View,TemplateView
# Create your views here.
def insert_fbv(request):
    SFO=studentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=studentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('data inserted')
    return render(request,'insert_fbv.html',d)
#insert_cbv
class insert_cbv(View):
    def get(self,request):
        SFO=studentForm()
        d={'SFO':SFO}
        return render(request,'insert_cbv.html',d)
    def post(self,request):
        SFD=studentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('insert_cbv')
class temp(TemplateView):
    template_name='temp'


