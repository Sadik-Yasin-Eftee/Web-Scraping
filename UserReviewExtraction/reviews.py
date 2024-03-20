import pandas as pd
import reviewCleaningPipeline
import reviewExtractionPipeline


def main():
    app_link = {
        "Facebook": "com.facebook.katana",
        "WhatsApp": "com.whatsapp",
        "Instagram": "com.instagram.android",
        "LinkedIn": "com.linkedin.android"
    }
    scores = [1, 2]
    number_of_reviews = 1000

    reviews = reviewExtractionPipeline.scrape_reviews(app_link, scores, number_of_reviews)

    reviewCleaningPipeline.save_reviews_csv_with_name(reviews)

if __name__ == "__main__":
    main()



