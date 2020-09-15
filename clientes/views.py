import os

from rest_framework import viewsets, status
from .models import (Menu,Factura,Mesa,Pedido,Platos,Cliente)
from .serializers import (ClienteSerializers,FacturaSerializers,MenuSerializers,PedidoSerializers,MesaSerializers,PlatosSerializers)
import requests


class ClientesViewsets(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializers

class FacturasViewsets(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializers

class MesaViewsets(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializers

class PedidoViewsets(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializers

class MenuViewsets(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers

class PLatoViewsets(viewsets.ModelViewSet):
    queryset = Platos.objects.all()
    serializer_class = PlatosSerializers

