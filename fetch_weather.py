import os
import urllib.parse
import json
import urllib.request

LAT = os.getenv("LATITUDE");
LON = os.getenv("LONGITUDE");
ENDPOINT=os.getenv("ENDPOINT");

def main():

 api_key=os.getenv("OPENWEATHERMAP_API_KEY");

 if not api_key:
   raise SystemExit("ERROR: OPENWEATHERMAP API KEY is not set");
 
 params = {
  "lat":str(LAT),
  "lon":str(LON),
  "appid":api_key,
  }

 url = ENDPOINT +"/data/2.5/weather?"+urllib.parse.urlencode(params)

 print("The endpoint is ", url);

 with urllib.request.urlopen(url,timeout=10) as r:
   data = json.loads(r.read().decode("utf-8"))

 print("API Repsonse", data);


if __name__ == "__main__":
  main()


