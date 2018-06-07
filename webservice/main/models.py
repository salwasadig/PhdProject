from django.db import models


class MainCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Country(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
            return self.name
class ProjectFeature(models.Model):
    name = models.CharField(max_length=255, null=False)
    main_category = models.ForeignKey(MainCategory, on_delete=models.SET_NULL, null=True)
    usd_pledged = models.FloatField(null=False)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    usd_goal_real = models.FloatField(null=False)
    duration_days = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    DT_predicted = models.IntegerField(null=True)
    RF_predicted = models.IntegerField(null=True)

    def __str__(self):
            return self.name