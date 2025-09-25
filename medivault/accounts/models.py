from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import FileExtensionValidator
# Create your models here.
  
class Profile(models.Model):
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=255,null=True,blank=True)
    mobile_number = PhoneNumberField(region='IN')  
    city=models.CharField(max_length=30)
    bio=models.TextField(max_length=200)

    # date_of_birth=models.DateField(null=True,blank=True)
   
    profile_image = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True,
        default='profile_pictures/default_image.jpg',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])]
    )

    
    def __str__(self):
        return f"{self.user.username} from {self.city} "

