# spamIt

spamIt is a spam filter in Python using the Naive Bayes algorithm.

## Check Modules

Use the `check_modules.py` to check your system for the required dependencies.

## Download Dataset

Run `get_data.py` to download a set of spam and ham actual emails in your machine, unzip the compressed files, read the text and load it into a Pandas dataframe. Convert the dataframe to a Pickle object.

## Clean the Data

Remove the punctuation, urls and numbers, and convert the words to lower case.

## Prepare the Data

Split the text into individual words, stem each word and remove english stop words.

## Machine Learning

### Vectorize Words and Split Data to Train/Test Sets

Transform the words into a tf-idf matrix with the `sklearn` TfIdf transformation and create train/test sets.

### Train a Classifier

Train a Naive Bayes classifier and evaluate the performance with the accuracy score.

### Identify the Most Powerful Features

Print the most important features.

### Play

Try out the classifier feeding it with some examples.
