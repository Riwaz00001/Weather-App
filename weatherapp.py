import requests,os
from dotenv import load_dotenv
from validate import get_city
def main():
    load_dotenv()
    url="http://api.weatherapi.com/v1/current.json"
    try:
        API_KEY=os.environ["WEATHER_API_KEY"]
    except KeyError:
        print(" API key not Found. Check .env file")
        return
    city=get_city()
    if city:
        try:
            response=requests.get(url,params={"key":API_KEY,"q":city},timeout=5)
        except requests.exceptions.ConnectionError:
            print("No internet!!!")
            return
        except requests.exceptions.Timeout:
            print("Request Timeout!!!.Try again!!")
            return
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return
        try:
            data=response.json()
        except requests.exceptions.JSONDecodeError:
            print("Recieved invalid response from server!!")
            return
        if response.status_code!=200:
            error_message = data.get("error", {}).get("message", "Unknown error occurred")
            print(f"API Error: {error_message}")
            return
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
    else:
        print("Enter valid City!!!")
if __name__=="__main__":
    main()