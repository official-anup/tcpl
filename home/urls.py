from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from home import views
from django.urls import path
# from .views import CustomLoginView,upload_file,upload_file_page,UploadedFile,customer_details,login,CustomerRegistrationForm,admin123,CustomerRegistrationForm,ProfileView,basemap,user_details,login_required,logout,LoginForm,LoginView,index,zoneDetail,planSurvey,mapCalculator,autocomplete,searchOnClick,Out_table,convert_To_Geojson,save_location,get_locations,delete_location,before_payment,payment_done,locations,getInfoValues
from django.conf.urls.static import static
from .forms import Customer2

urlpatterns = [
  path(''       , views.index,  name='index'),
  path('tables/', views.tables, name='tables'),

  path('profile/', views.ProfileView.as_view(), name='profile'),
  path('basemap/', views.basemap, name='basemap'),
  path('zondetails/', views.zonedetails, name='zonedetails'),

path('user_details/', views.user_details, name='user_details'),

  #search urls
path('autocomplete/', views.autocomplete, name='autocomplete'),
    
path('searchOnClick/', views.searchOnClick, name='searchOnClick'),
    
path('Out_table/',views.Out_table, name='Out_table'),
#bookmark   
path('save-location/',views.save_location, name='save_location'),
    
path('get-locations/',views.get_locations, name='get_locations'),
    
path('delete-location/',views.delete_location, name='delete_location'),

path('before_payment/',views.before_payment, name='before_payment'),  

path('download_file/',views.download_file, name='download_file'),  

  
path('paymentdone/',views.payment_done, name='paymentdone'),
path('locations/', views.locations, name='locations'),

path('upload_file_page/',views.upload_file_page, name='upload_file_page'),
   
path('upload_file/', views.upload_file, name='upload_file')

]
