import sys
import json
import argparse

parser = argparse.ArgumentParser(description='Checks for unicity amongst the speakers')
parser.add_argument('file', type=str, help='speakers-json.js file')

args = parser.parse_args()

print("Speakers appearing twice in the list:")
with open(args.file, 'r') as jsfile:
    content = jsfile.read()
    start = (content.find('['))
    speakers = json.loads(content[start:])
    unique = set()
    for speaker in speakers:
        name = speaker['first_name'] + " " + speaker['last_name']
        if name in unique:
            print(name)
        else:
            unique.add(name)
        