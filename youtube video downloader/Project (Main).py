from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube 

Folder_Name = ""

#this section is for file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")

#for downloading video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Sorry Your Link Is Wrong\nPaste correct Link !!",fg="red")


    #for download function
    select.download(Folder_Name)
    ytdError.config(text="Download Successful \nENJOY!!")



root = Tk()
root.title("YOUTUBE VIDEO DOWNLOADER")
root.geometry("400x500") #set window
root.columnconfigure(0,weight=1)#set all content in center.

#Ytd Link Label
ytdLabel = Label(root,text="Enter the URL of the Video",fg="blue",font=("jost",15))
ytdLabel.grid()

#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

#Error Msg
ytdError = Label(root,text="Error URL",fg="red",font=("jost",10))
ytdError.grid()

#Asking save file label
saveLabel = Label(root,text="Save the Video File",font=("jost",15,"bold"))
saveLabel.grid()

#btn of save file
saveEntry = Button(root,width=10,bg="green",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid()

#Error Msg location
locationError = Label(root,text="Error URL of Path",fg="red",font=("jost",10))
locationError.grid()

#Download Quality
ytdQuality = Label(root,text="Select Quality",font=("jost",15))
ytdQuality.grid()

#combobox
choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

#donwload btn
downloadbtn = Button(root,text="Download",width=15,bg="green",fg="white",command=DownloadVideo)
downloadbtn.grid()

#developer Label
developerlabel = Label(root,text="\n\n Made By \nRICHA SHARMA",font=("jost",15))
developerlabel.grid()
root.mainloop()
