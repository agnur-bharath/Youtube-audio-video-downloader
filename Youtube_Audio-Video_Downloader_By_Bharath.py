# Importing necessary packages 
from __future__ import unicode_literals
import tkinter as tk 
from tkinter import *
from tkinter import messagebox, filedialog
import youtube_dl
import os
from pytube import YouTube
# Defining CreateWidgets() function 
# to create necessary tkinter widgets 
def Widgets(): 
	link_label = Label(root, 
			text="YouTube Link / URL :", 
			bg="yellow") 
	link_label.grid(row=1, 
			column=0, 
			pady=5, 
			padx=5) 

	root.linkText = Entry(root, 
				width=55, 
				textvariable=video_Link) 
	root.linkText.grid(row=1, 
			column=1, 
			pady=5, 
			padx=5, 
			columnspan = 2) 

	destination_label = Label(root, 
				text="Destination Folder :", 
				bg="yellow") 
	destination_label.grid(row=2, 
			column=0, 
			pady=5, 
			padx=5) 

	root.destinationText = Entry(root, 
                                        width=45, 
					textvariable=download_Path) 
	root.destinationText.place(x=130,y=35) 

	browse_B = Button(root, 
			text="Browse", 
			command=Browse, 
			width=10, 
			bg="#05E8E0",
                        activebackground='#00FF00') 
	browse_B.place(x=420,y=35)

	Download_B = Button(root, 
			text="Download ONLY Video (MP4)", 
                        command=Download_Video, 
			width=23, 
			bg="#05E8E0",
                        activebackground='#00FF00')
	Download_B.place(x=60,y=70)

	
	Download_A = Button(root, 
			text="Download ONLY Audio (MP3)", 
			command=Download_Audio, 
			width=23, 
			bg="#05E8E0",
                        activebackground='#00FF00')
	Download_A.place(x=300,y=70)

	Download_AB=Button(root, 
			text="Download Video With Audio (MP4)", 
                        command=Download_VA, 
			width=27, 
			bg="#05E8E0",
                        activebackground='#00FF00')
	Download_AB.place(x=160,y=108)

# Defining Browse() to select a 
# destination folder to save the video 

def Browse():
	download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH") 

	download_Path.set(download_Directory)
	
# Defining Download() to download the video
def Download_VA():
        yt = YouTube(video_Link.get())

        #Showing details
        print("Title: ",yt.title)
        print("Number of views: ",yt.views)
        print("Length of video: ",yt.length)
        print("Rating of video: ",yt.rating)
        print('Ready to Download Video')
        ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio/best',
                'outtmpl':download_Path.get()+'/%(title)s'+'-video-audio'+'.%(ext)s',
        }
                      
        print('Downloading.....')
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([video_Link.get()])
        
        print('Downloaded!!')

                # Displaying the message 
        messagebox.showinfo("SUCCESSFULLY DOWNLOADED", "VIDEO WITH AUDIO SAVED IN\n"+ download_Path.get())
						
						 
def Download_Audio():
                yt = YouTube(video_Link.get())
                print("Title: ",yt.title)
                print("Number of views: ",yt.views)
                print("Length of video: ",yt.length)
                print("Rating of video: ",yt.rating)
                print('Ready to Download Audio')
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                    }],
                    'outtmpl':download_Path.get()+'/%(title)s'+'-audio'+'.%(ext)s',
                }
                      

                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                              ydl.download([video_Link.get()])

                messagebox.showinfo("SUCCESSFULLY DOWNLOADED", 
						"AUDIO SAVED IN\n"
						+ download_Path.get())


        
        
def Download_Video():
        yt = YouTube(video_Link.get())

        #Showing details
        print("Title: ",yt.title)
        print("Number of views: ",yt.views)
        print("Length of video: ",yt.length)
        print("Rating of video: ",yt.rating)
        print('Ready to Download Video')
        ydl_opts = {
                'format': 'bestvideo[ext=mp4]/137/136/best[ext=mp4]/mp4/best',
                'outtmpl':download_Path.get()+'/%(title)s'+'-video'+'.%(ext)s',
        }
                      
        print('Downloading.....')
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([video_Link.get()])
        
        print('Downloaded!!')

                # Displaying the message 
        messagebox.showinfo("SUCCESSFULLY DOWNLOADED", "VIDEO SAVED IN\n"+ download_Path.get())
                
# Creating object of tk class 
root = tk.Tk()

# Setting the title, background color 
# and size of the tkinter window and 
# disabling the resizing property 
root.geometry("600x150") 
root.resizable(False, False) 
root.title("YouTube_Video_Downloader-- Program By BHARATH") 
root.config(background="black") 

# Creating the tkinter Variables 
video_Link = StringVar() 
download_Path = StringVar() 

# Calling the Widgets() function 
Widgets() 

# Defining infinite loop to run 
# application 
root.mainloop() 
