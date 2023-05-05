from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image

# text = "Hello, World"
text = open("pythontext.txt", 'r').read()

python_mask = np.array(PIL.Image.open("py_logo.png"))

colormap=ImageColorGenerator(python_mask)


# wc = WordCloud().generate(text)
# wc = WordCloud(stopwords=["are","world"]).generate(text)
wc = WordCloud(stopwords=STOPWORDS,
               mask=python_mask,
               background_color="white",
               contour_color="black",
               contour_width=3,
               min_font_size=3).generate(text)

wc.recolor(color_func=colormap)
plt.imshow(wc)
plt.axis("off")

plt.savefig("wc_pythontext.png")

plt.show()
