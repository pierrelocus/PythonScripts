#!/usr/bin/python3

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
import cmd

class ImageToText(cmd.Cmd):
    def do_itt(self, line):
        """Usage: itt <image> <file>
        Will look for text on <image> and append it to <file>"""
        image = line.split(' ')[0]
        nfile = line.split(' ')[1]
        try:
            ofile = open(nfile, 'a+')
            ofile.write(pytesseract.image_to_string(Image.open(image), lang='fra'))
        except:
            print("Error")

    def do_ls(self, line):
        """Lists files in current directory"""
        print('\n'.join([i for i in os.listdir('.') if os.path.isfile(i)]))

    def do_exit(self, line):
        """Exits the program"""
        return True

if __name__ == '__main__':
    ImageToText().cmdloop()
