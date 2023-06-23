import pandas as pd
import os
import json
from data_cleaning.data_cleaning import preprocess
from sentiment_analysis.sentiment_analysis import add_sentiment_columns
from ner.ner import apply_ner


if __name__ == '__main__':
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the path to the data folder
    data_folder = os.path.join(current_dir, 'data')

    # Import the Tweets
    # file_path_import = os.path.join(data_folder, 'twitter_data.csv')
    # data = pd.read_csv(file_path_import)

    # OR import the News API data
    file_path_import = os.path.join(data_folder, 'news_api_data.json')
    with open(file_path_import, 'r') as json_file:
        data = json.load(json_file)
    data = pd.DataFrame(data)

    # Clean and preprocess the text data
    data['preprocessed_text'] = data['text'].apply(preprocess)

    # Perform sentiment analysis
    data = add_sentiment_columns(data)

    # Perform Named Entity Recognition (NER)
    data = apply_ner(data)

    # Save data and export to be analyzed in Power BI
    print(len(data))
    print(data)
    file_path_export = os.path.join(data_folder, 'data_to_export.csv')
    data.to_csv(file_path_export, encoding='utf-8', index=False)
