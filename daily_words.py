from extractor import Extractor
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os


global freq_dict


def grey_color(word, font_size, position, orientation, random_state=None, **kwargs):

    try:
        return f"hsl(0, 0%, {freq_dict[word] + max(freq_dict.values())}%)"

    except KeyError:
        return f"hsl(0, 0%, {min(freq_dict.values())}%)"


if __name__ == "__main__":

    this_dir = os.path.split(os.path.realpath(__file__))[0]
    config   = os.path.join(this_dir, 'config.json')

    keyword_list = Extractor(config).get_keywords()
    print(len(keyword_list))
    freq_dict    = {k: v for k, v in dict(Counter(keyword_list)).items() if v > 5}
    keyword_list = [k for k in keyword_list if k in freq_dict.keys()]
    print(len(keyword_list))

    wordcloud = WordCloud(width=1000, height=1000, min_font_size=10, background_color='black')
    wordcloud.generate(' '.join(keyword_list))

    plt.figure(figsize=(10, 10), facecolor=None)
    plt.imshow(wordcloud.recolor(color_func=grey_color, random_state=3), interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig('words.png')
