import pandas as pd

class FileMerger:
    
    def __init__(self, data):
        self.data = data
        self.target = "./target/"
    
    def createFiles(self):
        for d in self.data:
            self.mergeFiles(d["fileName"], d["files"] )

    def mergeFiles(self, filename, files):
        dataFramesList = []

        for file in files:
            df = pd.read_csv(file["location"]).assign(From = file["id"])
            df.columns = map(str.upper, df.columns)
            dataFramesList.append(df)
        
        df = pd.concat(dataFramesList)

        df.drop_duplicates(subset=None, inplace=True)

        df.to_csv(self.target + filename)