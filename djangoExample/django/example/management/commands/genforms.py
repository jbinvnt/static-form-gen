from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from fileinput import FileInput
from os import listdir, path
from re import compile, search
class Command(BaseCommand):
    help = 'Renders forms in static files without the need for templates'

    def add_arguments(self, parser):
        parser.add_argument('module-name', help='the name of the module containing your forms')
        parser.add_argument('static-dir', help='the directory relative to project root containing static files')
        #parser.add_argument('--render-type', default='as_p()') #TODO make this a limited set of options for eval security
        parser.add_argument('--file-extensions', nargs='*', default='html')
    def handle(self, *args, **options):
        exec("from " + options['module-name'] + " import *")
        regex = compile("<\\s*SForm\\s*class\\s*=\\s*\"([a-zA-Z0-9_]+)\"\\s*>")
        endtag = compile("<\\s*/SForm\\s*>")
        for filename in listdir(path.join(settings.BASE_DIR, options['static-dir'])): #TODO have it search recursively
            for extension in options['file_extensions']:
                if filename.endswith(extension):
                    with FileInput(path.join(settings.BASE_DIR, options['static-dir'], filename), inplace=True, backup='.previous') as f:
                        found = False #TODO this will break if user tries nested forms. Fix with stack?
                        for line in f:
                            if found and not endtag.search(line):
                                found = False
                                continue
                            result = regex.search(line)
                            if result:
                                found = True
                                className = result.group(0)
                                if className in locals():
                                    print(locals()[className].as_p())
                                    print("</SForm>")
                                else:
                                    raise CommandError("Could not expand the class name %s. Make sure this name is in the module you specified." % className)
                            else:
                                print(line)
                        if found:
                            raise CommandError("Did not find closing </SForm> tag in %s. Revert to the .previous file and close all tags." % filename) #TODO revert automatically?

