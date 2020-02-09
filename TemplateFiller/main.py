#!/usr/bin/python3

import cmd
import re

class Templater(cmd.Cmd):
    template = ''
    original_template = ''

    def do_set_template(self, line):
        """Usage: set_template <HTML Template>
        Set the HTML template that will be filled. It'll look for {{variables}}
        and ask you what to fill at their place."""
        try :
            self.template = line.strip()
            self.original_template = self.template
            print("Template set successfully")
        except:
            print("Not a valid template")
    def do_reset_template(self, line):
        """Usage: reset_template
        Resets the template to the original_template.
        Using set_template will change the original_template too"""
        self.template = self.original_template

    def do_print_template(self, line):
        """Usage: print_template
        Prints the current template."""
        print(str(self.template))

    def do_fill(self, line):
        """Usage: fill
        Begins the process to fill the {{variables}}"""
        pattern = re.compile('\{\{[a-zA-Z0-9]*\}\}')
        matches = re.findall(pattern, self.template)
        for match in matches:
            print("Got keyword : " , match)
            r = str(input("Replace With : ")).strip()
            self.template = self.template.replace(match, r)
        print("All matches are filled. Don't forget to save your template ;)")

    def do_save(self, line):
        """Usage: save <filename>
        saves the template to an html file <filename>.
        if file exists, append to it"""
        line = line.strip().replace('.html', '')
        line += '.html'
        with open(line, 'a+') as fi:
            fi.write(self.template)
        fi.close()
        print("Saved !")

if __name__ == '__main__':
    Templater().cmdloop()
