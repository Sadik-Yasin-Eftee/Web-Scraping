import pandas as pd
from google_play_scraper import Sort, reviews


def scrape_reviews(apps, score, n_reviews):
    
    reviews_dict = {}
    for app_name, app_id in apps.items():
        reviews_data, _ = reviews(
            app_id,
            lang='en',
            country='us',
            sort=Sort.MOST_RELEVANT,
            count=n_reviews,
            filter_score_with=score
        )
        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(reviews_data, columns=["reviewId", "content", "score"])
        reviews_dict[app_name] = df
    return reviews_dict
