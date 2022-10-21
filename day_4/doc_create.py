def md_to_docx(filename: str):
    import subprocess  # wywoływanie poleceń systemowych !!!
    import os

    output_file = os.path.splitext(filename)[0] + ".docx"
    print(f"{filename} -> {output_file}")

    if not os.access(filename, os.R_OK):
        return False


    try:
        command = ["pandoc", "-o", output_file, filename]
        ret_code = subprocess.run(command, capture_output=True)
        print(f"Returned: {ret_code}")
    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    q = md_to_docx("/home/adasiek/test.md._inny.md")
    print(q)
    q = md_to_docx("../output/USD.md")
    print(q)
