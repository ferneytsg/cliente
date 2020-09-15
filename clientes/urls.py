from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (MenuViewsets,ClientesViewsets,MesaViewsets,FacturasViewsets,
                    PedidoViewsets,PLatoViewsets)


# Create a router and register our viewsets with it.
router = DefaultRouter()


router.register('platos', PLatoViewsets)
router.register('menu', MenuViewsets)
router.register('clientes', ClientesViewsets)
router.register('mesa', MesaViewsets)
router.register('facturas', FacturasViewsets)
router.register('pedido', PedidoViewsets)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
