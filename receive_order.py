# Загирный Станислав, 9-ая когорта, финальный проект. Инженер QA+
import sender_stand_request
import data

# получение трека заказа
def receive_track():
    # в переменную new_order сохраняется результат запроса на создание нового заказа
    new_order = sender_stand_request.post_new_order(data.order_body)
    # в переменную track_number сохраняется значение трек-номера
    track_number = new_order().json()["track"]
    # возвращается значение трек-номера
    return track_number
# сохраняется функция для получения трека заказа
#save = receive_track()
# вывод трека заказа на экран
#print(save)

# получение заказа по его номеру
def trackk_order_assert():
    track = receive_track()
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_NUMBER_PATH + track)
    # Проверяется, что код ответа равен 200
    assert response.status_code == 200

def test_order():
    trackk_order_assert

# Загирный Станислав, 9 когорта, финальный проект, Инженер QA+