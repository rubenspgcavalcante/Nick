try:
    config
except NameError:
    config = {
        "main_controller" : {
            "class": "Chat_Controller",
            "module": "Chat_Controller",
            "package": "controllers",
        }
    }