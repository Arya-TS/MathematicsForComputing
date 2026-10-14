
import time


class GameTimer:
    def __init__(self):
        self.start_time = None
        self.elapsed_before_pause = 0
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.perf_counter()
            self.running = True

    def pause(self):
        if self.running:
            self.elapsed_before_pause += (
                time.perf_counter() - self.start_time
            )
            self.running = False
            self.start_time = None

    def reset(self):
        self.start_time = None
        self.elapsed_before_pause = 0
        self.running = False

    def elapsed(self):
        total = self.elapsed_before_pause

        if self.running:
            total += time.perf_counter() - self.start_time

        return int(total)

    def formatted_time(self):
        seconds = self.elapsed()
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"