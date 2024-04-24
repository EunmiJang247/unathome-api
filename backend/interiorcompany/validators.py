import os

def validate_file_extension(value):
    isValid = True
    root, ext = os.path.splitext(value)
    
    valid_extensions = ['.png', '.jpeg']

    if ext.lower() not in valid_extensions:
        isValid = False

    return isValid