# -- coding: utf-8 --
def function():
    text = input()
    new_text = ''
    for a in text:
        if a.upper():
            new_text += a.lower()
    print(new_text)
function()