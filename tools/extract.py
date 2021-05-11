import argparse
import csv
import json

parser = argparse.ArgumentParser(description='Extract speakers from CSV')
parser.add_argument('file', type=str, help='CSV file of the speakers')

args = parser.parse_args()

def is_accepted(row):
    try:
        return int(row[0]) == 1
    except:
        return False

def email_sent(row):
    return row[10].strip() == "Yes"

def already_on_website(row):
    return row[11].strip() == "Yes"

def should_add_to_site(row):
    return is_accepted(row) and email_sent(row) and (not already_on_website(row))

def get_link(string):
    if not string:
        return False
    stripped = string.strip()
    if stripped.startswith("https://"):
        return stripped
    handle = stripped
    if handle[0] == '@':
        handle = handle[1:]
    return "https://twitter.com/{}".format(handle)

def get_name(string):
    return string.strip().capitalize()


def create_entry(row):
    company = row[5]
    first_name = get_name(row[2])
    last_name = get_name(row[1])
    link = get_link(row[8])
    picture = "images/speakers/{}_{}.jpg".format(first_name, last_name)
    entry = { "company": company,
                "first_name": first_name,
                "last_name": last_name,
                "link": link,
                "picture": picture
    }
    return entry

with open(args.file, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    array = []
    iter_rows = iter(reader)
    next(iter_rows)
    for row in iter_rows:
        if should_add_to_site(row):
            entry = create_entry(row)
            array.append(entry)
    print(json.dumps(array, indent=4))