from django.db import models
class Cliente(models.Model):
    id_Cliente = models.IntegerField(unique=True, primary_key=True)


class Platos(models.Model):
    id_plato = models.IntegerField(unique=True, primary_key=True)
    precio = models.IntegerField(null=False, blank=True)
    pedido = models.ForeignKey('clientes.Pedido', on_delete=models.CASCADE, null=True, blank=True)
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE, null=True, blank=True)
    menu=models.ForeignKey('clientes.Menu', on_delete=models.CASCADE, null=True, blank=True)


class Mesa(models.Model):
    id_mesa = models.IntegerField(unique=True, primary_key=True)

class Menu(models.Model):
    id_menu = models.IntegerField(unique=True, primary_key=True)

class Pedido(models.Model):
    id_pedido = models.IntegerField(unique=True, primary_key=True)


class Factura(models.Model):
    id_factura = models.IntegerField(unique=True, primary_key=True)
