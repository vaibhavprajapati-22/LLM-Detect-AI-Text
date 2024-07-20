from transformers import DistilBertTokenizerFast
# from transformers import XLNetTokenizer
import torch
import torch.nn.functional as F
from nltk.corpus import stopwords
import re
import nltk

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split() 
    words = [word.lower() for word in words if word.isalpha()] 
    words = [word for word in words if word not in stop_words]  
    return ' '.join(words)

tokenizer = DistilBertTokenizerFast.from_pretrained('Tokenizer_DistilBert')
# tokenizer = XLNetTokenizer.from_pretrained('Tokenizer_XLNet')

model = torch.load('model_distilbert.pt')
# model = torch.load('model_XLNet.pt')

def get_result(text):
    text = clean_text(text)
    text = [text]
    enc = tokenizer(text, truncation=True, padding=True, return_tensors='pt')
    input_ids = enc['input_ids']
    attention_mask = enc['attention_mask']
    outputs = model(input_ids, attention_mask=attention_mask)
        
    logits = outputs.logits
    logits = F.softmax(logits)
    
    _,pred = torch.max(logits, dim=1)
    return pred.item(),_.item()