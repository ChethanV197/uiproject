# uiproject
Imports:

tkinter: The standard GUI library for Python. It provides tools to create graphical user interfaces.
filedialog: A module within Tkinter that provides a dialog window to open and save files.
vlc: The VLC Python bindings that allow interaction with the VLC media player
Class MoviePlayer:

This class serves as the main application container. It contains methods for creating the user interface, handling media-related operations, and interacting with the VLC media player instance.
__init__ Method:

Initializes the MoviePlayer class.
Sets up the main application window (root) with the title "Movie Player".
Initializes a VLC instance and a media player instance.
create_widgets Method:

Creates the GUI components, namely the buttons for opening a movie, playing, and pausing playback.
Each button is associated with a specific command that will be executed when the button is clicked.
open_movie Method:

Opens a file dialog to select a video file with specific extensions (MP4, MKV, AVI, MOV).
If a valid file is selected, it creates a VLC media object from the chosen file and associates it with the media player.
