# ajack Author Content
Python code to access API
```
>>python manage.py createsuperuser
create credentials
>>python manage.py runserver
Login with credentials to access API

```
# models.py
phone and  pincode validation is done by defining functions
User model is extended for author, one to mant relation ship is between content and categories

```
def phone_validation(phone):
    if len(phone) != 10:   #
        raise ValidationError('This is not a valid phone')

def pincode_validation(pincode):
    if len(phone) != 6:   #
        raise ValidationError('This is not a valid pincode')
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.BigIntegerField('phone',validators=[phone_validation])
    address = models.CharField('address',max_length=300)
    city = models.CharField('city',max_length=50)
    state = models.CharField('state',max_length=50)
    country = models.CharField('country',max_length=50)
    pincode = models.IntegerField('pincode',validators=[pincode_validation])

class Content(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=300)
    summary = models.CharField(max_length=60)
    document = models.FileField(upload_to='pdf')

class Categories(models.Model):
    id = models.IntegerField('id',primary_key=True)
    conref = models.ForeignKey(Content ,on_delete=models.CASCADE,related_name='catref')
```
# serilizer.py
To serilaize and deserilise content and categories,
nested relationship is between content and categories as by content id  to acesss all assigned categories

```
class CategoriesSerilizer(ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class ContentSerilizer(ModelSerializer):
    catref = CategoriesSerilizer(many = True)
    class Meta:
        model = Content
        fields =('title','body','summary','document','catref')
```
# views.py
For authorisation persmission class is used

```
in setting.py, for permisssion

REST_FRAMEWORK = {


    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated',]
}
```
```
class ContentView(ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerilizer
    permission_classes = [IsAuthenticated,IsAdminUser]

class CategoriesSerilizer(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerilizer
    permission_classes = [IsAuthenticated,IsAdminUser]
    
```
# Data adding
Data can be added through django admin or through database.
