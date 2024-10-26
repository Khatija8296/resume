# coding=utf-8
import logging
import os
import re
import subprocess

import pandas as pd  # Using 'pd' as a common alias for pandas
import yaml


from bin import pdf2text

CONFS = None

AVAILABLE_EXTENSIONS = {
    '.csv', '.doc', '.docx', '.eml', '.epub', '.gif', '.htm', '.html',
    '.jpeg', '.jpg', '.json', '.log', '.mp3', '.msg', '.odt', '.ogg',
    '.pdf', '.png', '.pptx', '.ps', '.psv', '.rtf', '.tff', '.tif',
    '.tiff', '.tsv', '.txt', '.wav', '.xls', '.xlsx'
}

def load_confs(confs_path="C:/Users/Dell-3420-Ci3/Documents/ResumeParser-master/confs/config.yaml"):
    """Load configurations from a YAML file.

    Args:
        confs_path (str): The path to the configuration file.

    Returns:
        dict: The loaded configuration dictionary.
    """
    global CONFS

    if CONFS is None:
        confs_template_path = r"C:\Users\Dell-3420-Ci3\Documents\ResumeParser-master\confs\config.yaml.template"
  # Move this declaration outside the try block
        try:
            with open(confs_path) as conf_file:  # Use context manager for file opening
                CONFS = yaml.safe_load(conf_file)  # Use safe_load for security
        except IOError:
            logging.warning(
                'Confs path: {} does not exist. Attempting to load confs template from path: {}'.format(confs_path, confs_template_path)
            )
            with open(confs_template_path) as conf_template_file:
                CONFS = yaml.safe_load(conf_template_file)
    return CONFS


def get_conf(conf_name):
    """Get a specific configuration value.

    Args:
        conf_name (str): The name of the configuration to retrieve.

    Returns:
        any: The value of the requested configuration.
    """
    return load_confs()[conf_name]


def archive_dataset_schemas(step_name, local_dict, global_dict):
    """Archive the schema for all available Pandas DataFrames.

    Args:
        step_name (str): The name of the current operation (e.g., `extract`, `transform`, `model`, or `load`).
        local_dict (dict): A dictionary containing mappings from variable name to objects.
        global_dict (dict): A dictionary containing mappings from variable name to objects.

    Returns:
        None
    """
    logging.info('Archiving data set schema(s) for step name: {}'.format(step_name))

    # Reference variables
    data_schema_dir = get_conf('data_schema_dir')
    schema_output_path = os.path.join(data_schema_dir, step_name + '.csv')
    schema_agg = []

    env_variables = {**local_dict, **global_dict}  # Merged dictionary

    # Filter down to Pandas DataFrames
    data_sets = {name: df for name, df in env_variables.items() if isinstance(df, pd.DataFrame)}

    for data_set_name, data_set in data_sets.items():
        logging.info('Working data_set: {}'.format(data_set_name))

        local_schema_df = pd.DataFrame(data_set.dtypes, columns=['type'])
        local_schema_df['data_set'] = data_set_name

        schema_agg.append(local_schema_df)

    # Aggregate schema list into one data frame
    agg_schema_df = pd.concat(schema_agg)

    # Write to file
    agg_schema_df.to_csv(schema_output_path, index_label='variable')


def term_count(string_to_search, term):
    """Count the number of occurrences of a term in a string.

    Args:
        string_to_search (str): The string to search within.
        term (str): The term to search for.

    Returns:
        int: The number of occurrences of the term.
    """
    try:
        regular_expression = re.compile(term, re.IGNORECASE)
        result = re.findall(regular_expression, string_to_search)
        return len(result)
    except Exception as e:
        logging.error('Error occurred during regex search: {}'.format(e))
        return 0


def term_match(string_to_search, term):
    """Return the first match of a term in a string.

    Args:
        string_to_search (str): The string to search within.
        term (str): The term to search for.

    Returns:
        str or None: The first match of the term, or None if no match is found.
    """
    try:
        regular_expression = re.compile(term, re.IGNORECASE)
        result = re.findall(regular_expression, string_to_search)
        return result[0] if result else None
    except Exception as e:
        logging.error('Error occurred during regex search: {}'.format(e))
        return None


def convert_pdf(f):
    """Convert a PDF file to text.

    Args:
        f (str): The path to the PDF file.

    Returns:
        str: The contents of the converted text file.
    """
    # Create intermediate output file
    output_filename = os.path.basename(os.path.splitext(f)[0]) + '.txt'
    output_filepath = os.path.join('..', 'data', 'output', output_filename)
    logging.info('Writing text from {} to {}'.format(f, output_filepath))

    # Convert pdf to text, placed in intermediate output file
    pdf2text.main(args=[f, '--outfile', output_filepath])

    # Return contents of intermediate output file with error handling
    try:
        with open(output_filepath, 'r', encoding='utf-8', errors='ignore') as output_file:
            return output_file.read()
    except Exception as e:
        logging.error(f'Failed to read {output_filepath}: {e}')
        return ""