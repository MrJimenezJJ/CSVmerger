
from FileMerger import FileMerger

import data 

def main():
    fileMerger = FileMerger(data.data)

    fileMerger.createFiles()


if __name__=="__main__":
    main()