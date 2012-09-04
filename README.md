django-jadelesscoffee
=====================

JadeLessCoffee for Node.js is a quick compiler for Jade, LessCSS, and CoffeeScript. This is a wsgi middleware for processing templates/src on the fly using it.

IMPORTANT
=========

jadelesscoffee-middleware is *not* meant for a production environment. **It is slow.**

Requirements
------------

**JadeLessCoffee** Node.js module. (Note that this is currently in a closed alpha state until it can be a proven technique.)


Installation
------------

`$ pip install git+git://github.com/Nuulogic/jadelesscoffee-middleware.git`

Where your application is created, add a line to throw in the JLC middleware:

`from jadelesscoffee.wsgi.middleware import JadeLessCoffeeMiddleware`
`app.wsgi_app = JadeLessCoffeeMiddleware(app.wsgi_app)`

define an environment variable JLC_DIRS that is a list of tuples:

    JLC_DIRS = (
        (os.path.normpath('{0}/templates/src'.format(BASE_PATH)), os.path.normpath('{0}/templates'.format(BASE_PATH))),
        (os.path.normpath('{0}/static/src'.format(BASE_PATH)), os.path.normpath('{0}/static'.format(BASE_PATH))),
        (os.path.normpath('{0}/static/media/src'.format(BASE_PATH)), os.path.normpath('{0}/static/media'.format(BASE_PATH))),
    )

The first entry is a directory containing .jade, .less, or .coffee files. The second is the destination of the output.

The following command will run at each request and will only compile files that have changed.
`jlc --quiet --incremental --output JLC_DIRS[i][1] JLC_DIRS[i][0]`

Note
----

You may want to add `.jlchistory` to your `.gitignore` files. These files are quick databases to track when files were last compiled. You probably don't want/need them in scm.