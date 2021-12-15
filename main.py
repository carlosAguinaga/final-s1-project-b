import collections
from package_module import reader

def get_top_ten():
    try:
        words = reader.get_words('historia.txt')
        top10 = collections.Counter(words).most_common(10)
    except Exception as e:
        return e

    return(top10)


print(get_top_ten())