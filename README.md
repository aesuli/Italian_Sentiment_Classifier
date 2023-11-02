# Italian Sentiment Classifier

This repo contains the code and the trained model to automatically classify text written in Italian by sentiment.
The classifier, a simple linear model, is trained on short-length posts on social platforms.

The main script is [``classify.py``](classify.py).

It takes in input a filename and a column name. The filename should point to a csv file with a document to be classified per row. The file must have a header row naming each column of the csv.

The script produces as the output a csv file named ``labeled_sent_ita.csv`` containing the same content of the input file plus a ``label`` column with the sentiment label for each row in the input file.

The file [``sample_data.csv``](sample_data.csv) is an example of input data.

```commandline
python classify.py sample_data.csv text
```

See [``requirements.txt``](requirements.txt) for the requirements of the python environment.

See [LICENSE](LICENSE) file for the license terms.
