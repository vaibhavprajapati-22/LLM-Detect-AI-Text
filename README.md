# LLM-Detect AI Text
Welcome to the "LLM-Detect AI Text" project! In this repository, we present solution for detecting AI-generated text using DistilBERT and XLNet by fine tuning the models. 

## Instalation
To get started, follow these steps:
1. Clone the repository:
  ```sh
  git clone https://github.com/your-username/LLM-Detect-AI-Text.git
  cd LLM-Detect-AI-Text
  ```
2. Get Large file
  ```sh
  git lfs fetch
  git pull
  ```
3. Install the required dependencies:
  ```sh
  pip install -r requirements.txt
  ```
5. Run app.py file
  ```sh
  python app.py
  ```
5. Access the AI Text Detector Website:
   <ul>
     <li>Open your web browser and go to the link provided in the terminal (e.g., http://127.0.0.1:5000).</li>
     <li>Paste the text and check result.</li>
   </ul>

## Work Flow

  1. Data Preprocessing: Creating a balanced dataset from a unbalanced dataset. Each types of labels(i.e AI generated text and Human written text) are same in number. For text preprocessing i have done following 
    operations:
    <ul>
       <li>Remove Non-Alphanumeric Characters</li>
       <li>Tokenization into words and Lowercasing</li>
       <li>Remove Stop Words</li>
     </ul>
  2. Model Training: I have used two pretrained models DistilBert and XLNet and fine tune the model using my dataset to classify between AI text and Human text. I have trained both of models on kaggle GPU.

  3. Validating the Models: I have used a very small portion of my dataset for validation and calulated the precision and recall. You can look the Validation.ipyb notebook for more info about the predictions and 
     confusion matrix.

  4. Deploying: Deploying the models on a website and rendering the websites using Flask. 

## Dataset 
I have a dataset that is available on kaggle. You  can download it from kaggle or google drive link provided below.
<ul>
  <li>https://drive.google.com/drive/folders/1XakZ70IC1bReQEBEX5tZ-IsBu_7PAF1C?usp=sharing</li>
  <li>https://www.kaggle.com/datasets/jdragonxherrera/augmented-data-for-llm-detect-ai-generated-text</li>
</ul>
