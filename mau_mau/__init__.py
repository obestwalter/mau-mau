try:
    # fix terminal output for windows command lines
    import win_unicode_console  # noqa

    win_unicode_console.enable()
except ImportError:
    pass
