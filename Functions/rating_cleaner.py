
def rating_cleaner(rating):
    """
    Some function desc here
    """
    num_rating = int(rating[0])
    return num_rating


def rating_list_cleaner(rating_list):
    """
    Some function desc here
    """
    numeric_list = []
    for rating in rating_list:
        num_rating = rating_cleaner(rating)
        numeric_list.append(num_rating)
    return numeric_list
