import pandas as pd

class FileAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def count_double_underscores(self):
        if not self.file_path.endswith('.txt'):
            print("count_double_underscores() is only for .txt files.")
            return
        try:
            with open(self.file_path, 'r') as file:
                text = file.read()
                count = text.count('__')
                print(f"Number of '__' in the text file: {count}")
        except FileNotFoundError:
            print(f"Text file not found: {self.file_path}")
        except Exception as e:
            print(f"Error reading text file: {e}")

    def load_data(self):
        try:
            if self.file_path.endswith('.csv'):
                self.df = pd.read_csv(self.file_path)
            elif self.file_path.endswith('.parquet'):
                self.df = pd.read_parquet(self.file_path)
            else:
                raise ValueError("Unsupported file format. Use .csv or .parquet.")
            print(f"Data loaded successfully from {self.file_path}")
        except FileNotFoundError:
            print(f"Data file not found: {self.file_path}")
        except Exception as e:
            print(f"Error loading data: {e}")

    def print_feature_count(self):
        if self.df is None:
            print("No data loaded. Cannot print feature count.")
            return
        print(f"Number of features (columns): {self.df.shape[1]}")

    def describe_data(self):
        if self.df is None:
            print("No data loaded to describe.")
            return
        print("\nPreview:")
        print(self.df.head())

def main():
    text_file = 'sample_text.txt'
    csv_file = './sample_junk_mail.csv'
    data_file = './Sample_data_2.parquet'

    # Analyze text file
    text_analyzer = FileAnalyzer(text_file)
    text_analyzer.count_double_underscores()

    # Analyze structured data file
    data_analyzer = FileAnalyzer(data_file)
    csv_analyzer = FileAnalyzer(csv_file)
    data_analyzer.load_data()
    data_analyzer.print_feature_count()
    csv_analyzer.load_data()
    csv_analyzer.describe_data()

if __name__ == "__main__":
    main()
