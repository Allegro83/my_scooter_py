# Загирный Станислав, 9-ая когорта, финальный проект. Инженер QA+

import sender_stand_request


def post_new_order():
    new_order_track = sender_stand_request.create_new_order()
    return new_order_track.json()['track']

def test_get_order_track_success():
    new_track = post_new_order()
    rip = sender_stand_request.new_track(new_track).status_code
    exp = 200
    assert rip == exp

# Загирный Станислав, 9 когорта, финальный проект, Инженер QA+