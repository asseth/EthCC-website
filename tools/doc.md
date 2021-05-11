# Updating speakers

First download the CSV and put it in this folder (`tools`)
Then launch
```sh
python3 extract.py CSV_FILE
```

It should print the list of speakers that should be added to `speakers-json.js`

Then download the pictures of every speaker and put them (naming them accordingly) in the `images/speakers` folder.

Then use `imagemagick` to convert the images to jpg, compress them. Make sure you take a look at the built website with new pictures, as you might need to crop some of them.

Resize:
```sh
mogrify -resize 256x256 *.png
```

Format to jpg
```sh
mogrify -format jpg *.png
```
