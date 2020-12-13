import pandas
from geopy.geocoders import Nominatim


def coords_finder(filename):
    """
    Finds and adds latitude and longitude to the file. Also saves it as Nice.csv
    :param filename: a path to file
    :return: if no problem: (True, HTML repr of df)
             else: (False, Error string to show on page)
    """
    try:
        df = pandas.read_csv(filename)
    except Exception as e:
        print(str(e))
        return False, "Can't open Your file. Please ensure, You are uploading a valid .csv file"

    if not ("Address" in df or "address" in df):
        return False, 'No address column. Please ensure, Your file has a column "Address" or "address"'

    def apply_address(address):
        return Nominatim(user_agent="agent").geocode(address, timeout=None)

    df["coords"] = df.Address.apply(apply_address)
    df["Latitude"] = df.coords.apply(lambda x: x.latitude if x is not None else None)
    df["Longitude"] = df.coords.apply(lambda x: x.longitude if x is not None else None)

    del df['coords']
    if "Unnamed: 0" in df:
        del df['Unnamed: 0']

    try:
        df.to_csv('Nice.csv')
    except:
         return False, "Can't proceed this file"

    return True, df.to_html(max_rows=10, max_cols=8, classes="table")


if __name__ == '__main__':
    trying, message = coords_finder("Sample.csv")
    print(trying, message)
