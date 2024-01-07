import os
import pygame
from tkinter import filedialog
from tkinter import Tk, Button, Label, Listbox

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")
        self.master.geometry("400x300")

        self.playlist = Listbox(self.master, selectmode='SINGLE', bg="lightgray", selectbackground="darkblue")
        self.playlist.pack(pady=20)

        self.load_button = Button(self.master, text="Load Songs", command=self.load_songs)
        self.load_button.pack(pady=10)

        self.play_button = Button(self.master, text="Play", command=self.play)
        self.play_button.pack(pady=10)

        self.pause_button = Button(self.master, text="Pause", command=self.pause)
        self.pause_button.pack(pady=10)

        self.stop_button = Button(self.master, text="Stop", command=self.stop)
        self.stop_button.pack(pady=10)

        self.current_song_label = Label(self.master, text="")
        self.current_song_label.pack()

        pygame.init()
        pygame.mixer.init()

    def load_songs(self):
        directory = filedialog.askdirectory()
        if directory:
            os.chdir(directory)
            song_list = [file for file in os.listdir(directory) if file.endswith((".mp3", ".wav"))]
            for song in song_list:
                self.playlist.insert(0, song)

    def play(self):
        selected_song = self.playlist.get(self.playlist.curselection())
        if selected_song:
            pygame.mixer.music.load(selected_song)
            pygame.mixer.music.play()
            self.current_song_label.config(text=f"Now Playing: {selected_song}")

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()
        self.current_song_label.config(text="")

if __name__ == "__main__":
    root = Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
