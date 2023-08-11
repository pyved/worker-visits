from rest_framework import generics, status
from rest_framework.response import Response
from .models import Unit, Visit
from .permissions import IsWorker, IsValidVisit
from .serializers import UnitSerializer, VisitSerializer, GetVisitSerializer


class GetUnitsAPIView(generics.ListAPIView):
    serializer_class = UnitSerializer
    permission_classes = [IsWorker]

    def get_queryset(self):
        """
        get queryset of units based on worker id
        """
        worker_id = self.kwargs['worker_id']
        return Unit.objects.filter(worker__id=worker_id)
    

class CreateVisitAPIView(generics.CreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    permission_classes = [IsValidVisit]

    def create(self, request, *args, **kwargs):
        """
        Overriding create method to create visit data and show custom response data
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Show custom response data as per requirement as VisitSerializer returns all fields of Unit model
        response_serializer = GetVisitSerializer(serializer.data)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


