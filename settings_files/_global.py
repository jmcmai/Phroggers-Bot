import os

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SETTINGS_DIR)
DATA_DIR = os.path.join(ROOT_DIR, 'data')

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", False)

REDDIT_APP_ID = os.getenv("REDDIT_APP_ID", False)
REDDIT_APP_SECRET = os.getenv("REDDIT_APP_SECRET", False)

REDDIT_ENABLED_FOOD_SUBREDDITS=[
    'food',
    'foodporn',
    'dessertporn'
]

REDDIT_ENABLED_DOG_SUBREDDITS=[
    'dogs',
    'dogpictures',
    'puppies',
    'rarepuppers',
    'corgi',
    'shiba',
    'whatswrongwithyourdog',
    'puppysmiles'
]

REDDIT_ENABLED_CAT_SUBREDDITS=[
    'catpics',
    'meow_irl',
    'cats',
    'kittens',
    'illegallysmolcats',
    'cutecats',
    'catloaf',
    'tuckedinkitties'
]
