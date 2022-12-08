
#%% Packages import
from bs4 import BeautifulSoup
import requests
import spacy
import re
from spacytextblob.spacytextblob import SpacyTextBlob
#%%
"""
Web Scraping - retrieve text from report
"""
def get_text():
    url = 'https://www.mckinsey.com/industries/education/our-insights/racial-and-ethnic-equity-in-us-higher-education'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the text
    text = []
    for i in soup.find_all('article')[0].find_all('p'):
        text.append(i.get_text())

    return text

text = get_text()
content = ' '.join(text)

#%%
"""
Cleaning the result text
"""
# citation: http://emailregex.com/
# citation: https://docs.python.org/3/library/re.html
email_re = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

replace = [
    # Matches most URLs
    (r"<a[^>]*>(.*?)</a>", r"\1"),  
    # Remove commas in numbers
    (r"(?<=\d),(?=\d)", ""),      
    # Punctuation and other junk
    (r"[\t\n\r\*\.\@\,\-\/]", " "), 
    # Extra whitespace
    (r"\s+", " ")]                   


for target in replace:
    content = re.sub(target[0], target[1], content)

#%%
"""
Conduct analysis on polarity and subjectivity
"""
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("spacytextblob")
doc = nlp(content)

polarity_report = doc._.blob.polarity
subjectivtiy_report = doc._.blob.subjectivity

polarity_report
subjectivtiy_report

#%%
"""
Conclusion:
    The report from McKinsey has a polarity value of 0.1099 which means its attitude is slightly positive,
    it has a subjectivity value of 0.442974 which means its tone is not very objective.
"""