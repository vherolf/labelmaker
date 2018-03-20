# labelmaker

## About

 
Its a simple Flask webapp to generate/print labels and tapes with the DYMO LabelWriter® Duo 450.
The DYMO Labelwriter® Duo 450 works well under Linux/MacOSX with with CUPS.

Idea is to make a webapp that generate dynamic pdfs (in lengths) with fixed height for Tapes.
and send send it to printer with ldr command

e.g.

  lpr -o PageSize=9_mm__1___Label__Auto -o PrintQuality=Text text_to_print.pdf -P LabelWriter-450-DUO-Tape

This code should work under Linux and MacOSX with python 3.4+

## Goals

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

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
http://weasyprint.readthedocs.io/en/latest/index.html
