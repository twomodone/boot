def should_serve_customer(customer_age, on_break, time):
    if (customer_age < 21 or on_break or (time < 5 or time > 10)):
        return False
    return True
