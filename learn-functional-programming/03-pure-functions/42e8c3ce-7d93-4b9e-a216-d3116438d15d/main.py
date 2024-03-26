def add_format(default_formats, new_format):
    supported_formats = default_formats.copy()
    supported_formats[new_format] = True
    return supported_formats


def remove_format(default_formats, old_format):
    supported_formats = default_formats.copy()
    supported_formats[old_format] = False
    return supported_formats
