import pickle
import sys
import pandas as pd


def classify(testdata_file, text_column_name):
    df = pd.read_csv(testdata_file, encoding='utf-8')

    with open('italian_sentiment_classifier.pkl', mode='rb') as inputfile:
        clf = pickle.load(inputfile)

    df['label'] = clf.predict(df[text_column_name])

    df.to_csv('labeled_sent_ita.csv', encoding='utf-8', index=False)


if __name__ == '__main__':
    testdata_file = sys.argv[1]
    text_column_name = sys.argv[2]

    classify(testdata_file, text_column_name)