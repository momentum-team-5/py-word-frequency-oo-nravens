#!/usr/local/bin/python3
from string import punctuation

STOP_WORDS = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
}


class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        
        with open(self.filename) as text_file:
            return text_file.read()
        

        
class WordList:
    def __init__(self, text):
        self.text = text
        self.wordsCounts = {}
       

    def extract_words(self):
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        self.wordsList = self.text.lower() # set all lowercase
        for p in punctuation: # remove all punctuation
            self.wordsList = self.wordsList.replace(p, '')    
        self.wordsList = self.wordsList.split()
            

    def remove_stop_words(self):
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
        for s_w in STOP_WORDS:
            while s_w in self.wordsList:
                self.wordsList.remove(s_w)
    
    def get_freqs(self):
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """
        for w in self.wordsList:
            if w in self.wordsCounts:
                self.wordsCounts[w] += 1
            else:
                self.wordsCounts[w] = 1
        return self.wordsCounts


class FreqPrinter:
    def __init__(self, freqs):
        self.freqs = freqs

    def print_freqs(self):
        """
        Prints out a frequency chart of the top 10 items
        in our frequencies data structure.

        Example:
          her | 33   *********************************
        which | 12   ************
          all | 12   ************
         they | 7    *******
        their | 7    *******
          she | 7    *******
         them | 6    ******
         such | 6    ******
       rights | 6    ******
        right | 6    ******
        """

        format_width = max(len(w) for w in self.freqs)
        output_string = ""

        for w in sorted(self.freqs, key=self.freqs.get, reverse=True):
            count = self.freqs[w]
            output_string += (f"{w:>{format_width}} : {count} {'*' * count}\n")
        
        print(output_string)


if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
