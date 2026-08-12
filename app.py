from customtkinter import *
from PIL import Image
from validate import get_city
from error import error_message
from weather_backend import weather
from reportwindow import *
def GUI(root):
    set_appearance_mode("dark")
    set_default_color_theme("blue")
    app = root
    app.title("Weather App")
    app.after(10,lambda :app.state('zoomed'))
    card = CTkFrame(master=app, width=360, height=320, corner_radius=16)
    card.place(relx=0.5, rely=0.5, anchor="center")
    card.pack_propagate(False)

    title = CTkLabel(
        master=card,
        text="Weather Search",
        font=("Arial", 22, "bold"),
    )
    title.pack(pady=(30, 10))

    label = CTkLabel(
        master=card,
        text="Enter city:",
        font=("Arial", 16),
    )
    label.pack(pady=(10, 5))

    entry = CTkEntry(
        master=card,
        placeholder_text="e.g. Kathmandu",
        width=260,
        height=40,
        corner_radius=8,
    )
    entry.pack(pady=5)

    img = Image.open("search.png")
    search_icon = CTkImage(light_image=img, dark_image=img, size=(20, 20))

    def on_search():
        try:
            city:str = entry.get()
            result=get_city(city)
            if result:
                report_info=weather(city)
                if report_info:
                    report(app,city,report_info)
        except ValueError as e:
            error_message(e)

    btn = CTkButton(
        master=card,
        text="Search",
        image=search_icon,
        compound="left",   
        corner_radius=8,
        width=180,
        height=40,
        command=on_search,     
    )
    btn.pack(pady=(20, 10))

    app.mainloop()


if __name__ == "__main__":
    root=CTk()
    root.title("Weather App")
    root.after(10,lambda :root.state('zoomed'))
    GUI(root)