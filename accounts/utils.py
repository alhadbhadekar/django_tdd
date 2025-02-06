from libgravatar import Gravatar

def create_avatar(email_address):
    g = Gravatar(email_address)
    return g.get_image(default="https://static.thenounproject.com/avatars/3983118/resized/260/260/b8f8b89b7054a0d6ae12ac64ee3b5e7c.png")