#!/usr/bin/python

import urllib.request
import os
import tarfile
import pickle
import pandas as pd

print("Downloading Enron emails in the Downloads folder...")

# Get the user's Downloads folder path
downloads = os.path.join(os.environ['HOME'] + "/Downloads")

url = "http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/"

enron_dir = os.path.join(downloads, 'Enron emails')

enron_files = ['enron1.tar.gz', 'enron2.tar.gz', 'enron3.tar.gz',
               'enron4.tar.gz', 'enron5.tar.gz', 'enron6.tar.gz']

def download():
    """ Download Enron emails if missing. """
    
    # Create the directories.
    if not os.path.exists(enron_dir):
        os.makedirs(enron_dir)
    # Download the files that not exist.
    for file in enron_files:
        path = os.path.join(enron_dir, file)
        if not os.path.exists(path):
            urllib.request.urlretrieve(url + file, path)

def extract_emails(fname):
    """ Extract the zipped emails and load them into a pandas df.
    Args:
        fname (str): the files with tar.gz extension
    Returns:
        pandas df: a pandas dataframe of emails
    """
    
    rows = []
    tfile = tarfile.open(fname, 'r:gz')
    for member in tfile.getmembers():
        if 'ham' in member.name:
            f = tfile.extractfile(member)
            if f is not None:
                row = f.read()
                rows.append({'message': row, 'class': 'ham'})
        if 'spam' in member.name:
            f = tfile.extractfile(member)
            if f is not None:
                row = f.read()
                rows.append({'message': row, 'class': 'spam'})
    tfile.close()
    return pd.DataFrame(rows)

def populate_df_and_pickle():
    """ Populate the df with all the emails and save it to a pickle object. """
    
    if not os.path.exists(downloads + "/emails.pickle"):
        emails_df = pd.DataFrame({'message': [], 'class': []})
        for file in enron_files:
            unzipped_file = extract_emails(os.path.join(enron_dir, file))
            emails_df = emails_df.append(unzipped_file)
        emails_df.to_pickle(downloads + "/emails.pickle")

if __name__ == '__main__':
    download()
    populate_df_and_pickle()
    print("Download, unzip, and save to pickle done!")