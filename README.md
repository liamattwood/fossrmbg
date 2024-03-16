# FOSSRMBG

FOSSRMBG is a website that removes backgrounds from images. 

This website is writen using Flask for the web server and rembg for the library that removes backgrounds off images.

I started this project as I found there were only a few websites that removed backgrounds and none of them were open source.

The one I was using previously: (remove.bg)[https://remove.bg] was propriatary and had a expensive API. I knew I could do better.

## Demo

In this demo I upload a simple image of some flowers in a vase with an annoying blue background.
I simply upload the image from my machine and click the button. The website then displays the image with the removed and transperent background.

[screenshot](demo/demo.gif)

Original image:

[screenshot](demo/flowers.png)

## Setup 

```
pip install -r requirements.txt
python main.py
```

I've even attached a `dockerfile` so you can easily use containers to host this!
