def overwrite_file(file_path: str, new_code: str):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_code)
