import pandas as pd
from google_play_scraper import Sort, reviews


def scrape_reviews(apps, scores, n_reviews): 
    reviews_dict = {}
    
    for app_name, app_id in apps.items():
        app_reviews = {}
        for score in scores:
            reviews_data, _ = reviews(
                app_id,
                lang='en',
                country='us',
                sort=Sort.MOST_RELEVANT,
                count=n_reviews,
                filter_score_with=score
            )

            df = pd.DataFrame(reviews_data, columns=["reviewId", "content", "score"])
            app_reviews[score] = df
        reviews_dict[app_name] = app_reviews

    return reviews_dict

