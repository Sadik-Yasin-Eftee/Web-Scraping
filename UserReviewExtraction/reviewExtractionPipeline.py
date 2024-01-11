from google_play_scraper import Sort, reviews
from reviewCleaningPipeline import extract_review_content


def reviewExtractionPipeline(appLink, lang, numberOfReviews, filter_score_with):
    result, continuation_token = reviews(
        appLink,
        lang=lang, 
        country='us', 
        sort=Sort.MOST_RELEVANT, 
        count=numberOfReviews, 
        filter_score_with=filter_score_with 
    )
    result, _ = reviews(
        appLink,
        continuation_token=continuation_token 
    )
    return extract_review_content(result)