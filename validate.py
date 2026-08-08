def get_city():
    try:
        city=input("Enter City: ").strip()
        if city=="":
            return None
        return city
    except ValueError:
        return None
