# labelmaker

## About
 
Labelmaker is a very simple Flask/Python3 webapp to generate/print labels and tapes with the DYMO LabelWriter® Duo 450. 
The DYMO Labelwriter® Duo 450 works well under Linux/MacOSX with CUPS.

The idea is to make a webapp that generate dynamic pdfs (in lengths) with fixed height for Tapes.
and send it to printer with the lpr command

e.g.

```
  lpr -o PageSize=9_mm__1___Label__Auto -o PrintQuality=Text text_to_print.pdf -P LabelWriter-450-DUO-Tape
```

This code should work under Linux/MacOSX with python 3.6+

```
DISCLAIMER: 

I only tested this code with 2 different Dymo models (Dymo duo 450 and the PNP).

If your label/tape printer is able using cups, it should also be possible to use this progam with small adaptions.

You are on your own with other printers, but ideas are welcome.
```

## Installation and running

* Install your CUPS drivers and plug it in.

* Edit the config.py and change the printers to your cups names.
```
    LABELPRINTER="LabelWriter-450-DUO-Label"
    TAPEPRINTER="LabelWriter-450-DUO-Tape"
```

* Install Python 3.6+ and [pipenv](https://docs.pipenv.org/en/latest/) (if you haven't already)

* Clone Repo and than run

```
git clone https://github.com/vherolf/labelmaker.git

cd labelmaker

pipenv install

bash start.sh
```

* Navigate in your favorite browser to http://localhost:5000


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


```
DISCLAIMER:

If I violate any naming convention or already reserved trade names - please let me now and I will change it.
```