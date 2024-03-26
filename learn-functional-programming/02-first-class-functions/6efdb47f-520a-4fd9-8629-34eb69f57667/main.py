def categorize_file(filename):
    extensions = {
        ".txt": "Text",
        ".docx": "Document",
        ".py": "Code"
    }
    get_category = lambda ext: extensions.get(ext, "Unknown")
    return get_category(filename[filename.rfind(".") :])
