def mood_response(mood):
    if mood.lower() == 'happy':
        print("Let's have a happy and productive day!")
    elif mood.lower() == 'sad':
        print("I hope your day get's better")
    elif mood.lower() == 'excited':
        print("WOOOO!")
    else:
        print("I hope you have a great day no matter how you're feeling.")
