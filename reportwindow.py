from customtkinter import *
from PIL import Image
from io import BytesIO
import requests
from error import error_message
from clearwindow import clear
from back import back

_image_cache = {}

def load_weather_icon(url, size=(80, 80)):
    if url in _image_cache:
        return _image_cache[url]

    if url.startswith("//"):
        url = "https:" + url
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        pil_img = Image.open(BytesIO(response.content))
        ctk_img = CTkImage(light_image=pil_img, dark_image=pil_img, size=size)
        _image_cache[url] = ctk_img
        return ctk_img
    except (requests.exceptions.RequestException, OSError):
        return None


def stat_frame(master, label_text, value_text):
    frame = CTkFrame(master, corner_radius=10)
    CTkLabel(frame, text=label_text, font=("Arial", 14), text_color="gray70").pack(pady=(10, 0),padx=15)
    CTkLabel(frame, text=value_text, font=("Arial", 20, "bold")).pack(pady=(0, 10), padx=15)
    return frame

def report(app, city, report_info):
    clear(app)
    app.title(f"Weather of {city}")

    report_card = CTkFrame(master=app, width=520, height=520, corner_radius=16)
    report_card.place(relx=0.5, rely=0.5, anchor="center")
    report_card.pack_propagate(False)

    try:
        main_title = CTkLabel(
            master=report_card, text=f"Weather in {city}", font=("Arial", 28, "bold")
        )
        main_title.pack(pady=(25, 15))

        top_row = CTkFrame(master=report_card, fg_color="transparent")
        top_row.pack(pady=10)

        icon_img = load_weather_icon(report_info["photo"], size=(80, 80))
        if icon_img:
            icon_label = CTkLabel(master=top_row, image=icon_img, text="")
            icon_label.image = icon_img 
            icon_label.pack(side="left", padx=15)
        else:
            CTkLabel(master=top_row, text="⛅", font=("Arial", 48)).pack(
                side="left", padx=15
            )

        condition_box = CTkFrame(master=top_row, fg_color="transparent")
        condition_box.pack(side="left", padx=15)
        CTkLabel(
            master=condition_box,
            text="Current Weather",
            font=("Arial", 14),
            text_color="gray70",
        ).pack(anchor="w")
        CTkLabel(
            master=condition_box,
            text=str(report_info["weather"]),
            font=("Arial", 22, "bold"),
        ).pack(anchor="w")

        # --- Temperature frame ---
        temp_frame = CTkFrame(master=report_card, corner_radius=10)
        temp_frame.pack(pady=20, padx=30, fill="x")
        CTkLabel(
            master=temp_frame, text="Temperature", font=("Arial", 14), text_color="gray70"
        ).pack(pady=(10, 0))
        temp_row = CTkFrame(master=temp_frame, fg_color="transparent")
        temp_row.pack(pady=(0, 10))
        CTkLabel(
            master=temp_row, text=f"{report_info['celsius']}°C", font=("Arial", 26, "bold")
        ).pack(side="left", padx=20)
        CTkLabel(
            master=temp_row, text=f"{report_info['farenheit']}°F", font=("Arial", 26, "bold")
        ).pack(side="left", padx=20)

        # --- Chance frames: humidity, cloud, rain ---
        chances_row = CTkFrame(master=report_card, fg_color="transparent")
        chances_row.pack(pady=10, padx=20, fill="x")

        humid_frame = stat_frame(chances_row, "Humidity", f"{report_info['humidity']}%")
        humid_frame.pack(side="left", expand=True, fill="both", padx=5)

        cloud_frame = stat_frame(
            chances_row, "Cloud Cover", f"{report_info['chance_of_cloud']}%"
        )
        cloud_frame.pack(side="left", expand=True, fill="both", padx=5)

        rain_frame = stat_frame(
            chances_row, "Chance of Rain", f"{report_info['chance_of_rain']}%"
        )
        rain_frame.pack(side="left", expand=True, fill="both", padx=5)

        # --- Back button ---
        exit_btn = CTkButton(
            master=report_card,
            text="Back",
            fg_color="red",
            hover_color="#a30000",
            command=lambda: back(app),
            height=40,corner_radius=8
        )
        exit_btn.pack(pady=25)

    except KeyError as e:
        error_message(f"Failed to retrieve {e}")