import random


def handle_response(message) -> str:
    x_message = message.lower()

    if x_message == '!help':
        return "`No new features yet.`"

    if x_message == '!roll':
        return str(random.randint(1, 6))

    if x_message == '!hi':
        return 'Whats up!'

    if x_message == '!Kenya':
        return "`Lion King`"

    # this will always trigger your bot everytime it does not understand you.

    # return "Select !help, !roll or !hi for now"
