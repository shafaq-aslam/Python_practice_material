
# Question No 20

# 1) Define a class called Song with attributes title, artist, and duration.
# 2) Include methods to play, pause, and skip songs.
# 3) Test the methods by creating a playlist and playing songs.

class Song:

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.playing = False

    def play(self):
        if not self.playing:
            print(f'{self.title} by {self.artist}\nDuration: {self.duration}\n')
            print(f'{self.title} is playing.....')
            self.playing = True
        else:
            print(f'{self.title} by {self.artist}\nDuration: {self.duration}\n')
            print(f'{self.title} is already playing.....')

    def pause(self):
        if self.playing:
            print(f'{self.title} is paused....')
            self.playing =False
        else:
            print(f'{self.title} is already paused....')

    def skip(self):
        print(f'{self.title} skipping...')
        self.playing = False

playlist = [Song('Thriller', 'Michael Jackson', '5:57'), Song('Like a Rolling Stone', 'Bob Dylan', '6:13'),
            Song('Smells Like Teen Spirit', 'Nirvana', '5:01')]

for song in playlist:
    wantToPlay = input("Enter 'p' for play song, 'q' for pause, and 's' for skip: ")
    if wantToPlay.lower() == 'p':
        song.play()
    elif wantToPlay.lower() == 'q':
        song.pause()
    else:
        song.skip()