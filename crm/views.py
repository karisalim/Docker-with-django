from django.shortcuts import render
from django.views import View  
from .views import *  
from django.http import HttpResponse, Http404, HttpResponseForbidden, HttpResponseBadRequest
from datetime import datetime
from django.core.exceptions import PermissionDenied

class MyView(View): 
    def get(self, request):
        try:
            # تجميع بيانات الطلب
            request_data = {
                'Request Path': request.path,
                'Request Method': request.method,
                'Scheme': request.scheme,
                'Address': request.META.get('REMOTE_ADDR', 'Unknown'),
                'User Agent': request.META.get('HTTP_USER_AGENT', 'Unknown'),
                'Path': request.META.get('PATH_INFO', 'Unknown'),
                'HTTP Host': request.META.get('HTTP_HOST', 'Unknown'),
                'HTTP Accept': request.META.get('HTTP_ACCEPT', 'Unknown'),
            }

            # تمرير البيانات إلى القالب
            return render(request, 'index.html', {'request_data': request_data})
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}", status=500)

class Say(View):
    def get(self, request):
        return HttpResponse('<html><body><h1>Hello, World!</h1><br><h3> Hello Docker</h3><small>c</small></body></html>')

class Time(View):
    def get(self, request, name, pk):  
        try:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return HttpResponse(f"""
            <html>
            <head><title>Time Display</title></head>
            <body><h1>Time is {now}</h1></body>
            <a href="/">Login</a>
            </html>
            """)
        except Exception:
            raise Http404("Time page not found!")

class ShowForm(View):
    def get(self, request):
        return render(request, 'form.html')

class GetForm(View):
    def post(self, request):  
        try:
            id = request.POST.get('id', 'Unknown')  
            name = request.POST.get('name', 'Unknown')

            if not id or not name:
                return HttpResponseBadRequest("Missing required fields")

            return render(request, 'results.html', {'id': id, 'name': name})
        except Exception as e:
            return HttpResponse(f"Error processing form: {e}", status=500)

class RestrictedView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied()
        return HttpResponse("Welcome to the restricted area!")
