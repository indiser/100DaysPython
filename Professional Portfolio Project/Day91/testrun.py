import pymupdf4llm
import markdown
from mdclense.parser import MarkdownParser
from bs4 import BeautifulSoup

contents=pymupdf4llm.to_markdown(
    doc="C:/Users/ranab/OneDrive/Desktop/100Days Python/Professional Portfolio Project/Day91/Self_improving_LLM.pdf"
)

# html=markdown.markdown(contents)
# soup=BeautifulSoup(html,"html.parser")

# text=soup.get_text().strip()
parser=MarkdownParser()
text=parser.parse(contents)
print(text)