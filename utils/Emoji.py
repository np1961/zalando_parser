import emoji

def actual_emojies(name):
    emojize_names={
        'image' : ':framed_picture:',
        'time' : ':stopwatch:',
        'this' : '⟹',
        'True' : ':check_mark_button:',
        'False' : ':cross_mark:'
                  }
    return emoji.emojize(emojize_names[name])
