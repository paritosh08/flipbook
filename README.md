# flipbook
Designing a language for describing flipbooks and implementing a compiler for this language that can convert a flipbook description into a printable pdf (or a video)

### Installation
First install the dependencies.

**Windows**
```cmd
installFlipbook
```
**Linux/Ubuntu**
```sh
./installFlipbook.sh
```

### Using flipbook
Write a code and save with extension `.flip` (say `myBook.flip`)
**Syntax:**
* First line shoud define the output format (`gif/pdf`).
* Second line should define the canvas size [integers separated by space] (`<width> <height>`).
* Third line onwards define the frames in the following format:
    * `<page range> <file name> <dimension> <start coordinate> <final coordinate>`.
    * `<page range>` is integers separated by space (i.e. `1 24` means from frame 1 to 24).
    * `<file name>` is the string adderess to the image file.
    * `<dimension>` is the image dimension [integers separated by space] (`<width> <height>`).
    * `<start coordinate>` is the image's initial coordinate. [integers separated by space (0,0) is the top left corner, +x is towards the right and +y is towards the bottom] (`<x> <y>`)
    * `<final coordinate>` is the image's final coordinate following the same format as `<start coordinate>`.

Now, run the following:
**Windows**
```cmd
flip myBook.flip -o flipbook.pdf
```