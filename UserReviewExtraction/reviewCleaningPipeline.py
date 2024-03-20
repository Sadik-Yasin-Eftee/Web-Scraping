import os

import pandas as pd


def save_reviews_csv_with_name(df, app_name):
    
    directory=r'D:\Academics\Thesis\New folder\Web-Scraping\App Reviews\Data'
    # Ensure the directory exists, if not, create it
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Construct the file path
    file_path = os.path.join(directory, f"{app_name}.csv")
    
    # Save the DataFrame to a CSV file
    df.to_csv(file_path, index=False)
    print(f"CSV file saved successfully at: {file_path}")
