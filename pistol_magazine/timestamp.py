from datetime import datetime, timedelta

from pistol_magazine.base import _BaseField


class Timestamp(_BaseField):
    D_TIMEE9 = 9
    D_TIMEE6 = 6
    D_TIMEE3 = 3
    D_TIMEE0 = 0

    def __init__(self, times: int or str = D_TIMEE9, **kwargs):
        self.start = datetime.now()
        self.times = int(times)
        if not kwargs:
            self.kwargs = {"milliseconds": 1}
        else:
            self.kwargs = kwargs

    def mock(self):
        self.start += timedelta(**self.kwargs)
        return int(self.start.timestamp() * (10 ** self.times))

    @classmethod
    def match(cls, value):
        now = datetime.now()
        start = now - timedelta(weeks=100)
        end = now + timedelta(weeks=100)
        for times in cls.defined_list:
            try:
                timestamp = value / (10 ** times)
                if timestamp > 1:
                    date = datetime.fromtimestamp(timestamp)
                    if start < date < end:
                        return times

            except (ValueError, OSError):
                pass

    def to_str(self):
        return "_".join([type(self).__name__, str(self.times)])



