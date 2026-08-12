import requests,os
from dotenv import load_dotenv
from validate import get_city
from error import error_message
def weather(city):
    load_dotenv()
    url="http://api.weatherapi.com/v1/current.json"
    global error_message
    try:
        API_KEY=os.environ["WEATHER_API_KEY"]
    except KeyError:
        error_message(" API key not Found. Check .env file")
    try:
        response=requests.get(url,params={"key":API_KEY,"q":city},timeout=5)
    except requests.exceptions.ConnectionError:
        error_message("No internet!!!")
        return False
    except requests.exceptions.Timeout:
        error_message("Request Timeout!!!.Try again!!")
        return False
    except requests.exceptions.RequestException as e:
        error_message(f"Error: {e}")
        return False
    try:
        data=response.json()
    except requests.exceptions.JSONDecodeError:
            error_message("Recieved invalid response from server!!")
            return False
    if response.status_code!=200:
        message = data.get("error", {}).get("message", "Unknown error occurred")
        error_message(f"API Error: {message}")
        return False
    current=data.get("current")
    temp_c=current.get("temp_c")
    temp_f=current.get("temp_f")
    condition=data.get("current").get("condition")
    weather_condition=condition.get("text")
    img=condition.get("icon")
    humidity=current.get("humidity")
    cloud=current.get("cloud")
    rain=current.get("chance_of_rain")
    print(f"Weather of {city} is: ")
    print(f"Temperature in C:{temp_c}")
    print(f"Temperature in F:{temp_f}")
    print("Condition is:")
    print(f"Weather: {weather_condition}")
    print(f"Image: {img}")
    print(f"Humidity: {humidity}%")
    print(f"Cloud: {cloud}%")
    print(f"Chance of Rain: {rain}%")
    if img.startswith("//"):
        img="https:"+img
    print(img)
    result={"celsius":temp_c,
            "farenheit":temp_f,
            "weather":weather_condition,
            "photo":img,
            "humidity":humidity,
            "chance_of_cloud":cloud,
            "chance_of_rain":rain}
    return result
if __name__=="__main__":
    weather()