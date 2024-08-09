import xml.etree.ElementTree as ET


titles = ["company", "last", "change", "min", "max"]

try:
    parser = ET.parse("nyse/nyse.xml")
except FileNotFoundError:
    print("File not found")
except ET.ParseError:
    print("Parsing error")
except Exception as e:
    print("Please try again")

root = parser.getroot()

for title in titles:
    if title == "company":
        print(title.upper().ljust(40, " "), end="")
    elif title == "max":
        print(title.upper().ljust(40, " "))
    else:
        print(title.upper().ljust(10, " "), end="")

print("-" * 90)

for quote in root.findall("quote"):
    print(quote.text.ljust(40, " "), end="")
    for key, value in quote.attrib.items():
        if key == "max":
            print(value.ljust(10, " "))
        else:
            print(value.ljust(10, " "), end="")