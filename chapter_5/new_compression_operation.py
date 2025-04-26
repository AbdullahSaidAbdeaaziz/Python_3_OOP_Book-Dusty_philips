from zip_processor import ZipProcessor
import sys


class ZipReplace(ZipProcessor):
    def __init__(self, filename: str, search_string: str, replace_string: str):
        """
        Initialize the ZipReplace object.

        Args:
            filename (str): The name of the zip file.
            search_string (str): The string to search for.
            replace_string (str): The string to replace with.
        """
        super().__init__(filename)
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self) -> None:
        """
        Perform a search and replace on all files in the temporary directory.
        """
        try:
            for filename in self.temp_directory.iterdir():
                if filename.is_file():  # Only process files, not subdirectories
                    with filename.open("r", encoding="utf-8") as file:
                        contents = file.read()
                    contents = contents.replace(self.search_string, self.replace_string)
                    with filename.open("w", encoding="utf-8") as file:
                        file.write(contents)
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python zip_replace.py <filename> <search_string> <replace_string>"
        )
    else:
        ZipReplace(*sys.argv[1:4]).process_zip()
