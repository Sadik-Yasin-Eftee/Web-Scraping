import pandas as pd
import reviewCleaningPipeline
import reviewExtractionPipeline

app_link = {"Facebook": "com.facebook.katana", "WhatsApp": "com.whatsapp", "Instagram": "com.instagram.android", "LinkedIn": "com.linkedin.android"}
score = 2
number_of_reviews = 1000

reviews = reviewExtractionPipeline.scrape_reviews(app_link, score, number_of_reviews)

for app_name, review_df in reviews.items():
    reviewCleaningPipeline.save_reviews_csv_with_name(review_df, app_name)



