from rest_framework import generics
from rest_framework.response import Response

from .serializers import CargoSerializer
from .models import CargoModel


class CargoListAPI(generics.ListCreateAPIView):
    queryset = CargoModel.objects.all()
    serializer_class = CargoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        cargo_info = {}

        for i in queryset:
            cargo_str = str(i.date)
            if cargo_str not in cargo_info:
                cargo_info[cargo_str] = []

            cargo_info[cargo_str].append({
                'cargo': i.cargo_type,
                'rate': str(i.rate),
                'declared_value': str(i.declared_value),
                'result': (i.rate * i.declared_value),
            })

        return Response(cargo_info)

