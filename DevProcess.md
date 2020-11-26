# flipbook
Designing a language for describing flipbooks and implementing a compiler for this language that can convert a flipbook description into a printable pdf (or a video)

## V1
Can parse the following format using python:
```html
<Canvas size>
<page range> <file name> <dimension> <start coordinate> <final coordinate>
.
.
```
eg. for the following images and `.flip` code
![Apple image](images/applePic.png =33x33)
![Isaac Newton](images/isaac-newtonPic.png =109x125)
```
500 500
1 25 applePic.png 82 82 209 0 209 105
26 35 applePic.png 82 82 209 105 239 75
36 42 applePic.png 82 82 239 75 245 75
43 49 applePic.png 82 82 245 75 300 105
50 100 applePic.png 82 82 300 105 418 418
1 100 isaac-newtonPic.png 272 313 114 187 114 187
```
Output:
![Animated GIF](images/ezgif.com-gif-maker.gif)