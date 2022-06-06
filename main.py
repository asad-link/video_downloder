from tkinter import *
from pytube import YouTube as YT
window = Tk()
window.geometry("800x500")
window.title("2k19 Youtube Downloader")
Label(window, text="Paste your link", font='arial 20 bold', bg="yellow").pack()
entryData = StringVar()
Entry(window, width=40, textvariable=entryData).pack()
def download():
    link = YT(str(entryData.get()))
    format = link.streams.filter(progressive=True, file_extension="mp4")
    video = format.first()
    video.download()
Button(window, text="Click me!", command=download).pack()

window.mainloop()
