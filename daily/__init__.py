from .from_issues import get_info_from_issue_comments

MY_STATUS_DICT_FROM_API = {
    # TODO url
    # "扇贝": {"daily_func": get_shanbay_daily, "url": MY_SHANBAY_URL, "unit_str": " (天)"},
}

MY_STATUS_DICT_FROM_COMMENTS = {
    "周记": {"daily_func": get_info_from_issue_comments, "unit_str": " (周)"},
}
