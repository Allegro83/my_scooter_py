import configuration
import requests
import data

# создание заказа
def create_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=data.order_body)


# получение трек-номера заказа
def new_track(new_order_track):
    track_number = configuration.ORDER_NUMBER_PATH + str(new_order_track)
    return requests.get(configuration.URL_SERVICE + track_number)
