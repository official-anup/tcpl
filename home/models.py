from django.db import models
from django.contrib.auth.models import User 
from django.contrib.gis.db import models

# Create your models here.

# class Product(models.Model):
#     id    = models.AutoField(primary_key=True)
#     name  = models.CharField(max_length = 100) 
#     info  = models.CharField(max_length = 100, default = '')
#     price = models.IntegerField(blank=True, null=True)

#     def __str__(self):
#         return self.name
   

OCCUPATION_CHOICES=[
   ("others","others"),
   ("architect","architect"),
   ("builder","builder"),
   ("land owner", "land owner"),
   ("liaison","liaison")
   
]

INDUSTRY_CHOICES = [
    ('civil', 'Civil'),
    ('govt', 'Government'),
    ('private', 'Private'),
    ('ngo', 'NGO'),
    ('other', 'Other'),
]




class Customer2(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    fullname=models.CharField(max_length=200)
   
    dob = models.DateField()  # Add the date of birth field
   
    address = models.TextField(max_length=250)
    
    city=models.TextField(max_length=50)
    
    pin_code =models.IntegerField()# Add the address field
   
    mobileno = models.BigIntegerField()
    
    occupation=models.CharField(choices=OCCUPATION_CHOICES,max_length=200)
    
    industry = models.CharField(choices=INDUSTRY_CHOICES, max_length=20)

    def __str__(self):
        return str(self.id)
    




class UploadedFile(models.Model):
    user_id1 = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
    files1 = models.FileField(upload_to="file/", blank=True)

   

     
   
# Location table create for save bookmark
class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    name = models.CharField(max_length=100, default='Default Name')
    latitude = models.FloatField()
    longitude = models.FloatField()

    # def __str__(self):
    #     return self.name
    
class VillageBoundary(models.Model):
    fid = models.BigIntegerField(primary_key=True)
    # geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    geom = models.GeometryField()  # This field type is a guess.
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    taluka = models.CharField(db_column='Taluka', max_length=50, blank=True, null=True)  # Field name made lowercase.
    area_in_ha = models.FloatField(db_column='Area_In_Ha', blank=True, null=True)  # Field name made lowercase.
    village_name_census = models.CharField(db_column='Village_Name_Census', max_length=255, blank=True, null=True)  # Field name made lowercase.
    village_name_revenue = models.CharField(db_column='Village_Name_Revenue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    temp = models.IntegerField(db_column='Temp', blank=True, null=True)  # Field name made lowercase.
    shape_length = models.FloatField(db_column='Shape_Length', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='Shape_Area', blank=True, null=True)  # Field name made lowercase.
  

    class Meta:
        managed = False
        db_table = 'village_boundary'
        #'Village_Boundary'
        
class Revenue1(models.Model):
    objectid = models.BigIntegerField(db_column='OBJECTID', primary_key=True)  # Field name made lowercase.
    geom = models.GeometryField(blank=True, null=True)
    gut_number = models.CharField(db_column='Gut_Number', max_length=50, blank=True, null=True)  # Field name made lowercase.
    taluka = models.CharField(db_column='Taluka', max_length=50, blank=True, null=True)  # Field name made lowercase.
    area_in_ha = models.FloatField(db_column='Area_In_Ha', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=200, blank=True, null=True)  # Field name made lowercase.
    govtland_gayran_type = models.CharField(db_column='GovtLand_Gayran_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    govt_private_forest_type = models.CharField(db_column='Govt_Private_Forest_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    govtland_forest_7_12_availibility = models.CharField(db_column='GovtLand_Forest_7_12_Availibility', max_length=50, blank=True, null=True)  # Field name made lowercase.
    govtland_forest_as_7_12_full_part = models.CharField(db_column='GovtLand_Forest_as_7_12_Full_Part', max_length=50, blank=True, null=True)  # Field name made lowercase.
    old_gut_no = models.CharField(db_column='Old_Gut_No', max_length=50, blank=True, null=True)  # Field name made lowercase.
    new_gut_no = models.CharField(db_column='New_Gut_No', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    village_name_census = models.CharField(db_column='Village_Name_Census', max_length=255, blank=True, null=True)  # Field name made lowercase.
    village_name_revenue = models.CharField(db_column='Village_Name_Revenue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    temp = models.IntegerField(db_column='Temp', blank=True, null=True)  # Field name made lowercase.
    shape_length = models.FloatField(db_column='Shape_Length', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='Shape_Area', blank=True, null=True)  # Field name made lowercase.
    village_taluka = models.CharField(db_column='Village_Taluka', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'revenue1'
        
        

# class FinalPlu(models.Model):
#     fid = models.BigIntegerField(primary_key=True)
#     geom = models.GeometryField(blank=True, null=True)
#     taluka = models.CharField(db_column='TALUKA', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     broad_lu = models.CharField(db_column='Broad_LU', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     detailed_l = models.CharField(db_column='Detailed_L', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     descriptio = models.CharField(db_column='Descriptio', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     label = models.CharField(db_column='Label', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     area_ha = models.FloatField(db_column='Area_HA', blank=True, null=True)  # Field name made lowercase.
#     plu_zone = models.CharField(db_column='PLU_Zone', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     reservatio = models.CharField(db_column='Reservatio', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pa_name = models.CharField(db_column='PA_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     growth_centre = models.CharField(db_column='Growth_Centre', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     shape_length = models.FloatField(db_column='Shape_Length', blank=True, null=True)  # Field name made lowercase.
#     shape_area = models.FloatField(db_column='Shape_Area', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Final_PLU'

class Payment(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
    ammount=models.IntegerField(default=50)

class DownloadFile(models.Model):
    user_id1 = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
    files1 = models.FileField(upload_to="file", blank=True)
   



# class villagetalukadata(models.Model):
    
#     user=models.ForeignKey(User, on_delete=models.CASCADE)
#     village = models.CharField(max_length=200)
#     taluka=models.CharField(max_length=100)
#     gut=models.CharField(max_length=100)

#     def __str__(self):
#         return self.village 



# # WARD_MODEL
# class DhankawadiWards(models.Model):
#     objectid = models.BigIntegerField(db_column='OBJECTID', primary_key=True)  # Field name made lowercase.
#     geom = models.GeometryField(blank=True, null=True)
#     name = models.CharField(max_length=80, blank=True, null=True)
#     wardnum = models.CharField(max_length=50, blank=True, null=True)
#     shape_length = models.FloatField(db_column='Shape_Length', blank=True, null=True)  # Field name made lowercase.
#     shape_area = models.FloatField(db_column='Shape_Area', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Dhankawadi_wards'


# class Dhankawadi(models.Model):
#     objectid = models.BigIntegerField(db_column='OBJECTID', primary_key=True)  # Field name made lowercase.
#     geom = models.GeometryField(blank=True, null=True)
#     name = models.CharField(max_length=80, blank=True, null=True)
#     shape_length = models.FloatField(db_column='Shape_Length', blank=True, null=True)  # Field name made lowercase.
#     shape_area = models.FloatField(db_column='Shape_Area', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'dhankawadi'

# # class DhankawdiRoad(models.Model):
# #     objectid = models.BigIntegerField(db_column='OBJECTID', primary_key=True)  # Field name made lowercase.
# #     geom = models.GeometryField(blank=True, null=True)
# #     name = models.CharField(db_column='Name', max_length=320, blank=True, null=True)  # Field name made lowercase.
# #     road_width = models.CharField(db_column='Road_width', max_length=50, blank=True, null=True)  # Field name made lowercase.     
# #     missing_existing = models.CharField(db_column='Missing_Existing', max_length=50, blank=True, null=True)  # Field name made lowercase.
# #     length_m = models.FloatField(db_column='Length_m', blank=True, null=True)  # Field name made lowercase.
# #     wardnum = models.CharField(max_length=50, blank=True, null=True)
# #     shape_length = models.FloatField(db_column='Shape_Length', blank=True, null=True)  # Field name made lowercase.

# #     class Meta:
# #         managed = False
# #         db_table = 'Dhankawdi_Road'


# class DhankawdiRoad(models.Model):
#     objectid = models.BigIntegerField(db_column='OBJECTID', primary_key=True)  # Field name made lowercase.
#     geom = models.GeometryField(blank=True, null=True)
#     name = models.CharField(db_column='Name', max_length=320, blank=True, null=True)  # Field name made lowercase.
#     road_width = models.CharField(db_column='Road_width', max_length=50, blank=True, null=True)  # Field name made lowercase.     
#     missing_existing = models.CharField(db_column='Missing_Existing', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     length_m = models.FloatField(db_column='Length_m', blank=True, null=True)  # Field name made lowercase.
#     wardnum = models.CharField(max_length=50, blank=True, null=True)
#     shape_length = models.FloatField(db_column='Shape_Length', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Dhankawdi_Road'


# class Road(models.Model):
#     objectid = models.BigIntegerField(db_column='OBJECTID', primary_key=True)  # Field name made lowercase.
#     geom = models.GeometryField(blank=True, null=True)
#     name = models.CharField(db_column='Name', max_length=320, blank=True, null=True)  # Field name made lowercase.
#     road_width = models.CharField(db_column='Road_width', max_length=50, blank=True, null=True)  # Field name made lowercase.     
#     missing_existing = models.CharField(db_column='Missing_Existing', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     length_m = models.FloatField(db_column='Length_m', blank=True, null=True)  # Field name made lowercase.
#     wardnum = models.CharField(max_length=50, blank=True, null=True)
#     shapelength = models.CharField(db_column='shapeLength', max_length=50, blank=True, null=True)  # Field name made lowercase.   
#     shape_length = models.FloatField(db_column='Shape_Length', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Road'
