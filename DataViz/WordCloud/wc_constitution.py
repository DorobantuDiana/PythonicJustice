from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import PIL.Image

# Read data
data = pd.read_csv('./Constitution Dataset.csv') 

text = ' '.join(data['Preamble'].dropna().astype(str))

python_mask = np.array(PIL.Image.open("contitution.jpeg"))

# colormap=ImageColorGenerator(python_mask)

# Generate a word cloud image
wc = WordCloud(stopwords=STOPWORDS,
               mask=python_mask,
               background_color="black",
            #    contour_color="white",
            #    contour_width=1,
               min_font_size=5,
               max_words=400).generate(text)

# wc.recolor(color_func=colormap)
plt.figure(figsize=(10, 6))
plt.imshow(wc)
plt.axis("off")

plt.savefig("wc_constitution.png")

plt.show()

