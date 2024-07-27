from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KI', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Tea_images/')
    date_added = models.DateTimeField(default=timezone.now)
    types = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    pricing = models.DecimalField(default=350, max_digits=5, decimal_places=2)
    description = models.TextField(default='')

    def __str__(self):
        return self.name


# One to Many
class ChaiReview(models.Model):
    chai = models.ForeignKey(
        ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_reviews')
    RATING_CHOICE = [(1, 'One Star'),
                     (2, 'Two Stars'),
                     (3, 'Three Stars'),
                     (4, 'Four Stars'),
                     (5, 'Five Stars')]
    ratings = models.IntegerField(choices=RATING_CHOICE)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.chai.name}"


# Many to Many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(
        ChaiVariety, related_name='chai_stores')

    def __str__(self):
        return self.name


# One to One
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(
        ChaiVariety, on_delete=models.CASCADE, related_name='certificate_of_chai')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f"Certificate for {self.chai.name}"
