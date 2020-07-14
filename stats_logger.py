import os.path
from os import path
import json, string
import random
import datetime

class StatsLogger:
    def __init__(self, filename: str):
        self.filename = filename
        self.try_load_stats()

    def try_load_stats(self):
        if not path.exists(self.filename):
            self.stats = {'users':{}, 'days':{}}
        else:
            with open(self.filename, 'r') as fp:
                self.stats = json.load(fp)

    def save(self):
        with open(self.filename, 'w') as fp:
            json.dump(self.stats, fp)

    def new_request(self, user):
        usr = {
        'name': user.name,
        'usr_id':user.id,
        'id':randomString()
        # 'username': user.username,
        # 'first_name': user.first_name,
        # 'last_name': user.last_name,
        # 'full_name': user.full_name,
        }

        if user.id not in self.stats['users']:
            self.stats['users'][user.id] = usr

        date_today = datetime.date.today().strftime("%Y-%m-%d")

        if date_today not in self.stats['days']:
            self.stats['days'][date_today] = 1
        else:
            self.stats['days'][date_today] += 1

        self.save_to_file()

    def get_top(self):
        users_count = len(self.stats['users'])

        top_days = list(self.stats['days'].items())[::-1]
        top_days = top_days[:7]

        return users_count, top_days

def randomString(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choices(letters, k=string_length))