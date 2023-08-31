import tkinter as tk
from tkinter import filedialog
import vlc

class MoviePlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Player")

        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        self.create_widgets()

    def create_widgets(self):
        self.open_button = tk.Button(self.root, text="Open Movie", command=self.open_movie)
        self.open_button.pack()

        self.play_button = tk.Button(self.root, text="Play", command=self.play)
        self.play_button.pack()

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause)
        self.pause_button.pack()

    def open_movie(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.mkv *.avi *.mov")])
        if file_path:
            self.media = self.instance.media_new(file_path)
            self.player.set_media(self.media)

    def play(self):
        if self.media:
            self.player.play()

    def pause(self):
        if self.media:
            self.player.pause()

if __name__ == "__main__":
    root = tk.Tk()
    app = MoviePlayer(root)
    root.mainloop()

