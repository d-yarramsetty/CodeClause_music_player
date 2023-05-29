import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Music Player")
        self.playlist = []
        self.current_index = 0
        self.paused = False

        # Initialize mixer
        mixer.init()

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Playlist label
        playlist_label = tk.Label(self.window, text="Playlist:")
        playlist_label.pack()

        # Playlist listbox
        self.playlist_listbox = tk.Listbox(self.window, width=50)
        self.playlist_listbox.pack()

        # Add Button
        add_button = tk.Button(self.window, text="Add", command=self.add_song)
        add_button.pack()

        # Play Button
        play_button = tk.Button(self.window, text="Play", command=self.play_song)
        play_button.pack()

        # Pause Button
        pause_button = tk.Button(self.window, text="Pause", command=self.pause_song)
        pause_button.pack()

        # Next Button
        next_button = tk.Button(self.window, text="Next", command=self.next_song)
        next_button.pack()

    def add_song(self):
        filetypes = (("Audio Files", "*.mp3;*.wav"), ("All Files", "*.*"))
        selected_files = filedialog.askopenfilenames(filetypes=filetypes)

        for file in selected_files:
            self.playlist.append(file)
            self.playlist_listbox.insert(tk.END, os.path.basename(file))

    def play_song(self):
        if self.paused:
            mixer.music.unpause()
            self.paused = False
        else:
            if len(self.playlist) > 0:
                song_path = self.playlist[self.current_index]
                mixer.music.load(song_path)
                mixer.music.play()

    def pause_song(self):
        if mixer.music.get_busy():
            mixer.music.pause()
            self.paused = True

    def next_song(self):
        if self.current_index < len(self.playlist) - 1:
            self.current_index += 1
        else:
            self.current_index = 0

        self.play_song()

    def run(self):
        self.window.mainloop()

# Create and run the music player
music_player = MusicPlayer()
music_player.run()
