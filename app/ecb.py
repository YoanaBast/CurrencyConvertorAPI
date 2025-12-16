import requests
import xml.etree.ElementTree as ET

ECB_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"

def fetch_ecb_rates():
    response = requests.get(ECB_URL)
    response.raise_for_status()  # fail if request fails

    root = ET.fromstring(response.content)
    ns = {"gesmes": "http://www.gesmes.org/xml/2002-08-01",
          "def": "http://www.ecb.int/vocabulary/2002-08-01/eurofxref"}

    # Find the Cube with time/rates
    cube = root.find(".//def:Cube/def:Cube", ns)
    rates = {"EUR": 1.0}  # base currency
    for rate in cube.findall("def:Cube", ns):
        currency = rate.attrib["currency"]
        value = float(rate.attrib["rate"])
        rates[currency] = value
    return rates

if __name__ == "__main__":
    rates = fetch_ecb_rates()
    print(rates)
