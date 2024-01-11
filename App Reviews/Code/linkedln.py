
from UserReviewExtraction.reviewCleaningPipeline import \
    reviewExtractionPipeline

reviews = reviewExtractionPipeline('com.facebook.android', 'en', 10, 1)
print(reviews)