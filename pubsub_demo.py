from pubsub import PubSub

ps = PubSub()


def connect(host, port):
    print(f"Establishing connection to {host}:{port}...")
    ps.publish("connected", "john", "secret")

@ps.subscribe("connected")    
def authenticate(username, password):
    print(f"Authenticating {username}")
    ps.publish("authenticated")

@ps.subscribe("authenticated")
def switch_to_secure_channel():
    print(f"Switching to secure channel...")


connect("localhost", 8080)
