from django.db import models

# Create your models here.

class RegisterData(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    class Meta:
        db_table = 'register'

    @staticmethod
    def get_customer_by_email(email):
        try:
            return RegisterData.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if RegisterData.objects.filter(email=self.email):
            return True

        return False

sex = {
    'Male':'Male',
    'Female':'Female',
    'Transgender':'Transgender'
}

class Image(models.Model):
    user = models.OneToOneField(RegisterData, on_delete=models.CASCADE, default=None, unique='email')
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    mobile = models.IntegerField(max_length=10, null=True)
    gender = models.CharField(max_length=10, null=True)
    photo = models.ImageField(upload_to='myimage')
    date = models.DateTimeField(auto_now_add=True)

    def placeImage(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(user_id):
        return Image.objects.filter(user=user_id).exist_by('email')
