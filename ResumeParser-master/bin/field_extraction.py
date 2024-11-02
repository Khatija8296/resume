# import logging
#
# from gensim.utils import simple_preprocess
#
# from bin import lib
#
# EMAIL_REGEX = r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}"
# PHONE_REGEX = r"\(?(\d{3})?\)?[\s\.-]{0,2}?(\d{3})[\s\.-]{0,2}(\d{4})"
# NAME_REGEX = r'[a-z]+(\s+[a-z]+)?'
#
#
# def candidate_name_extractor(input_string, nlp):
#
#     doc = nlp(input_string)
#
#     # Extract entities
#     doc_entities = doc.ents
#
#     # Subset to person type entities
#     doc_persons = filter(lambda x: x.label_ == 'PERSON', doc_entities)
#     doc_persons = filter(lambda x: len(x.text.strip().split()) >= 2, doc_persons)
#     doc_persons = map(lambda x: x.text.strip(), doc_persons)
#     doc_persons = list(doc_persons)
#
#     # Assuming that the first Person entity with more than two tokens is the candidate's name
#     if len(doc_persons) > 0:
#         return doc_persons[0]
#     return "NOT FOUND"
#
#
# def extract_fields(df):
#     for extractor, items_of_interest in lib.get_conf('extractors').items():
#         df[extractor] = df['text'].apply(lambda x: extract_skills(x, extractor, items_of_interest))
#     return df
#
#
# def extract_skills(resume_text, extractor, items_of_interest):
#     potential_skills_dict = dict()
#     matched_skills = set()
#
#     # TODO This skill input formatting could happen once per run, instead of once per observation.
#     for skill_input in items_of_interest:
#
#         # Format list inputs
#         if type(skill_input) is list and len(skill_input) >= 1:
#             potential_skills_dict[skill_input[0]] = skill_input
#
#         # Format string inputs
#         elif type(skill_input) is str:
#             potential_skills_dict[skill_input] = [skill_input]
#         else:
#             logging.warn('Unknown skill listing type: {}. Please format as either a single string or a list of strings'
#                          ''.format(skill_input))
#
#     for (skill_name, skill_alias_list) in potential_skills_dict.items():
#
#         skill_matches = 0
#         # Iterate through aliases
#         for skill_alias in skill_alias_list:
#             # Add the number of matches for each alias
#             skill_matches += lib.term_count(resume_text, skill_alias.lower())
#
#         # If at least one alias is found, add skill name to set of skills
#         if skill_matches > 0:
#             matched_skills.add(skill_name)
#
#     return matched_skills


import logging
import re
from gensim.utils import simple_preprocess
from bin import lib
import spacy

# Improved regex patterns
EMAIL_REGEX = r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}"
PHONE_REGEX = r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}|\d{10}'
NAME_REGEX = r'[A-Z][a-z]+(\s+[A-Z][a-z]+)?'

def candidate_name_extractor(input_string, nlp):
    doc = nlp(input_string)

    # Extract entities
    doc_entities = doc.ents

    # Subset to person type entities
    doc_persons = filter(lambda x: x.label_ == 'PERSON', doc_entities)
    doc_persons = filter(lambda x: len(x.text.strip().split()) >= 2, doc_persons)
    doc_persons = map(lambda x: x.text.strip(), doc_persons)
    doc_persons = list(doc_persons)

    # Assuming that the first Person entity with more than two tokens is the candidate's name
    if len(doc_persons) > 0:
        return doc_persons[0]
    return "NOT FOUND"


# Load the pre-trained SpaCy model
# nlp = spacy.load("en_core_web_sm")  # or "en_core_web_md" for a larger model

# def candidate_name_extractor(input_string,nlp):
#     # First, attempt to extract names using regular expressions
#     regex_patterns = [
#         r'\b[A-Z][a-z]+\s[A-Z][a-z]+(?:\s[A-Z][a-z]+)?\b',  # Matches 'First Last' or 'First Middle Last'
#         r'\b[A-Z][a-z]+\s[A-Z][a-z]+\s[A-Z][a-z]+\b',  # Matches 'First Middle Last'
#     ]
#
#     combined_pattern = '|'.join(regex_patterns)
#     regex_matches = re.findall(combined_pattern, input_string)
#
#     # If regex matches are found, return the first match
#     if regex_matches:
#         return regex_matches[0]
#
#     # If no regex matches, fall back to the NER model
#     doc = nlp(input_string)
#     doc_persons = [ent.text.strip() for ent in doc.ents if ent.label_ == 'PERSON']
#
#     # Return the first match from NER, if available
#     if doc_persons:
#         return doc_persons[0]
#     return "NOT FOUND"

def extract_fields(df):
    for extractor, items_of_interest in lib.get_conf('extractors').items():
        df[extractor] = df['text'].apply(lambda x: extract_skills(x, extractor, items_of_interest))
    return df

def extract_skills(resume_text, extractor, items_of_interest):
    potential_skills_dict = dict()
    matched_skills = set()

    # Format skill inputs into a dictionary
    for skill_input in items_of_interest:
        if isinstance(skill_input, list) and len(skill_input) >= 1:
            potential_skills_dict[skill_input[0]] = skill_input
        elif isinstance(skill_input, str):
            potential_skills_dict[skill_input] = [skill_input]
        else:
            logging.warning(f'Unknown skill listing type: {skill_input}. Please format as either a single string or a list of strings.')

    # Match skills in the resume text
    for skill_name, skill_alias_list in potential_skills_dict.items():
        skill_matches = sum(lib.term_count(resume_text, skill_alias.lower()) for skill_alias in skill_alias_list)

        if skill_matches > 0:
            matched_skills.add(skill_name)

    return matched_skills




def format_phone_number(phone):
    return ''.join(phone.split())
 # Joins the characters without spaces

# Function to extract phone numbers using regex
def extract_phone_numbers(text):
    matches = re.findall(PHONE_REGEX, text)
    return [format_phone_number(match) for match in matches]

# Usage Example
def transform(observations, nlp):
    logging.info('Begin transform')

    # Extract candidate name
    observations['candidate_name'] = observations['text'].apply(lambda x: candidate_name_extractor(x, nlp))

    # Extract contact fields
    observations['email'] = observations['text'].apply(lambda x: lib.term_match(x, EMAIL_REGEX))
    observations['phone'] = observations['text'].apply(extract_phone_numbers)  # Updated phone extraction

    # Extract skills
    observations = extract_fields(observations)

    # Archive schema and return
    lib.archive_dataset_schemas('transform', locals(), globals())
    logging.info('End transform')
    return observations, nlp
