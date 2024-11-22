import re
from dotenv import load_dotenv
import os
from googleapiclient.discovery import build
import nltk
from nltk.tokenize import word_tokenize
import json
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download('averaged_perceptron_tagger')

nltk.download('stopwords')
nltk.download('punkt')

load_dotenv()

api_key = os.getenv('API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

def get_all_comments(video_id):
    comments = []
    next_page_token = None

    while True:
        # Make API call to get comments
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            pageToken=next_page_token  # Use pagination token for next set of comments
        )
        
        # Execute the request
        response = request.execute()

        # Loop through the comments in the response
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            timestamp = item['snippet']['topLevelComment']['snippet']['publishedAt']
            like_count = item['snippet']['topLevelComment']['snippet']['likeCount']
            comments.append({
                'author': author.strip(),
                'comment': comment.strip(),
                'timestamp': timestamp.strip(),
                'like_count': like_count,
            })
        
        # Check if there's another page of comments (pagination)
        next_page_token = response.get('nextPageToken')

        if not next_page_token or len(comments) >= 100:  # If no more pages, break the loop
          break

    return comments

def extract_youtube_id(url_or_id):
    pattern = r'(?:v=|\/)([a-zA-Z0-9_-]{11})(?:&|$)?'
    
    if re.fullmatch(r'[a-zA-Z0-9_-]{11}', url_or_id):
        return url_or_id
    
    match = re.search(pattern, url_or_id)
    if match:
        return match.group(1)
    return None  

informal_phrases = {
    "sat set sat set": "cepat", "ya mas": ""
}

def load_slang_txt(file_path):
    slang_dict_txt = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            slang_dict_txt = json.loads(file_content)
    except json.JSONDecodeError:
        print(f"Error decoding JSON in the file: {file_path}")
    return slang_dict_txt


def load_slang_csv(file_path):
    slang_df = pd.read_csv(file_path, encoding='ISO-8859-1')
    return dict(zip(slang_df.iloc[:, 0], slang_df.iloc[:, 1]))


# Combine slang dictionaries
slang_txt_path = 'combined_slang_words.txt'
slang_dict_txt = load_slang_txt(slang_txt_path)

slang_csv_path = 'new_kamusalay.csv'
slang_dict_csv = load_slang_csv(slang_csv_path)

slang_dict_tambahan = {
    "gw": "saya", "mau": "ingin", "ni": "ini", "aja": "saja", "gak": "tidak", "bgt": "sangat",
    "klo": "kalau", "bgs": "bagus", "masi": "masih", "msh": "masih", "lom": "belum",
    "blm": "belum", "ap": "apa", "brg": "barang", "ad": "ada", "blom": "belum",
    "kebli": "kebeli", "tp": "tapi", "org": "orang", "tdk": "tidak", "yg": "yang",
    "kalo": "kalau", "sy": "saya", "bng": "abang", "bg": "abang", "fto": "foto",
    "spek": "spesifikasi", "cm": "cuma", "jg": "juga", "pd": "pada", "skrg": "sekarang",
    "ga": "tidak", "gk": "tidak", "batre": "baterai", "gue": "saya", "dpt": "dapat",
    "kek": "seperti", "mna": "mana", "mnding": "mending", "mend": "mending",
    "dr": "dari", "sma": "sama", "drpada": "daripada"
}

slang_dict = {**slang_dict_tambahan, **slang_dict_txt, **slang_dict_csv}

# Stopwords (Adjusted)
stpwds_id = list(set(stopwords.words('indonesian')))
retain_words = ['baru', 'lama', 'sama', 'tapi', 'tidak', 'dari', 'belum', 'bagi', 'mau', 'masalah']
for word in retain_words:
    if word in stpwds_id:
        stpwds_id.remove(word)

# Initialize Lemmatizer
lemmatizer = WordNetLemmatizer()

# Function to replace slang terms
def replace_slang_in_text(text, slang_dict):
    words = text.split()
    replaced_words = [slang_dict.get(word, word) for word in words]
    return ' '.join(replaced_words)

def text_preprocessing(text, slang_dict):
    # Case folding (convert text to lowercase)
    text = text.lower()

    # Remove mentions, hashtags, and newlines
    text = re.sub(r"@[\w]+|#[\w]+|\n", " ", text)

    # Remove URLs
    text = re.sub(r"http\S+|www.\S+", " ", text)

    # Remove non-alphabetic characters and extra spaces
    text = re.sub(r"[^\w\s']", " ", text)

    # Replace informal phrases
    for phrase, replacement in informal_phrases.items():
        text = text.replace(phrase, replacement)

    # Replace slang terms
    text = replace_slang_in_text(text, slang_dict)

    # Tokenization
    tokens = word_tokenize(text)

    # Remove stopwords
    tokens = [word for word in tokens if word not in stpwds_id]

    # Lemmatization (optional, but can improve performance)
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Stemming with exceptions
    stemming_exceptions = {"terasa": "terasa", "sat": "cepat", "set": "cepat"}
    tokens = [stemming_exceptions.get(word, word) for word in tokens]

    # Reassemble the text and remove duplicates
    text = ' '.join(dict.fromkeys(tokens))

    return text

