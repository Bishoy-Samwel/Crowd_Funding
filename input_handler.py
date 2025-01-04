from validation import msg_dict

def check_valid_input(msg, valid_func, err_key ):
    while True:
        val = input(msg)
        if valid_func(val):
            return val
        print(msg_dict[err_key])