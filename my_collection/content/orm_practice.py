from models import Game


class TestManager:

    def __init__(self):
        self.objects = []

    def all(self):
        return self.objects

    def filter(self, **kwargs):
        return [
            obj for obj in self.objects if all(getattr(obj, k) == v for k, v in kwargs.items())
        ]

    def get(self, **kwargs):
        matches = self.filter(**kwargs)
        if len(matches) == 1:
            return matches[0]
        elif len(matches) == 0:
            raise Game.DoesNotExist('Game matching query does not exist.')
        else:
            raise Game.MultipleObjectsReturned('get() returned more than one Game -- it returned {}!'.format(len(matches)))

    def create(self, **kwargs):
        game = Game(**kwargs)
        self.objects.append(game)
        return game


Game.objects = TestManager()
