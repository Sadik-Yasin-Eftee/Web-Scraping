from datetime import datetime

import pandas as pd


def extract_review_content(reviews):
    review_dict = {review['reviewId']: review.get('content', '') for review in reviews}
    df = pd.DataFrame(list(review_dict.items()), columns=['Review ID', 'Review Content'])
    return df