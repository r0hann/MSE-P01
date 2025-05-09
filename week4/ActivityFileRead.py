import pandas as pd

class CSVLoader:
    def __init__(self, csv_file):
      self.csv_file_path = csv_file
      self.df = None
    def load_and_preview(self):
        self.df = pd.read_csv(self.csv_file_path)
        print("CSV file loaded successfully. Preview :")
        print(self.df.head())

      

def main():
    csv_file = 'sample_junk_mail.csv'
    loader = CSVLoader(csv_file)
    loader.load_and_preview()

if __name__ == "__main__":
    main()
