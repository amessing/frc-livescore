class Alliance:
    def __init__(self, score=None, teams=[]):
        print 'score'
        print score
        if score:
            print score.isdigit()
        self.score = int(score) if score is not None and score.isdigit() else None
        self.teams = teams


class OngoingMatchDetails:
    def __init__(self, match=None, time=None, red=Alliance(), blue=Alliance()):
        print 'time'
        print time
        print time.isdigit()
        self.match = match
        self.time = int(time) if time is not None and time.isdigit() else None
        self.red = red
        self.blue = blue
