# labelmaker

## About
 
Labelmaker is a very simple Flask/Python3 webapp to generate/print labels and tapes with the DYMO LabelWriter® Duo 450. 
The DYMO Labelwriter® Duo 450 works well under Linux/MacOSX with CUPS.

Idea is to make a webapp that generate dynamic pdfs (in lengths) with fixed height for Tapes.
and send it to printer with the lpr command

e.g.

```
  lpr -o PageSize=9_mm__1___Label__Auto -o PrintQuality=Text text_to_print.pdf -P LabelWriter-450-DUO-Tape
```

This code should work under Linux/MacOSX with python 3.6+

DISCLAIMER: 

I dont have any knowledge of other label printers.

With small adaptions and depending on your label/tape printer - it should work with most DYMO printers. (I have only one, so its not tested with others)

You are on your own with other printers, but ideas are welcome.

If I violate any naming convention or already reserved trade names - please let me now and I will change it.


## Installation and running

Install your DYMO Labelwriter 450 DUO CUPS drivers and plug it in.

Install pipenv and run

```
pipenv install

bash start.sh
```
than go in browser to http://localhost:5000


## Credits

The idea to generate variable pdf and send it to the printer is from the perlmeister himself - Michael Schilli
http://www.linux-magazin.de/ausgaben/2015/12/perl-snapshot/

The flask stub code is from the great Miguel Grindberg (thanks alot, I love Your tutorial - especially the videos)
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world


## Links

### the awesome flask

  http://flask.pocoo.org/


### best tutorial ever (it has even mega in name and deserves it)

  https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world


### libraries

  https://matplotlib.org/

  http://weasyprint.readthedocs.io/en/latest/index.html


### python virtual environments

  https://docs.python.org/3/library/venv.html

  https://anaconda.org/
