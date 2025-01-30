from dsa.queue import list_queue
from random import randint

from dsa.queue.list_queue import ListQueue


class Track:
    def __init__(self, title):
        self.title = title
        self.length = randint(5, 10)

    def __str__(self):
        return f"Track {self.title}-{self.length}"

import time

class MediaPlayerQueue(ListQueue):
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()

    def add_track(self, track):
        self.enqueue(track)

    def play(self):
        while self.size > 0:
            current_track_node = self.dequeue()
            print("Now playing {}".format(current_track_node.title))
            time.sleep(current_track_node.length)

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        """Returns a string representation of the queue."""
        if self.is_empty():
            return "[]"
        elements = [str(track) for track in self.queue]
        return "[" + ",\n".join(elements) + "]"

track1 = Track("white whistle")
track2 = Track("butter butter")
track3 = Track("Oh black star")
track4 = Track("Watch that chicken")
track5 = Track("Don't go")
media_player = MediaPlayerQueue()

media_player.add_track(track1)
media_player.add_track(track2)
media_player.add_track(track3)
media_player.add_track(track4)
media_player.add_track(track5 )

print(f'media_player {media_player}')
media_player.play()
