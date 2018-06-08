from rest_framework.serializers import ModelSerializer
from main.models import ProjectFeature


class ProjectCreateSerializers(ModelSerializer):
    class Meta: 
        model = ProjectFeature
        fields=[
            #'id',
            'name',
            'main_category',
            'usd_pledged',
            'country',
            'usd_goal_real',
            'duration_days',
            #'created_at',
            #'DT_predicted',
            #'RF_predicted',
        ]

class ProjectSerializers(ModelSerializer):
    class Meta: 
        model = ProjectFeature
        fields=[
            'id',
            'name',
            'main_category',
            'usd_pledged',
            'country',
            'usd_goal_real',
            'duration_days',
            'created_at',
            'updated_at',
            'DT_predicted',
            'RF_predicted',
        ]

class ProjectUpdateSerializers(ModelSerializer):
    class Meta: 
        model = ProjectFeature
        fields=[
            #'id',
            'name',
            'main_category',
            'usd_pledged',
            'country',
            'usd_goal_real',
            'duration_days',
            #'created_at',
            #'updated_at',
            'DT_predicted',
            'RF_predicted',
        ]

