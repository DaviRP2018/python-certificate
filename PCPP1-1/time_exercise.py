class TimeManager:
    def __init__(self, hours, minutes, seconds):
        if any([hours < 0, minutes < 0, seconds < 0]):
            raise ValueError("Time cannot be negative")
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return self.format_time(self.hours, self.minutes, self.seconds)

    def __add__(self, other):
        return self._calculate_time(other, "__add__")

    def __sub__(self, other):
        return self._calculate_time(other, "__sub__")

    def _calculate_time(self, other, operator):
        self_total_seconds = self._get_total_seconds(self.hours, self.minutes, self.seconds)
        other_total_seconds = self._get_total_seconds(other.hours, other.minutes, other.seconds)
        total_seconds = getattr(self_total_seconds, operator)(other_total_seconds)

        if total_seconds < 0:
            return self.format_time(0, 0, 0)

        hours, minutes, seconds = self._transform_seconds(total_seconds)
        return self.format_time(hours, minutes, seconds)

    def format_time(self, hours, minutes, seconds):
        total_seconds = self._get_total_seconds(hours, minutes, seconds)
        hours, minutes, seconds = self._transform_seconds(total_seconds)
        seconds_str = str(seconds)
        minutes_str = str(minutes)
        hours_str = str(hours)

        if len(seconds_str) == 1:
            seconds_str = f"0{seconds_str}"
        if len(minutes_str) == 1:
            minutes_str = f"0{minutes_str}"
        if len(hours_str) == 1:
            hours_str = f"0{hours_str}"

        return f"{hours_str}:{minutes_str}:{seconds_str}"

    def _transform_seconds(self, seconds):
        hours = 0
        minutes = 0

        if seconds > 59:
            minutes += seconds // 60
            seconds = seconds % 60

        if minutes > 59:
            hours += minutes // 60
            minutes = minutes % 60

        return hours, minutes, seconds

    def _get_total_seconds(self, hours, minutes, seconds):
        return hours * 3600 + minutes * 60 + seconds


time1 = TimeManager(20, 0, 738)
print(time1)

time2 = TimeManager(5, 33, 20)
print(time2)

print(time1 + time2)
print(time1 - time2)
print(time2 - time1)

time3 = TimeManager(-5, 33, 20)
print(time3)