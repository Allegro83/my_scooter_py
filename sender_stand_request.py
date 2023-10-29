import configuration
import requests
import data


# создание заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body)

# response = post_new_order(data.order_body)
# print(response.json())


