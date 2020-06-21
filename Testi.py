import json
def see():
    with open("Test JSON.json", 'r') as js:
        x=js.read()
        print(x)
see()
