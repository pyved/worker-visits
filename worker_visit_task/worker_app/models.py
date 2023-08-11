from django.db import models


class Worker(models.Model):
    """
    A worker model for storing worker information
    """
    name = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name        


class Unit(models.Model):
    """
    A Unit model for storing Unit data
    """
    name = models.CharField(max_length=255, null=False, blank=False)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.name
    

class Visit(models.Model):
    """
    A Visit model store visit information of workers 
    """
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    latitude = models.FloatField(null=False, blank=False)
    longitude = models.FloatField(null=False, blank=False)
    visit_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Visit Lat {self.latitude} and Long {self.longitude}"
