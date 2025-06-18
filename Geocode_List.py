import pandas as pd
import requests
import re
import time
from urllib.parse import quote

def get_coords_from_wikipedia(query):
    search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={quote(query)}&utf8=&format=json"
    search_resp = requests.get(search_url).json()
    if not search_resp["query"]["search"]:
        return None, None

    page_title = search_resp["query"]["search"][0]["title"]
    page_url = f"https://en.wikipedia.org/wiki/{quote(page_title)}"
    page_resp = requests.get(page_url)

    dms_match = re.search(
        r'(\d{1,3})[°:] ?(\d{1,2})[′:\'] ?(\d{1,2}(?:\.\d+)?|)?[″\"]? ?([NS])'
        r'.*?(\d{1,3})[°:] ?(\d{1,2})[′:\'] ?(\d{1,2}(?:\.\d+)?|)?[″\"]? ?([EW])',
        page_resp.text, re.DOTALL
    )
    
    if dms_match:
        lat_deg = int(dms_match[1])
        lat_min = int(dms_match[2])
        lat_sec = float(dms_match[3]) if dms_match[3] else 0
        lat_dir = dms_match[4]

        lon_deg = int(dms_match[5])
        lon_min = int(dms_match[6])
        lon_sec = float(dms_match[7]) if dms_match[7] else 0
        lon_dir = dms_match[8]

        lat = lat_deg + lat_min / 60 + lat_sec / 3600
        lon = lon_deg + lon_min / 60 + lon_sec / 3600
        if lat_dir == 'S':
            lat = -lat
        if lon_dir == 'W':
            lon = -lon

        return round(lat, 6), round(lon, 6)

    return None, None

input_file = "Harshvardhan.xlsx"
df = pd.read_excel(input_file)

df["Latitude"] = None
df["Longitude"] = None

for idx, row in df.iterrows():
    query = f"{row['Name']}, {row['District']}, {row['State']}"
    print(f"[{idx+1}] Looking up: {query}")
    lat, lon = get_coords_from_wikipedia(query)
    print(f"    → Found coordinates: {(lat, lon)}")
    df.at[idx, "Latitude"] = lat
    df.at[idx, "Longitude"] = lon
    time.sleep(1.5)

df.to_csv("Harshvardhan_coords.csv", index=False)
print("\n✅ All done! Coordinates saved to 'Harshvardhan_coords.csv'")
