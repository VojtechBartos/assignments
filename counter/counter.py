from random import randint

def count_analyses(df):
    """
    Returns number of possible analyses from input DataFrame.
    :param df: {pd.DataFrame}
    """
    count = randint(0, 100)
    return "Number of possible analyses: {}".format(count)
