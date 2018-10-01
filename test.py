class Object:
    pass


def Hello(self):
    print('Hello')

obj = Object()
Object.say = Hello
obj.say()

