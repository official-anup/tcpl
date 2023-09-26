# from django
# from django-datta-able1.home.forms import CustomerProfileForms
import re
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CustomerProfileForms,Customer2
from django.conf import settings
from django.shortcuts import render,HttpResponse,redirect, get_object_or_404 ,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from django.views import View
from django.core.files.storage import FileSystemStorage
from django.utils.decorators import method_decorator
from django.http import JsonResponse, HttpResponse
from django.contrib.gis.geos import Point
from django.contrib import gis
from django.contrib.gis.geos import LineString
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.serializers.geojson import Serializer as GeoJSONSerializer
from django.contrib.gis.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
import json

@login_required
def index(request):

  context = {
    'segment'  : 'index',
    #'products' : Product.objects.all()
  }
  return render(request, "pages/index.html", context)

def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/dynamic-tables.html", context)


#_____________ profile _____________________________
@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForms()
        add=Customer2.objects.filter(user=request.user)

        files = DownloadFile.objects.filter(user_id1=request.user)
        
        return render(request,'pages/profile.html',{"form":form,"active":"btn-primary","add":add,"files":files})
    
    def post(self,request):
        form=CustomerProfileForms(request.POST)
        if form.is_valid():
            usr=request.user
            fullname=form.cleaned_data["fullname"]
            
            mobileno=form.cleaned_data["mobileno"]
            
            dob=form.cleaned_data["dob"]
            
            city=form.cleaned_data["city"]
            
            pin_code=form.cleaned_data["pin_code"]
            
            address=form.cleaned_data['address']
            
            occupation=form.cleaned_data["occupation"]

            industry = form.cleaned_data["industry"]

            
            if Customer2.objects.filter(user=usr).exists():
                messages.warning(request, "Profile data already exists.")
                return redirect('profile')  # Redirect to the profile page or another suitable page
            
            
            reg=Customer2(user=usr,fullname=fullname,mobileno=mobileno,city=city,pin_code=pin_code,occupation=occupation,address=address,dob=dob,industry=industry)#
            
            reg.save()

            messages.success(request,"Congratulations !! Profile Updated Successfully")


            # add=Customer2.objects.filter(user=request.user)
       
            return render(request, 'pages/profile.html',{"form":form,"active":"btn-primary"})


@login_required
def basemap(request):
    return render(request, 'pages/basemap.html')


# def notification(request):
#     return render(request, 'pages/navigation.html')


@login_required
def zonedetails(request):
    return render(request, 'pages/zoneDetail.html')


def upload_file_page(request):
      return render(request, 'pages/upload_file.html')

# @login_required(login_url="login")
def before_payment(request):
      add=Customer2.objects.filter(user=request.user)
      return render(request, 'pages/before_payment.html',{"add":add})
    
# @login_required(login_url="login")
def payment_done(request):
    user=request.user  
    cust=Customer2.objects.filter(user=user)
    pay=Payment(user=user).save()
    
    return redirect("upload_file")


@login_required
# @staticmethod   
def upload_file(request):
        if request.method == 'POST' and 'file' in request.FILES:
            # Check if the user is authenticated
            if request.user.is_authenticated:
                uploaded_file = request.FILES['file']
                allowed_extensions = ['.jpg', '.jpeg', '.pdf', '.tif', '.tiff']

                if any(uploaded_file.name.lower().endswith(ext) for ext in allowed_extensions):
                    # Save the uploaded file using the model
                    uploaded_file_instance = UploadedFile(files1=uploaded_file, user_id1=request.user)
                    uploaded_file_instance.save()

                    message = 'File uploaded successfully!'
                else:
                    message = 'Invalid file format. Allowed formats: JPG, PDF, TIFF.'
            else:
                message = 'User is not authenticated.'
        else:
            message = ''
        return render(request, 'pages/upload_file.html', {'message': message})


def user_details(request):
    # add=Customer2.objects.filter(user=request.user) 
    #This is to get the current user,it solve the problem like to store user in login as a session.
    
    file=UploadedFile.objects.filter(user_id1=request.user)
    
    files = DownloadFile.objects.filter(user_id1=request.user)
    
    return render(request, 'pages/user_details.html',{"files":files,"active":"btn-primary"})


# @login_required(login_url="login")
def download_file(request):
    files = DownloadFile.objects.filter(user_id1=request.user)
    # print(request.user,"...............")
    return render(request, "pages/navigation.html", {"files": files})    

    
# Save BookMarks_____________________________

@csrf_exempt
@login_required
def save_location(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        name = request.POST.get('name')
        username = request.POST.get('username')

        location = Location(user=request.user, name=name,
                            latitude=latitude, longitude=longitude)
        location.save()

        return JsonResponse({'message': 'Location saved successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'})


def get_locations(request):
    locations = Location.objects.filter(user=request.user)
    data = {
        'locations': list(locations.values('id','name', 'latitude', 'longitude'))
    }
    return JsonResponse(data)

#delete_location
@csrf_exempt
@login_required
def delete_location(request):
    if request.method == 'POST':
        location_id = request.POST.get('locationId')
        try:
            location = Location.objects.get(id=location_id)
            if location.user == request.user:
                location.delete()
                return JsonResponse({'message': 'Location deleted successfully.'})
            else:
                return JsonResponse({'message': 'Unauthorized access.'}, status=401)
        except Location.DoesNotExist:
            return JsonResponse({'message': 'Location not found.'}, status=404)
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)
    
def locations(request):
    return render(request,"pages/search_location.html")    
 
 
##############################search_button orginal#######################################################################

pattern =r'(^(?P<village_name>[\w\s\(\)\.-]+),(?P<taluka_name>[\D\\w\s\(\)\.-]+)(?:,(?P<gut_numbers>\d+(?:,\d+)*))?$)|(?P<xy>\b\d+\.\d+\s*,\s*\d+\.\d+\b)'


def getInfoValues(request):
    selected_layer = request.GET.get('selected_layer')
    print(selected_layer,"______________________________________")
    if request.method == 'POST':
        selected_value = request.POST.get('radio_field')


                
    return JsonResponse(products1, safe=False)           
            


def autocomplete(request):
    term = request.GET.get('term')
    if term is not None:
        products = VillageBoundary.objects.filter(village_name_revenue__istartswith=term).values_list('village_name_revenue','taluka')
        products_list1 = list(set(products))
        products_list = [','.join(t) for t in products_list1]
        
    return JsonResponse(products_list, safe=False)

def convert_To_Geojson(products1):
    coordinates_list = []
    geojson_data = {
                    "type": "FeatureCollection",
                    "features": coordinates_list
                            }
    for instance in  products1:   
        geom_geojson = GEOSGeometry(json.dumps({"type": "MultiPolygon", "coordinates": [instance.geom.coords[0]]}))
        feature = {
        "type": "Feature",
        "geometry": json.loads(geom_geojson.geojson),
        "properties": {
            "village_name_revenue": instance.village_name_revenue,
            "taluka": instance.taluka,
                        } }
        coordinates_list.append(feature)
        # geojson_data = {
        #             "type": "FeatureCollection",
        #             "features": coordinates_list
        #                     }
    return geojson_data

def searchOnClick(request):
    response = request.GET.get("selected_value").split(",")
    respo = ','.join(response)
    sd_values = re.compile(pattern)
    sd = re.finditer(sd_values,respo)
    for s in sd:
        if bool(s.group('gut_numbers'))== True:
            tr123 = list(s.group('gut_numbers').split(","))
            products1 = Revenue1.objects.filter(taluka=s.group('taluka_name'), village_name_revenue=s.group('village_name'), gut_number__in= tr123)
            geojson_gut = convert_To_Geojson(products1)
        elif bool(s.group('village_name'))== True:           
            products1 = VillageBoundary.objects.filter(taluka=s.group('taluka_name'), village_name_revenue=s.group('village_name'))
            geojson_gut = convert_To_Geojson(products1)
            
        elif bool(s.group('xy'))== True:  
            coordinates_list =[]
            latitude, longitude = [float(coord) for coord in s.group('xy').split(',')]
            geom_geojson = GEOSGeometry(json.dumps({"type": "Point", "coordinates": [longitude, latitude]}))
            feature = {
            "type": "Feature",
            "geometry": json.loads(geom_geojson.geojson),
                            }
            coordinates_list.append(feature)
            geojson_data = {
                        "type": "FeatureCollection",
                        "features": coordinates_list
                                }
            geojson_gut = geojson_data 
        
    return JsonResponse(geojson_gut, safe=False)



# ****************PDF TABLE***************************************

def Out_table(request):
    
    response = request.GET.get("selected_value").split(",")
    villageName, talukaName, gutNumber = response[0], response[1], response[2:]
    gutnumber2=response[2:]
    
    
    products1 = Revenue1.objects.filter(taluka=talukaName, village_name_revenue=villageName, gut_number=str(gutNumber[0]))
    intersection_query = Q(geom__intersects=products1[0].geom)
    
    
    for product in products1[1:]:
        intersection_query |= Q(geom__intersects=product.geom)
    plu = FinalPlu.objects.filter(intersection_query)
    data = []
    for Iplu in plu:
        intersection_area = Iplu.geom.intersection(products1[0].geom).area
      
        data.append(Iplu.broad_lu)
        data.append(intersection_area)
        
    data1 = {
        
        "Village_Name": villageName,
        "Taluka_Name": talukaName,
        "Gut_Number": gutNumber,
        "selected_values": data
    }

   
    
    return JsonResponse(data1,safe=False) 

