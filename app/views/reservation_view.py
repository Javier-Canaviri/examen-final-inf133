def render_reservation_list(reservations):
    return [
        {
            "id": reservation.id,
            "user_id": reservation.user_id,
            "reservation_id": reservation.reservation_id,
            "reservation_date": reservation.reservation_date,
            "num_guest": reservation.num_guest,
            "special_request": reservation.special_request,
            "status": reservation.status,
            
        }
        for reservation in reservations
    ]

def render_reservation_detail(reservation):
    return {
        "id": reservation.id,
        "name": reservation.name,
        "address": reservation.address,
        "city": reservation.city,
        "phone": reservation.phone,
        "description": reservation.description,
        "rating": reservation.rating,
    }