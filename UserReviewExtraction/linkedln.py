import os

import pandas as pd
from reviewExtractionPipeline import reviewExtractionPipeline

reviews = reviewExtractionPipeline('com.linkedin.android', 'en', 1000, 1)
print(reviews)

directory_path = r'D:\Semester\Thesis\Web-Scraping\App Reviews\Data'

if not os.path.exists(directory_path):
    os.makedirs(directory_path)

csv_file_path = os.path.join(directory_path, 'linkedin_reviews.csv')
reviews.to_csv(csv_file_path, index=False)

print(f"Reviews saved")