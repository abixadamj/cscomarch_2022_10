def markdown_to_word_file(directory: str):
    import os
    for any_file in os.listdir(directory):
        full_file = os.path.join(directory, any_file)
        ext = os.path.splitext(full_file)[1].lower()
        if "." in ext and ext.split(".")[1] == "md":
            # mamy markdown
            print(any_file, full_file, ext)


if __name__ == "__main__":
    dir = "../output"
    markdown_to_word_file(dir)