## 

import cairo
import argparse 

printtext = ""
font_size = 40  // for 11mm  labels
font = "SANS"
font_args=[]
#font_args=[cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD]

def text_extent(font, font_size, text, *args, **kwargs):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 0, 0)
    ctx = cairo.Context(surface)
    ctx.select_font_face(font, *args, **kwargs)
    ctx.set_font_size(font_size)
    return ctx.text_extents(text)

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [TEXT]",
        description="create pdf from given text and print it to a label"
    )
    parser.add_argument("text",nargs='*' )
    return parser

def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    if args.text:
        print(' '.join(map(str, args.text)) )
        printtext = ' '.join([str(elem) for elem in args.text])

    (x_bearing, y_bearing, text_width, text_height,
     x_advance, y_advance) = text_extent(font, font_size, printtext, *font_args)
    print(x_bearing, y_bearing,text_width, text_height) 
    print(x_advance, y_advance)
    ps = cairo.PDFSurface("pdffile.pdf", int(text_width), int(text_height))
    cr = cairo.Context(ps)
    
    cr.set_source_rgb(0, 0, 0)
    #cr.select_font_face(font, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(font_size)
    
    cr.move_to(-x_bearing, -y_bearing)
    cr.show_text(printtext)
    cr.show_page()
        
if __name__ == "__main__":    
    main()

