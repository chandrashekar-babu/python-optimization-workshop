class CommandDispatch:
    def __init__(self, config):
        self.config = config
        self.dispatch = {}

    def for_command(self, command):
        def decorate(fn):
            self.dispatch[command] = fn
        return decorate

    def invalid(self, fn):
        self.invalidfn = fn

    def input(self, fn):
        self.inputfn = fn

    def run(self):
        while True:
            args = self.inputfn(self.config)
            self.dispatch.get(args[0], self.invalidfn)(*args)
            
