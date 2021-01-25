import uuid

from django.db import models

# Create your models here.
class customer_details(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    name = models.CharField(max_length=200, help_text="enter customer name")
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for customers')
    age = models.IntegerField
    sex = models.CharField(max_length=50)
    joining_date = models.DateField(null=True, blank=True)
    trainer =models.CharField(max_length=200, help_text="enter trainer name")
    subscription = models.CharField(max_length=200,help_text="enter the subscription type")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reversed('customer-detail', args=[str(self.id)])



class renewal(models.Model):
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4,help_text='Unique ID for this particular book across whole library')
    name = models.ForeignKey('customer_details', on_delete=models.RESTRICT)
    due_date = models.DateField(null=True, blank=True)
    renewal_date =models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['due_date']

        def __str__(self):
            """String for representing the Model object."""
            return {self.id},({self.customer.name})



class trainer_details(models.Model):
    trainer_name = models.CharField(max_length=200, help_text="enter customer name")
    age = models.IntegerField
    sex = models.CharField(max_length=50)

    class Meta:
        ordering = ['trainer_name']

    def get_absolute_url(self):
        return reversed('trainer-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return {self.customername}, {self.trainer_name}



class branch(models.Model):
    branchname = models.CharField(max_length=200, help_text="enter customer name")
    area = models.CharField(max_length=200, help_text="enter customer name")
    place = models.CharField(max_length=200, help_text="enter customer name")
    def __str__(self):
        return self.branchname

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reversed('branch-detail', args=[str(self.id)])



class subscription(models.Model):
    uniqueid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='customers unique id')
    month = models.CharField(max_length=200, help_text="enter customer name")
    amount = models.IntegerField

    def get_absolute_url(self):
        return reversed('branch-detail', args=[str(self.id)])

    def __str__(self):
        return self.customername