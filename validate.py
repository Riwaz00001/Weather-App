def get_city(city:str)->bool:
    if city=="":
        raise ValueError("City name can't be empty!")
    if any(l.isnumeric() for l in city):
        raise ValueError("City has only letters!")
    return True
