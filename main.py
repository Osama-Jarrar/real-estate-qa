# main.py


from pipelines.full_pipeline import full_pipeline


if __name__ == "__main__":

    RAW_PATH = "Data/kc_house_data.csv"
    

    x = full_pipeline(RAW_PATH)
    
    print(x)
