from fabric.api import settings, run


def exists(path):
    with settings(warn_only=True):
        return run('test -e %s' % path)