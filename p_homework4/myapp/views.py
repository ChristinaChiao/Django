from django.shortcuts import render
from myapp.models import * #所有

def view_history_temperature(request):
  datas = temperature_db.objects.all().order_by('-myid')
  return render(request, 'temperature.html', {"datas": datas})
