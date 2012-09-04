from os import path, environ
import sys
import os

class JadeLessCoffeeMiddleware(object):
    directories = None;

    def __init__(self, app, directories=None):
        self.app = app;
        self.directories = directories
        JLC_DIRS = environ.get("JLC_DIRS", None)
        if directories == None and JLC_DIRS is not None:
            self.directories = JLC_DIRS

        print('JadeLessCoffee compiler will run at every request...\n');

    def __call__(self, environ, response):
        #if the JLC_DIRS is set then just do them
        if self.directories is not None:
            if isinstance(self.directories, tuple):
                try:
                    for jlcsource, jlcdestination in self.directories:
                        self.compile(path.normpath(jlcsource), path.normpath(jlcdestination))
                except:
                    print("Cannot compile jlc directories. directories should be a tuple of tuples. \ne.g. JLC_DIRS = (\n    ('/path/to/src', '/path/to/'),\n    ('/path/to/other/src', '/path/to/other'),\n)")
            else:
                try:
                    jlcsource, jlcdestination = self.directories
                    self.compile(path.normpath(jlcsource), path.normpath(jlcdestination))
                except:
                    print("Cannot compile jlc directories. directories should be a tuple of tuples. \ne.g. JLC_DIRS = (\n    ('/path/to/src', '/path/to/'),\n    ('/path/to/other/src', '/path/to/other'),\n)")


        return self.app(environ, response)


    def compile(self, source_directory, output_directory):
        if not path.exists(source_directory):
            #print('No such file or directory: "%s"' % source_directory)
            return
        if not path.exists(output_directory):
            #print('No such file or directory: "%s"' % output_directory)
            return

        # subprocess suddenly stopped working...
        # from subprocess import Popen, call, PIPE
        # shell=True is necessary on windows due to jlc being provided by environment variables in node
        # call(['jlc', '--incremental', '--out', output_directory, source_directory], shell=True)#, stdout=PIPE, stderr=PIPE)
        os.system('jlc --incremental --out "%s" "%s"' % (output_directory, source_directory))
