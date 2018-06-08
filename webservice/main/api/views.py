from main.models import ProjectFeature
import pandas as pd
import pickle
from .serializers import (
    ProjectSerializers, 
    ProjectCreateSerializers,
    ProjectUpdateSerializers
)
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)


class ProjectAPICreateView(CreateAPIView):
    queryset = ProjectFeature.objects.all()
    serializer_class = ProjectCreateSerializers
    def predict(self, serializers):
        print(serializers.data)

class ProjectAPIListView(ListAPIView):
    queryset = ProjectFeature.objects.all()
    serializer_class = ProjectSerializers

class ProjectAPIDetailView(RetrieveAPIView):
    queryset = ProjectFeature.objects.all()
    serializer_class = ProjectSerializers

class ProjectAPIUpdateView(RetrieveUpdateAPIView):
    queryset = ProjectFeature.objects.all()
    serializer_class = ProjectUpdateSerializers
    def perform_update(self, serializer):
        y = pd.DataFrame([[self.request.data['main_category'],
                           self.request.data['country'], 
                           self.request.data['usd_pledged'], 
                           self.request.data['usd_goal_real'],
                           self.request.data['duration_days']]])

        DT = pickle.load(open('finalized_DT_model.sav', 'rb'))
        DTpredicted = DT.predict(y)
        RF = pickle.load(open('finalized_RF_model.sav', 'rb'))
        RFpredicted = RF.predict(y)
        serializer.save(DT_predicted = DTpredicted, RF_predicted = RFpredicted)


class ProjectAPIDeleteView(DestroyAPIView):
    queryset = ProjectFeature.objects.all()
    serializer_class = ProjectSerializers