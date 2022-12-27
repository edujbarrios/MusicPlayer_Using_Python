import pygame

class MusicPlayer:
    def __init__(self, tracks):
        """Initialize the player with a list of tracks."""
        self.tracks = tracks
        self.current_track_index = 0
        pygame.init()
        pygame.mixer.init()

    def play(self):
        """Play the current track."""
        pygame.mixer.music.load(self.tracks[self.current_track_index])
        pygame.mixer.music.play()

    def pause(self):
        """Pause the current track."""
        pygame.mixer.music.pause()

    def stop(self):
        """Stop the current track."""
        pygame.mixer.music.stop()

    def next_track(self):
        """Skip to the next track."""
        self.stop()
        self.current_track_index = (self.current_track_index + 1) % len(self.tracks)
        self.play()

    def previous_track(self):
        """Skip to the previous track."""
        self.stop()
        self.current_track_index = (self.current_track_index - 1) % len(self.tracks)
        self.play()

    def set_volume(self, volume):
        """Set the volume of the player."""
        pygame.mixer.music.set_volume(volume)

    def get_current_track(self):
        """Return a tuple with the title and artist of the current track."""
        track = self.tracks[self.current_track_index]
        # Get the title and artist from the track's metadata
        title = track.metadata["title"]
        artist = track.metadata["artist"]
        return (title, artist)

# Create a list of tracks
tracks = [Track("song1.mp3"), Track("song2.mp3"), Track("song3.mp3")]

# Create the player and play the first track
player = MusicPlayer(tracks)
player.play()

# Pause the player
player.pause()

# Skip to the next track
player.next_track()

# Set the volume to 50%
player.set_volume(0.5)

# Get the current track's title and artist
title, artist = player.get_current_track()
print(f"Now playing: {title} by {artist}")
