#from collections import defaultdict

class PubSub:
    def __init__(self):
        self.channels = {}
        #self.channels = defaultdict(list)

    def subscribe(self, event):
        def decorate(fn):
            self.channels.setdefault(event, []).append(fn)
            # self.channel[event].append(fn)
        return decorate
    
    def publish(self, event, *args, **kwargs):
        for fn in self.channels[event]:
            fn(*args, **kwargs)
        


    