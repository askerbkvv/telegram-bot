import telegram


def main_menu_keyboard():
    keyboard=()
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
)


