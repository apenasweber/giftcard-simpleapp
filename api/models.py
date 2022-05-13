import uuid

from django.db import models

"""
Crie um sistema onde você possa conceder cartões-presente a um cliente. 
Um cliente poderá gastar qualquer valor de um cartão-presente, desde que esteja disponível.

Precisamos de uma página de administração do django para esse cliente, 
onde cada cartão-presente individual é exibido (um nome de cartão-presente, valor atual / inicial) e se o usuário clicar em um cartão-presente, 
uma janela de diálogo com o histórico de log de como esse cartão-presente foi usado é exibido: 
data hora, quantidade usada, número do pedido (este deve ser um número aleatório para este exercício).
   
As chamadas da API REST devem ser criadas para criar/atualizar e recuperar um registro de cartão-presente
Para as partes extras que não são cobertas pelo django admin, você pode usar js simples ou jquery.
"""


class GiftCards(models.Model):
    name = models.CharField(max_length=100, blank=False)
    initial_amount = models.IntegerField(default=100)
    current_amount = models.IntegerField(default=100)


class GiftCardLogs(models.Model):
    gift_card = models.ForeignKey(GiftCards, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    used_amount = models.IntegerField(default=0)
    order_number = models.CharField(max_length=255, default=uuid.uuid1())
