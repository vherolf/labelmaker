from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import  LabelForm, TapeForm
import subprocess

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/label', methods=['GET', 'POST'])
def label():
    form = LabelForm()
    if form.validate_on_submit():
        flash('printing label: {}'.format(form.labeltext.data))
        printLabel(form.labeltext.data, form.generate_pdf_only.data)
        return redirect(url_for('label'))
    return render_template('label.html', title='Print Label', form=form)

@app.route('/tape', methods=['GET', 'POST'])
def tape():
    form = TapeForm(tapewidth='12')
    if form.validate_on_submit():
        flash('printing tape: {} on {}'.format(form.tapetext.data, form.tapewidth.data))
        printTape(form.tapetext.data, form.generate_pdf_only.data, form.tapewidth.data)
        return redirect(url_for('tape'))
    return render_template('tape.html', title='Print Tape', form=form)


from matplotlib import pyplot as plot
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.font_manager import FontProperties
from matplotlib.cbook import get_sample_data
import matplotlib.pyplot as plt

from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

def printLabel( text_to_print = '', generate_pdf_only=True ):
    font_config = FontConfiguration()
    print(text_to_print)
    textsize = str(len( text_to_print.splitlines() )+1)
    textInHtml = '<h'+ textsize + '><pre>'
    for line in text_to_print.splitlines():
        textInHtml=textInHtml + line + '<br />'
    textInHtml = textInHtml + '</pre></h'+ textsize + '>'
    print(textInHtml)
    html = HTML(string=textInHtml)
    css = CSS(string='''
        @page {
              size: 3.5in 0.9in;
              margin: 0em;
              margin-bottom: 0em;
              margin-top: 0em;
              vertical-align: center;
        }
        @font-face {
        font-family: 'Roboto Slab', serif;
        font-family: 'BioRhyme Expanded', serif;
        src: url(https://fonts.googleapis.com/css?family=BioRhyme+Expanded|Roboto+Slab);
        }
        h1 { font-family: 'BioRhyme Expanded', serif; }''', font_config=font_config)
    html.write_pdf('text_to_print.pdf', stylesheets=[css], font_config=font_config)

    # lpr -o PrintQuality=Text text_to_print.pdf -P LabelWriter-450-DUO-Label
    command = [ "lpr", "-o", "PrintQuality=Graphics", "text_to_print.pdf", "-P" , app.config["LABELPRINTER"] ]
    print(command)
    if not generate_pdf_only:
        subprocess.call(command)

def printTape( text_to_print = '', generate_pdf_only=True, tapewidth='9' ):
    ## set width for cups - find all available with
    cupswidth = "PageSize="+ tapewidth +"_mm__1___Label__Auto_"
    figwidth = {'11': 0.2, '12': 0.25, '9':0.13, '19':0.5 }
    ## generate dynamic pdf with matplotlib
    pdf_pages = PdfPages('text_to_print.pdf')
    fig = plot.figure(figsize=(0, figwidth[tapewidth] ),facecolor='w')
    #fig.text(0, 0, text_to_print)
    fig.text(0, 0.25, text_to_print)

    ## bbox_inches='tight' resize automativally
    ## found here  https://stackoverflow.com/questions/1271023/resize-a-figure-automatically-in-matplotlib
    pdf_pages.savefig(fig, fontsize=tapewidth,verticalalignment='center', bbox_inches='tight',dpi=100)
    pdf_pages.close()

    ##  lpr -o PageSize=9_mm__1___Label__Auto -o PrintQuality=Text text_to_print.pdf -P LabelWriter-450-DUO-Tape
    command = [ "lpr", "-o", cupswidth , "-o", "PrintQuality=Text", "text_to_print.pdf", "-P" , app.config["TAPEPRINTER"] ]
    print(command)
    if not generate_pdf_only:
        subprocess.call(command)

@app.route('/printers')
def printers():
    command = [ "lpstat", "-p", "-d" ]
    out = subprocess.check_output(command)
    print(command)
    return render_template('printers.html', title='Printers', out=out.decode("utf-8"))