# #!/usr/bin/env python
# """
# coding=utf-8
#
# Code Template
#
# """
# import inspect
# import logging
# import os
# import sys
#
# import pandas
# import spacy
#
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0,parentdir)
#
# from bin import field_extraction
# from bin import lib
#
#
# def main():
#     """
#     Main function documentation template
#     :return: None
#     :rtype: None
#     """
#     logging.getLogger().setLevel(logging.INFO)
#
#     # Extract data from upstream.
#     observations = extract()
#
#     # Spacy: Spacy NLP
#     nlp = spacy.load('en_core_web_sm')
#
#     # Transform data to have appropriate fields
#     observations, nlp = transform(observations, nlp)
#
#     # Load data for downstream consumption
#     load(observations, nlp)
#
#     pass
#
# def extract():
#     logging.info('Begin extract')
#
#     # Reference variables
#     candidate_file_agg = list()
#
#     # Create list of candidate files
#     for root, subdirs, files in os.walk(lib.get_conf('resume_directory')):
#         folder_files = map(lambda x: os.path.join(root, x), files)
#         candidate_file_agg.extend(folder_files)
#
#     # Convert list to a pandas DataFrame
#     observations = pandas.DataFrame(data=candidate_file_agg, columns=['file_path'])
#     logging.info('Found {} candidate files'.format(len(observations.index)))
#
#     # Subset candidate files to supported extensions
#     observations['extension'] = observations['file_path'].apply(lambda x: os.path.splitext(x)[1])
#     observations = observations[observations['extension'].isin(lib.AVAILABLE_EXTENSIONS)]
#     logging.info('Subset candidate files to extensions w/ available parsers. {} files remain'.
#                  format(len(observations.index)))
#
#     # Attempt to extract text from files
#     observations['text'] = observations['file_path'].apply(lib.convert_pdf)
#
#     # Archive schema and return
#     lib.archive_dataset_schemas('extract', locals(), globals())
#     logging.info('End extract')
#     return observations
#
#
# def transform(observations, nlp):
#     # TODO Docstring
#     logging.info('Begin transform')
#
#     # Extract candidate name
#     observations['candidate_name'] = observations['text'].apply(lambda x:
#                                                                 field_extraction.candidate_name_extractor(x, nlp))
#
#     if (observations['candidate_name'] == "NOT FOUND").all():
#
#         match = re.search(field_extraction.NAME_REGEX, observations['text'], re.IGNORECASE)
#         observations['candidate_name'] = match[0]
#
#
#     # Extract contact fields
#     observations['email'] = observations['text'].apply(lambda x: lib.term_match(x, field_extraction.EMAIL_REGEX))
#     observations['phone'] = observations['text'].apply(lambda x: lib.term_match(x, field_extraction.PHONE_REGEX))
#
#     # Extract skills
#     observations = field_extraction.extract_fields(observations)
#
#     # Archive schema and return
#     lib.archive_dataset_schemas('transform', locals(), globals())
#     logging.info('End transform')
#     return observations, nlp
#
#
# # def load(observations, nlp):
# #     logging.info('Begin load')
# #     output_path = os.path.join(lib.get_conf('summary_output_directory'), 'resume_summary.csv')
# #
# #     logging.info('Results being output to {}'.format(output_path))
# #     print('Results output to {}'.format(output_path))
# #
# #     observations.to_csv(path_or_buf=output_path, index_label='index')
# #     logging.info('End transform')
# #     pass
#
# def load(observations, nlp):
#     logging.info('Begin load')
#
#     # Modify the output path to a known writable directory
#     output_path = os.path.join('C:\\Users\\Dell-3420-Ci3\\Desktop', 'resume_summary.csv')
#
#     # Optionally change the output path for testing
#     # output_path = os.path.join(os.getcwd(), 'resume_summary.csv')  # Save in the current directory
#
#     logging.info('Results being output to {}'.format(output_path))
#     print('Results output to {}'.format(output_path))
#
#     try:
#         observations.to_csv(path_or_buf=output_path, index_label='index')
#         logging.info('Successfully saved observations to CSV.')
#     except PermissionError as e:
#         logging.error('Permission denied while saving CSV: {}'.format(e))
#         print('Permission denied while saving CSV. Please check your permissions.')
#     except Exception as e:
#         logging.error('An error occurred while saving CSV: {}'.format(e))
#         print('An error occurred while saving CSV. Check the logs for more details.')
#
#     logging.info('End load')
#
#
# # Main section
# if __name__ == '__main__':
#     main()


# !/usr/bin/env python
"""
coding=utf-8

Code Template

"""
# import inspect
# import logging
# import os
# import sys
# import pandas
# import spacy
# import re  # Make sure to import the re module
#
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0, parentdir)
#
# from bin import field_extraction
# from bin import lib
#
#
# def main():
#     """
#     Main function documentation template
#     :return: None
#     :rtype: None
#     """
#     logging.getLogger().setLevel(logging.INFO)
#
#     # Extract data from upstream.
#     observations = extract()
#
#     # Spacy: Spacy NLP
#     nlp = spacy.load('en_core_web_sm')
#
#     # Transform data to have appropriate fields
#     observations, nlp = transform(observations, nlp)
#
#     # Load data for downstream consumption
#     load(observations, nlp)
#
#     pass
#
#
# def extract():
#     logging.info('Begin extract')
#
#     # Reference variables
#     candidate_file_agg = list()
#
#     # Create list of candidate files
#     for root, subdirs, files in os.walk(lib.get_conf('resume_directory')):
#         folder_files = map(lambda x: os.path.join(root, x), files)
#         candidate_file_agg.extend(folder_files)
#
#     # Convert list to a pandas DataFrame
#     observations = pandas.DataFrame(data=candidate_file_agg, columns=['file_path'])
#     logging.info('Found {} candidate files'.format(len(observations.index)))
#
#     # Subset candidate files to supported extensions
#     observations['extension'] = observations['file_path'].apply(lambda x: os.path.splitext(x)[1])
#     observations = observations[observations['extension'].isin(['.pdf', '.txt'] + list(lib.AVAILABLE_EXTENSIONS))]
#     logging.info('Subset candidate files to extensions w/ available parsers. {} files remain'.
#                  format(len(observations.index)))
#
#     # Attempt to extract text from files
#     observations['text'] = observations['file_path'].apply(lib.convert_pdf)
#
#     # Archive schema and return
#     lib.archive_dataset_schemas('extract', locals(), globals())
#     logging.info('End extract')
#     return observations
#
#
#
# def read_txt_file(file_path):
#     """Read text file and return its content."""
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             return file.read()
#     except Exception as e:
#         logging.error(f"Error reading {file_path}: {e}")
#         return None
#
#
# def transform(observations, nlp):
#     logging.info('Begin transform')
#
#     # Extract candidate name
#     observations['candidate_name'] = observations['text'].apply(lambda x:
#                                                                 field_extraction.candidate_name_extractor(x, nlp))
#
#     if (observations['candidate_name'] == "NOT FOUND").all():
#         match = re.search(field_extraction.NAME_REGEX, observations['text'].str.cat(sep=' '), re.IGNORECASE)
#         if match:
#             observations['candidate_name'] = match.group(0)
#
#     # Extract contact fields
#     observations['email'] = observations['text'].apply(lambda x: lib.term_match(x, field_extraction.EMAIL_REGEX))
#     observations['phone'] = observations['text'].apply(lambda x: lib.term_match(x, field_extraction.PHONE_REGEX))
#
#     # Extract skills
#     observations = field_extraction.extract_fields(observations)
#
#     # Archive schema and return
#     lib.archive_dataset_schemas('transform', locals(), globals())
#     logging.info('End transform')
#     return observations, nlp
#
#
# def load(observations, nlp):
#     logging.info('Begin load')
#
#     # Modify the output path to a known writable directory
#     output_path = os.path.join('C:\\Users\\Dell-3420-Ci3\\Desktop', 'resume_summary1.csv')
#
#     logging.info('Results being output to {}'.format(output_path))
#     print('Results output to {}'.format(output_path))
#
#     try:
#         observations.to_csv(path_or_buf=output_path, index_label='index')
#         logging.info('Successfully saved observations to CSV.')
#     except PermissionError as e:
#         logging.error('Permission denied while saving CSV: {}'.format(e))
#         print('Permission denied while saving CSV. Please check your permissions.')
#     except Exception as e:
#         logging.error('An error occurred while saving CSV: {}'.format(e))
#         print('An error occurred while saving CSV. Check the logs for more details.')
#
#     logging.info('End load')
#
#
# # Main section
# # if __name__ == '__main__':
#     main()
#
#
# import inspect
# import logging
# import os
# import sys
# import pandas
# import spacy
# import re  # Make sure to import the re module
# from flask import Flask, jsonify  # Import Flask and jsonify
# from flask import Flask, jsonify, request
#
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0, parentdir)
#
# from bin import field_extraction
# from bin import lib
#
# app = Flask(__name__)  # Create a Flask app instance
#
# def main():
#     """
#     Main function documentation template
#     :return: None
#     :rtype: None
#     """
#     logging.info('Starting the application...')
#     logging.getLogger().setLevel(logging.INFO)
#
#     # Extract data from upstream.
#     observations = extract()
#
#     # Spacy: Spacy NLP
#     nlp = spacy.load('en_core_web_sm')
#
#     # Transform data to have appropriate fields
#     observations, nlp = transform(observations, nlp)
#
#     # Load data for downstream consumption
#     load(observations, nlp)
#
#     return observations  # Return observations for use in the API endpoint
#
#
# @app.route('/api/resumes', methods=['POST'])
# def get_resumes():
#     logging.info('Received a POST request to /api/resumes')
#
#     # Check if the request method is POST
#     if request.method != 'POST':
#         logging.error("Invalid method: {}".format(request.method))
#         return jsonify({'error': 'Method not allowed'}), 405
#
#     logging.info("Function get_resumes was called")
#
#     # Call extract and transform
#     observations = extract()  # Call extract again or maintain state
#     observations, nlp = transform(observations, spacy.load('en_core_web_sm'))  # Ensure it's transformed
#
#     # Log the transformed observations to check contents
#     logging.info("Transformed observations:\n{}".format(observations))
#
#     return jsonify(observations.to_dict(orient='records'))
#
#
# def extract():
#     logging.info('Begin extract')
#     candidate_file_agg = []
#
#     # Create list of candidate files
#     for root, subdirs, files in os.walk(lib.get_conf('resume_directory')):
#         folder_files = map(lambda x: os.path.join(root, x), files)
#         candidate_file_agg.extend(folder_files)
#
#     observations = pandas.DataFrame(data=candidate_file_agg, columns=['file_path'])
#     logging.info('Found {} candidate files'.format(len(observations.index)))
#
#     # Log the DataFrame to check contents
#     logging.info("Extracted observations:\n{}".format(observations))
#
#     # Subset candidate files to supported extensions
#     observations['extension'] = observations['file_path'].apply(lambda x: os.path.splitext(x)[1])
#     observations = observations[observations['extension'].isin(['.pdf', '.txt'] + list(lib.AVAILABLE_EXTENSIONS))]
#     logging.info('Subset candidate files to extensions w/ available parsers. {} files remain'.
#                  format(len(observations.index)))
#
#     # Attempt to extract text from files
#     observations['text'] = observations['file_path'].apply(lib.convert_pdf)
#
#     # Archive schema and return
#     lib.archive_dataset_schemas('extract', locals(), globals())
#     logging.info('End extract')
#     return observations
#
#
#
# def read_txt_file(file_path):
#     """Read text file and return its content."""
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             return file.read()
#     except Exception as e:
#         logging.error(f"Error reading {file_path}: {e}")
#         return None
#
#
# def transform(observations, nlp):
#     logging.info('Begin transform')
#
#     # Extract candidate name
#     observations['candidate_name'] = observations['text'].apply(lambda x:
#                                                                 field_extraction.candidate_name_extractor(x, nlp))
#
#     if (observations['candidate_name'] == "NOT FOUND").all():
#         match = re.search(field_extraction.NAME_REGEX, observations['text'].str.cat(sep=' '), re.IGNORECASE)
#         if match:
#             observations['candidate_name'] = match.group(0)
#
#     # Extract contact fields
#     observations['email'] = observations['text'].apply(lambda x: lib.term_match(x, field_extraction.EMAIL_REGEX))
#     observations['phone'] = observations['text'].apply(lambda x: lib.term_match(x, field_extraction.PHONE_REGEX))
#
#     # Extract skills
#     observations = field_extraction.extract_fields(observations)
#
#     # Archive schema and return
#     lib.archive_dataset_schemas('transform', locals(), globals())
#     logging.info('End transform')
#     return observations, nlp
#
#
# def load(observations, nlp):
#     logging.info('Begin load')
#
#     # Modify the output path to a known writable directory
#     output_path = os.path.join('C:\\Users\\Dell-3420-Ci3\\Desktop', 'resume_summary1.csv')
#
#     logging.info('Results being output to {}'.format(output_path))
#     print('Results output to {}'.format(output_path))
#
#     try:
#         observations.to_csv(path_or_buf=output_path, index_label='index')
#         logging.info('Successfully saved observations to CSV.')
#     except PermissionError as e:
#         logging.error('Permission denied while saving CSV: {}'.format(e))
#         print('Permission denied while saving CSV. Please check your permissions.')
#     except Exception as e:
#         logging.error('An error occurred while saving CSV: {}'.format(e))
#         print('An error occurred while saving CSV. Check the logs for more details.')
#
#     logging.info('End load')
#
#
# # Main section
# if __name__ == '__main__':
#     # Call main to process the data
#     app.run(debug=True, port= 8000)
#     # Start the Flask application

#
# import inspect
# import logging
# import os
# import sys
# import pandas as pd
# import spacy
# import re  # Import the re module for regex operations
# from flask import Flask, jsonify, request  # Import Flask and related modules
#
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0, parentdir)
#
# from bin import field_extraction
# from bin import lib
#
# app = Flask(__name__)  # Initialize Flask app
#
# def main():
#     """
#     Main function that handles the complete ETL (Extract, Transform, Load) process.
#     :return: pandas DataFrame containing observations
#     """
#     logging.info('Starting the application...')
#     logging.getLogger().setLevel(logging.INFO)
#
#     # Extract data
#     observations = extract()
#
#     # Load the Spacy NLP model
#     nlp = spacy.load('en_core_web_sm')
#
#     # Transform the data
#     observations, nlp = transform(observations, nlp)
#
#     # Load data for downstream consumption
#     load(observations, nlp)
#
#     return observations  # Return the observations
#
# @app.route('/api/resumes', methods=['POST'])
# def get_resumes():
#     logging.info('Received a POST request to /api/resumes')
#
#     # Check if the request method is POST
#     if request.method != 'POST':
#         logging.error("Invalid method: {}".format(request.method))
#         return jsonify({'error': 'Method not allowed'}), 405
#
#     logging.info("Function get_resumes was called")
#
#     # Call extract and transform
#     observations = extract()  # Call extract again or maintain state
#     observations, nlp = transform(observations, spacy.load('en_core_web_sm'))  # Ensure it's transformed
#
#     # Log the transformed observations to check contents
#     logging.info("Transformed observations:\n{}".format(observations))
#
#     # Convert any sets to lists before jsonify
#     for col in observations.columns:
#         if isinstance(observations[col].iloc[0], set):
#             observations[col] = observations[col].apply(list)
#
#     # Return the observations as JSON
#     return jsonify(observations.to_dict(orient='records'))
#
#
#
# def extract():
#     """
#     Extract function to gather files from the resume directory and process them.
#     :return: pandas DataFrame containing the file paths and text data
#     """
#     logging.info('Begin extract')
#     candidate_file_agg = []
#
#     # Traverse the directory to collect resume files
#     for root, subdirs, files in os.walk(lib.get_conf('resume_directory')):
#         folder_files = map(lambda x: os.path.join(root, x), files)
#         candidate_file_agg.extend(folder_files)
#
#     # Create a DataFrame with the file paths
#     observations = pd.DataFrame(data=candidate_file_agg, columns=['file_path'])
#     logging.info('Found {} candidate files'.format(len(observations.index)))
#
#     # Subset candidate files to only those with supported extensions
#     observations['extension'] = observations['file_path'].apply(lambda x: os.path.splitext(x)[1])
#     observations = observations[observations['extension'].isin(['.pdf', '.txt'] + list(lib.AVAILABLE_EXTENSIONS))]
#     logging.info('Subset candidate files to extensions w/ available parsers. {} files remain'.
#                  format(len(observations.index)))
#
#     # Extract text from the files
#     observations['text'] = observations['file_path'].apply(lib.convert_pdf)
#
#     # Archive schema for logging
#     lib.archive_dataset_schemas('extract', locals(), globals())
#     logging.info('End extract')
#     return observations
#
#
# def transform(observations, nlp):
#     """
#     Transform function to extract meaningful fields from the resumes.
#     :param observations: pandas DataFrame containing resume data
#     :param nlp: Spacy NLP model
#     :return: Transformed DataFrame and NLP model
#     """
#     logging.info('Begin transform')
#
#     # Extract candidate names using Spacy and regex as a fallback
#     observations['candidate_name'] = observations['text'].apply(lambda x: field_extraction.candidate_name_extractor(x, nlp))
#
#     if (observations['candidate_name'] == "NOT FOUND").all():
#         match = re.search(field_extraction.NAME_REGEX, observations['text'].str.cat(sep=' '), re.IGNORECASE)
#         if match:
#             observations['candidate_name'] = match.group(0)
#
#     # Extract email and phone using regex
#     observations['email'] = observations['text'].apply(lambda x: lib.term_match(x, field_extraction.EMAIL_REGEX))
#     observations['phone'] = observations['text'].apply(lambda x: lib.term_match(x, field_extraction.PHONE_REGEX))
#
#     # Extract additional fields like skills
#     observations = field_extraction.extract_fields(observations)
#
#     # Archive schema for logging
#     lib.archive_dataset_schemas('transform', locals(), globals())
#     logging.info('End transform')
#     return observations, nlp
#
#
# def load(observations, nlp):
#     """
#     Load function to output the processed data to a CSV file.
#     :param observations: pandas DataFrame containing transformed data
#     :param nlp: Spacy NLP model
#     :return: None
#     """
#     logging.info('Begin load')
#
#     output_path = os.path.join('C:\\Users\\Dell-3420-Ci3\\Desktop', 'resume_summary1.csv')
#     logging.info('Results being output to {}'.format(output_path))
#
#     try:
#         observations.to_csv(path_or_buf=output_path, index_label='index')
#         logging.info('Successfully saved observations to CSV.')
#     except PermissionError as e:
#         logging.error('Permission denied while saving CSV: {}'.format(e))
#         print('Permission denied while saving CSV. Please check your permissions.')
#     except Exception as e:
#         logging.error('An error occurred while saving CSV: {}'.format(e))
#         print('An error occurred while saving CSV. Check the logs for more details.')
#
#     logging.info('End load')
#
#
# # Main entry point for the application
# if __name__ == '__main__':
#     # Start the Flask application
#     app.run(debug=True, port=8000)
#


import inspect
import logging
import pandas as pd
import spacy
import sys
import os
import re  # Import the re module for regex operations
from flask import Flask, jsonify, request
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import PyPDF2  # For PDF text ext
from bin import lib
from flask_cors import CORS  # Import CORS

from bin import field_extraction
# Add the current directory (bin) to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Your custom imports
# Now, you can import from bin
from bin.lib import convert_pdf, get_conf, archive_dataset_schemas, AVAILABLE_EXTENSIONS
  # Modify as per actual content
from bin.field_extraction import candidate_name_extractor, NAME_REGEX, EMAIL_REGEX, PHONE_REGEX, extract_fields

app = Flask(__name__)  # Initialize Flask app
CORS(app)  # Enable CORS for the app
# Function to extract text from a PDF file
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()
    return text

def load(observations, nlp):
    """
    Load function to output the processed data to a CSV file.
    :param observations: pandas DataFrame containing transformed data
    :param nlp: Spacy NLP model
    :return: None
    """
    logging.info('Begin load')
    output_path = os.path.join('C:\\Users\\Dell-3420-Ci3\\Desktop', 'resume_summary1.csv')
    logging.info('Results being output to {}'.format(output_path))

    try:
        # Ensure DataFrame is not empty before saving
        if not observations.empty:
            observations.to_csv(path_or_buf=output_path, index_label='index')
            logging.info('Successfully saved observations to CSV.')
        else:
            logging.warning('No data to save to CSV.')
            print('No data available to save to CSV.')
    except PermissionError as e:
        logging.error('Permission denied while saving CSV: {}'.format(e))
        print('Permission denied while saving CSV. Please check your permissions.')
    except Exception as e:
        logging.error('An error occurred while saving CSV: {}'.format(e))
        print('An error occurred while saving CSV. Check the logs for more details.')
    logging.info('End load')
# @app.route('/api/resumes', methods=['POST'])
# def get_resumes():
#     logging.info('Received a POST request to /api/resumes')
#
#     # Check if the file is in the request
#     if 'file' not in request.files:
#         logging.error("No file part in the request")
#         return jsonify({'error': 'No file part in the request'}), 400
#
#     file = request.files['file']
#
#     # Check if a file was selected
#     if file.filename == '':
#         logging.error("No selected file")
#         return jsonify({'error': 'No selected file'}), 400
#
#     # Check if the file is a PDF
#     if not file.filename.endswith('.pdf'):
#         logging.error("Invalid file type, only PDF allowed")
#         return jsonify({'error': 'Invalid file type, only PDF allowed'}), 400
#
#     logging.info("Processing file: {}".format(file.filename))
#
#     # Extract text from the uploaded PDF
#     extracted_text = extract_text_from_pdf(file)
#
#     # Create a DataFrame to hold the extracted text
#     observations = pd.DataFrame([{'file_path': file.filename, 'text': extracted_text}])
#
#     # Call the transform function
#     nlp = spacy.load('en_core_web_sm')
#     observations, nlp = transform(observations, nlp)
#
#     # Log the transformed observations
#     logging.info("Transformed observations:\n{}".format(observations))
#
#     # Load the observations to a CSV
#     load(observations, nlp)  # Add this line to call the load function
#
#     # Convert sets to lists (if any) before sending as JSON
#     for col in observations.columns:
#         if isinstance(observations[col].iloc[0], set):
#             observations[col] = observations[col].apply(list)
#
#     # Only return specific fields, excluding the 'text' field
#     filtered_observations = observations[['candidate_name', 'email', 'phone', 'experience', 'platforms',
#                                           'database', 'programming', 'machinelearning', 'universities',
#                                           'languages', 'hobbies']]
#
#     # Clean up the phone number to remove empty strings and format it
#     # Clean up the phone number to remove empty strings and format it
#     filtered_observations['phone'] = filtered_observations['phone'].apply(
#         lambda x: ' '.join(filter(None, x)) if x else "")
#
#     # Optionally remove fields that are empty lists
#     filtered_observations = filtered_observations.apply(lambda row: row.dropna().to_dict(), axis=1)
#
#     # Return the filtered observations as JSON
#     return jsonify([obs for obs in filtered_observations if obs])
@app.route('/api/resumes', methods=['POST'])
def get_resumes():
    logging.info('Received a POST request to /api/resumes')
    # Check if the file(s) are in the request
    if 'file' not in request.files and 'file[]' not in request.files:
        logging.error("No file part in the request")
        return jsonify({'error': 'No file part in the request'}), 400
    # Handle single file upload
    if 'file' in request.files:
        files = [request.files['file']]  # Wrap the single file in a list to treat it as multiple
    else:
        # Handle multiple files (file[])
        files = request.files.getlist('file[]')
    observations = []

    for file in files:
        # Check if a file was selected
        if file.filename == '':
            logging.error("No selected file")
            return jsonify({'error': 'No selected file'}), 400

        # Check if the file is a PDF
        if not file.filename.endswith('.pdf'):
            logging.error("Invalid file type, only PDF allowed")
            return jsonify({'error': 'Invalid file type, only PDF allowed'}), 400

        logging.info("Processing file: {}".format(file.filename))

        # Extract text from the uploaded PDF
        extracted_text = extract_text_from_pdf(file)

        # Create a dictionary with extracted text and add it to observations list
        observations.append({'file_path': file.filename, 'text': extracted_text})

    # Create a DataFrame from the observations
    observations_df = pd.DataFrame(observations)

    # Load the NLP model and transform the data
    nlp = spacy.load('en_core_web_sm')
    observations_df, nlp = transform(observations_df, nlp)

    # Log the transformed observations
    logging.info("Transformed observations:\n{}".format(observations_df))

    # Load the observations to a CSV
    load(observations_df, nlp)

    # Convert sets to lists (if any) before sending as JSON
    for col in observations_df.columns:
        if isinstance(observations_df[col].iloc[0], set):
            observations_df[col] = observations_df[col].apply(list)

    # Only return specific fields, excluding the 'text' field
    filtered_observations = observations_df[['candidate_name', 'email', 'phone', 'experience', 'platforms',
                                             'database', 'programming', 'machinelearning', 'universities',
                                             'languages', 'hobbies']]

    # Clean up the phone number to remove empty strings and format it
    filtered_observations['phone'] = filtered_observations['phone'].apply(
        lambda x: ' '.join(filter(None, x)) if x else "")

    # Optionally remove fields that are empty lists
    filtered_observations = filtered_observations.apply(lambda row: row.dropna().to_dict(), axis=1)

    # Return the filtered observations as JSON
    return jsonify([obs for obs in filtered_observations if obs])


def extract():
    """
    Original extract function, to be called when extracting from directory (not used in the Postman flow).
    """
    logging.info('Begin extract')
    candidate_file_agg = []

    # Traverse the directory to collect resume files
    for root, subdirs, files in os.walk(lib.get_conf('resume_directory')):
        folder_files = map(lambda x: os.path.join(root, x), files)
        candidate_file_agg.extend(folder_files)

    # Create a DataFrame with the file paths
    observations = pd.DataFrame(data=candidate_file_agg, columns=['file_path'])
    logging.info('Found {} candidate files'.format(len(observations.index)))

    # Subset candidate files to only those with supported extensions
    observations['extension'] = observations['file_path'].apply(lambda x: os.path.splitext(x)[1])
    observations = observations[observations['extension'].isin(['.pdf', '.txt'] + list(lib.AVAILABLE_EXTENSIONS))]
    logging.info('Subset candidate files to extensions w/ available parsers. {} files remain'.
                 format(len(observations.index)))

    # Extract text from the files
    observations['text'] = observations['file_path'].apply(lib.convert_pdf)

    # Archive schema for logging
    lib.archive_dataset_schemas('extract', locals(), globals())
    logging.info('End extract')
    return observations


def transform(observations, nlp):
    """
    Transform function to extract meaningful fields from the resumes.
    :param observations: pandas DataFrame containing resume data
    :param nlp: Spacy NLP model
    :return: Transformed DataFrame and NLP model
    """
    logging.info('Begin transform')

    # Extract candidate names using Spacy and regex as a fallback
    observations['candidate_name'] = observations['text'].apply(lambda x: field_extraction.candidate_name_extractor(x, nlp))

    if (observations['candidate_name'] == "NOT FOUND").all():
        match = re.search(field_extraction.NAME_REGEX, observations['text'].str.cat(sep=' '), re.IGNORECASE)
        if match:
            observations['candidate_name'] = match.group(0)

    # Extract email and phone using regex
    observations['email'] = observations['text'].apply(lambda x: lib.term_match(x, field_extraction.EMAIL_REGEX))
    observations['phone'] = observations['text'].apply(lambda x: lib.term_match(x, field_extraction.PHONE_REGEX))

    # Extract additional fields like skills
    observations = field_extraction.extract_fields(observations)

    # Archive schema for logging
    lib.archive_dataset_schemas('transform', locals(), globals())
    logging.info('End transform')
    return observations, nlp



# Main entry point for the application
if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=8000, debug=True)


