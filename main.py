# main.py

from pipeline import run_data_pipeline

def main():
    processed_df = run_data_pipeline("Data/kc_house_data.csv")
    print(processed_df.head())

if __name__ == "__main__":
    main()
