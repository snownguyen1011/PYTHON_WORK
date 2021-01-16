class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print ("{} got message {}".format (self.name, message))


class Publisher:
    def __init__(self, events):
        self.subscribers = {event: dict () for event in events}

    def get_subscribers(self, event):
        return self.subscribers[event]

    def register(self, event, who, callback=None):
        if callback is None:
            callback = getattr (who, 'update')
        self.get_subscribers (event)[who] = callback

    def unregister(self, event, who):
        del self.get_subscribers (event)[who]

    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers (event).items ():
            callback (message)


pub = Publisher (['Lunch', 'Dinner'])
print (pub.subscribers)

Ravi = Subscriber ('Ravi')
Snow = Subscriber ('Snow')

pub.register ('Lunch', Snow, None)
print (pub.subscribers)

pub.dispatch ('Lunch', "It's Lunch time")

pub.register ('Lunch', Ravi, None)

pub.dispatch ('Lunch', "It's Lunch time")
