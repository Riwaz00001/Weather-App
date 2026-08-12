from customtkinter import *
from PIL import Image
from io import  BytesIO
import requests
from error import error_message
from clearwindow import clear
from back import back
def report(app,city,report_info):
    clear(app)
    app.title(f"Weather of {city}")
    report_card=CTkFrame(master=app,width=720,height=720,corner_radius=16)
    report_card.place(relx=0.5,rely=0.5,anchor="center")
    report_card.pack_propagate(False)
    main_title=CTkLabel(master=report_card,text=("Weather"),font=("Arial",40))
    main_title.pack(pady=20)
    #labeling the image
    try:
        Weather=CTkLabel(master=report_card,text=("Current weather: "),font=("Arial",24))
        Weather.pack(pady=60)
        #label it to the right of weather label
        condition=CTkLabel(master=report_card,text=(f"{report_info["weather"]}"),font=("Arial",24))
        condition.pack(pady=70)
        """
        try:
            response=requests.get(report_info["photo"])
            if response.status_code!=200:
                error_message(f"Failed to load image. status code:{response.status_code}")
            img=Image.open(BytesIO(response.content))
            weather_img=CTkImage(dark_image=img,size=(30,30))
            label = CTkLabel(master=report_card, image=img, text="")
            label.pack(pady=50)
        except FileNotFoundError:
            error=CTkLabel(master=report_card,text="Failed to load Image",font=("Arial",24))
            error.pack(pady=50)
        """
        #fetching and labeling temperature

        TempC=CTkLabel(master=report_card,text=(f"{report_info["celsius"]}"),font=("Arial",24))
        TempC.place(x=20,y=40)
        TempF=CTkLabel(master=report_card,text=(f"{report_info["farenheit"]}"),font=("Arial",24))
        TempF.place(x=40,y=50)

        #humidity
        humid=CTkLabel(master=report_card,text=(f"{report_info["humidity"]}"),font=("Arial",24))
        humid.pack(pady=90)

        #chance of cloud
        cloud_chance=CTkLabel(master=report_card,text=(f"{report_info["chance_of_cloud"]}"),font=("Arial",24))
        cloud_chance.pack(pady=70)

        #chance of rain
        rain_chance=CTkLabel(master=report_card,text=(f"{report_info["chance_of_rain"]}"),font=("Arial",24))
        cloud_chance.pack(pady=70)

        #exit button
        exit_btn=CTkButton(master=report_card,text=("Back",20),bg_color="red",command=lambda:back(app))
        exit_btn.place(x=100,y=90)
    except KeyError as e:
        error_message(f"Failed to retrieve {e}")