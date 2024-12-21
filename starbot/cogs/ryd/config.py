class Settings:
    YT_ID_REGEX_TEXT = r'((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)(?P<videoId>[\w\-]+)(\S+)?'

    REQUEST_HEADERS = {"User-Agent": " RYDCog by NoPlagiarism"}
    API_BASE_URL = "https://returnyoutubedislikeapi.com/"
    VOTES_URL = API_BASE_URL + "Votes"

    DISPLAY_PER_RATIO = 6
    DISPLAY_RATIO_FULL = "█"
    DISPLAY_RATIO_EMPTY = " "
    DISPLAY_LIKE = "👍"
    DISPLAY_DISLIKE = "👎"

    MAX_DISPLAYED = 3
    IGNORE_MAX_REACHED = True
