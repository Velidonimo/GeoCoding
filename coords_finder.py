import pandas
from geopy.geocoders import Nominatim


def coords_finder(filename):
    try:
        df = pandas.read_csv(filename)
    except:
        return False, "Can't open Your file. Please ensure, You are uploading a .csv file"

    if not ("Address" in df or "address" in df):
        return False, 'No address column. Please ensure, Your file has a column "Address" or "address"'

    df["coords"] = df.Address.apply(Nominatim(user_agent="agent").geocode)
    df["Latitude"] = df.coords.apply(lambda x: x.latitude if x != None else None)
    df["Longitude"] = df.coords.apply(lambda x: x.longitude if x != None else None)

    del df['coords']
    if "Unnamed: 0" in df:
        del df['Unnamed: 0']

    try:
        df.to_csv('Nice.csv')
    except PermissionError:
        return (False, "Can't save the file")

    return True, "OK"


if __name__ == '__main__':
    trying, message = coords_finder("Sample.csv")
    print(trying, message)
