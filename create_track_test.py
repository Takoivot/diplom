import sender_stand_request

import data


def get_new_track(order_response):
    return order_response.json().get("track")


data.params_get["t"] = get_new_track(sender_stand_request.order_response)


def positive_assert():
    track_response = sender_stand_request.get_order(data.params_get)
    assert track_response.status_code == 200


def test():
    order = sender_stand_request.post_new_order(data.order_body)
    data.params_get["t"] = get_new_track(order)
    print(data.params_get["t"])
    positive_assert()

# Сахбиев Артур, 21-я когорта — Финальный проект. Инженер по тестированию плюс
