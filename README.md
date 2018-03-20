# labelmaker

(only working proof of concept so far)

## About
 
Its a simple Flask webapp to generate/print labels and tapes with the DYMO LabelWriter® Duo 450. 
The DYMO Labelwriter® Duo 450 works well under Linux/MacOSX with CUPS.

Idea is to make a webapp that generate dynamic pdfs (in lengths) with fixed height for Tapes.
and send send it to printer with ldr command

e.g.

  lpr -o PageSize=9_mm__1___Label__Auto -o PrintQuality=Text text_to_print.pdf -P LabelWriter-450-DUO-Tape

This code should work under Linux and MacOSX with python 3.4+

DISCLAIMER: 

I dont have any knowledge of other label printers.

With small adaptions and depending on your labelmaker oder tape printer it should work with most DYMO printers. (I have only one so its not tested)

You are on your own with other printers, but ideas are welcome.

If I violate any naming convention or already reserved trade names - please let me now and I will change it.


## Installation and running

Install some virtual environment as venv or (ana)conda

Switch to the virtual environment and run 

pip install -r requirements.txt

bash start.sh

than go in browser to http://localhost:5000


## Goals

make code readable and comment it

Find a good python library that does most layouting for me, but is flexible

so far I have played around with.
  - matplotlib
  - weasyprint (as crazy as it sounds - most promissing aproach so far)
  - panda
  - all other that can produce pdf
  - reportlab (why is this not on first place ? HELP !)

Second step to make self centering adress labels (also pdfs)

Third step to make an API, so it can be easy called from other apps or production systems. 
Maybe deployed on a small print server (like a raspy or similar)

Fourth step would be to produce QR and barcode to add in tapes and labels.


## Credits

the idea to generate variable pdf and send it to the printer is from the perlmeister himself - Michael Schilli
http://www.linux-magazin.de/ausgaben/2015/12/perl-snapshot/

the flask stub code is from the great Miguel Grindberg (thanks alot, I love your tutorial - especially the videos)
( sorry the code will get better when I advance in your tutorial :)  ) 
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world


## Links

### the awesome flask

  http://flask.pocoo.org/


### best tutorial ever (it has even mega in the name and deserves it)

  https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world


### libraries used

  https://matplotlib.org/

  http://weasyprint.readthedocs.io/en/latest/index.html


### virtual environments

  https://docs.python.org/3/library/venv.html

  https://anaconda.org/