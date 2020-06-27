from .extentions import db
from datetime import datetime
import string
from random import choices

from .extentions import db

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048))
    short_url = db.Column(db.String(7), unique=True)
    visits = db.Column(db.Integer, default = 0)
    date_created = db.Column(db.DateTime, default = datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_link()
    
    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=7))
        link = self.query.filter_by(short_url = short_url).first()
        if link:
            return self.generate_short_link()
        return short_url