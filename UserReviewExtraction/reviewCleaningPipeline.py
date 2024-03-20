import os

import pandas as pd


def save_reviews_csv_with_name(reviews_dict):
    directory=r'D:\Academics\Thesis\New folder\Web-Scraping\App Reviews\Data'

    if not os.path.exists(directory):
        os.makedirs(directory)
        
    for app_name, app_reviews in reviews_dict.items():
        combined_df = pd.concat(app_reviews.values(), ignore_index=True)        
        file_path = os.path.join(directory, f"{app_name}.csv")
        combined_df.to_csv(file_path, index=False)
        print(f"CSV file saved successfully at: {file_path}")
