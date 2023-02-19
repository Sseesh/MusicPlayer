from tkinter import *
import pygame
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("Music Player")
root.geometry("470x370")
root.configure(bg="#e6f5ff")

#initialize Pygame mixer
pygame.mixer.init()

#Animation
canvas = Canvas(root, bg="#e6f5ff", width=440, height=80, highlightbackground="#80aaff", highlightthicknes=2)
canvas.pack(pady=10)

def animate():
    canvas_t = canvas.create_text(220,41, text='',fill ="#80aaff",  font = "Verdana 30 bold italic")
    our_text = "MY MUSIC PLAYER"
    delta = 100
    delay = 0
    for x in range(len(our_text)+1):
        s = our_text[:x]
        new_text = lambda s=s: canvas.itemconfigure(canvas_t, text=s)
        canvas.after(delay, new_text)
        delay += delta

#Add  Songs
def add_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose a Song",
                                        filetypes=(("mp3 Files", "*.mp3"),))

    # loop thru song list and replace directory info and mp3
    for song in songs:
        song = song.replace("C:/songs/", "")
        song = song.replace(".mp3", "")
        #insert into playlist
        song_box.insert(END, song)

#delete a song
def delete_song():

    response = messagebox.askokcancel("Playlist", "Delete song from playlist?")
    if response == 1:
        song_box.delete(ANCHOR)#to delete the highlighted song
        pygame.mixer.music.stop()
    else:
        pass

# delete all songs
def  delete_songs():
    response = messagebox.askokcancel("Playlist", "Delete all songs from playlist?")
    if response == 1:
        song_box.delete(0, END)
        pygame.mixer.music.stop()
    else:
        pass

#play selected song
def play(event=""):

    song = song_box.get(ACTIVE)
    song = f'C:/songs/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

#stop playing current song
def stop(event=""):
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

#Play the next Song
def next_song(event=""):
    #get the current song tuple number
    next_one = song_box.curselection()
    #add one to the current song
    next_one = next_one[0]+1
    #grab song title from playlist
    song = song_box.get(next_one)
    #add directory structure and mp3 to song title
    song = f'C:/songs/{song}.mp3'
    #Load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    #Clear active bar in playlist listbox
    song_box.selection_clear(0, END)

    #Activate new song bar
    song_box.activate(next_one)

    # set active Bar to next song
    song_box.selection_set(next_one, last=None)

# Play prev song in playlist
def previous_song(event=""):
    # get the current song tuple number
    next_one = song_box.curselection()
    # add one to the current song
    next_one = next_one[0] - 1
    # grab song title from playlist
    song = song_box.get(next_one)
    # add directory structure and mp3 to song title
    song = f'C:/songs/{song}.mp3'
    # Load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Clear active bar in playlist listbox
    song_box.selection_clear(0, END)

    # Activate new song bar
    song_box.activate(next_one)

    # set active Bar to next song
    song_box.selection_set(next_one, last=None)

#create global pause variable
global paused
paused = False

#pause and unpause the current song
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()  # unpause
        paused = False
    else:
        pygame.mixer.music.pause()  # pause
        paused = True

#Pop-up Menu
def pop_up(e):
    remove_song_menu.tk_popup(e.x_root, e.y_root)

def dark():
    root.configure(bg="black")
    song_box.configure(bg="black", fg="#80aaff", selectbackground="#80aaff",
                   selectforeground="black", highlightbackground="#80aaff",)
    canvas.configure(bg="black")
    my_frame.configure(bg="black")
    controls_frame.configure(bg="black")
    back_button.configure(bg="black")
    forward_button.configure(bg="black")
    play_button.configure(bg="black")
    stop_button.configure(bg="black")
    add_button.configure(bg="black")
    pause_button.configure(bg="black")

def light():
    root.configure(bg="#e6f5ff")
    song_box.configure(bg="#e6f5ff", fg="black", selectbackground="#80aaff",
                       selectforeground="black", highlightbackground="#80aaff", )
    canvas.configure(bg="#e6f5ff")
    my_frame.configure(bg="#e6f5ff")
    controls_frame.configure(bg="#e6f5ff")
    back_button.configure(bg="#e6f5ff")
    forward_button.configure(bg="#e6f5ff")
    play_button.configure(bg="#e6f5ff")
    stop_button.configure(bg="#e6f5ff")
    add_button.configure(bg="#e6f5ff")
    pause_button.configure(bg="#e6f5ff")

def about():
    message = Toplevel(root)
    message.title("About")
    message.geometry("250x150")
    message.configure(bg="#e6f5ff")
    message_label = Label(message, text="----------------------------------------------", fg="black", bg="#e6f5ff",
                          highlightbackground="#80aaff", highlightthicknes=4)
    message_label.pack()
    message_label = Label(message, text=" This Music Player is a Python GUI", fg="black", bg="#e6f5ff",
                          highlightbackground="#80aaff", highlightthicknes=4)
    message_label.pack()
    message_label = Label(message, text=" Created by: Mark Dave Lorejo BSIT 1R3", fg="black", bg="#e6f5ff",
                          highlightbackground="#80aaff", highlightthicknes=4)
    message_label.pack()
    message_label = Label(message, text=" A Final Project in Computer Programming 2", fg="black", bg="#e6f5ff",
                          highlightbackground="#80aaff", highlightthicknes=4)
    message_label.pack()
    message_label = Label(message, text="----------------------------------------------", fg="black", bg="#e6f5ff",
                          highlightbackground="#80aaff", highlightthicknes=4)
    message_label.pack()

# Scrollbar
my_frame = Frame(root, bg="#e6f5ff")
my_scrollbar = Scrollbar(my_frame, orient=VERTICAL, bg="#e6f5ff")

#create playlist box
song_box = Listbox(my_frame, bg="#e6f5ff", fg="black", width=60, selectbackground="#80aaff",
                   selectforeground="white", highlightbackground="#80aaff", highlightthicknes=2, yscrollcommand=my_scrollbar.set)

#configure scrollbar
my_scrollbar.config(command=song_box.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_frame.pack()
song_box.pack(pady=20)

#define player control button images
back_btn_img = PhotoImage(file='img/play2.png')
forward_btn_img = PhotoImage(file='img/play4.png')
play_btn_img = PhotoImage(file='img/play3.png')
pause_btn_img = PhotoImage(file='img/play5.png')
stop_btn_img = PhotoImage(file='img/play1.png')
add_btn_img = PhotoImage(file='img/add.png')

#create player control frame
controls_frame = Frame(root, bg="#e6f5ff")
controls_frame.pack()

#create player control Buttons
back_button = Button(controls_frame, bg="#e6f5ff", image=back_btn_img, borderwidth=0, command=previous_song)
forward_button = Button(controls_frame, bg="#e6f5ff", image=forward_btn_img, borderwidth=0, command=next_song)
play_button = Button(controls_frame, bg="#e6f5ff", image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, bg="#e6f5ff", image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame, bg="#e6f5ff", image=stop_btn_img, borderwidth=0, command=stop)
add_button = Button(controls_frame, bg="#e6f5ff", image=add_btn_img, borderwidth=0, command=add_songs)

add_button.grid(row=0, column=0, padx=10)
back_button.grid(row=0, column=2, padx=10)
forward_button.grid(row=0, column=4, padx=10)
play_button.grid(row=0, column=3, padx=10)
pause_button.grid(row=0, column=5, padx=10)
stop_button.grid(row=0, column=1, padx=10)

#create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Menu
M_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=M_menu)
M_menu.add_command(label="Dark Mode", command=dark)
M_menu.add_command(label="Light Mode", command=light)
M_menu.add_command(label="About", command=about)
M_menu.add_command(label="Exit", command=root.quit)

# Create delete song menu
remove_song_menu = Menu(my_menu, tearoff=False)
remove_song_menu.add_command(label="Delete Song From Playlist", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs From Playlist", command=delete_songs)

#key bindings
root.bind("<space>", play)
root.bind("<Left>", previous_song)
root.bind("<Right>", next_song)
root.bind("<Control-space>", stop)
song_box.bind("<Button-3>", pop_up)

animate()
root.mainloop()





