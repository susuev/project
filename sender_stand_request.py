import configuration
import requests
import data

# функция для создания заказа
def create_order(order_body):
   return requests.post(configuration.URL_SERVICE + configuration.CREAT_ORDERS,
                         json=order_body)

# Запрос на получение трека
def getting_a_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK + str(track))