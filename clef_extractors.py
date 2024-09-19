# from lxml import html as etree
import re 


def remove_extra_spaces(text):
    # remove extra spaces
    return re.sub(r'\s+', ' ', text)



def _find_all_and_concatenate(doc, xpath):
    elements = [paragraph.text.strip() for paragraph in doc.findall(xpath) if paragraph.text is not None]
    elements = ' '.join(elements) if elements is not None else " "
    return elements


def _combine(text_elements):
    """
    Removes newlines, tabs, carriage returns, and extra spaces.
    :param text_elements: list of text snippets
    :return: cleaned and concatenated version of it

    """
    text_elements = [elem if elem is not None else "" for elem in text_elements]
    full_text = ' '.join(text_elements)
    combined= full_text.replace("\n", " ").replace("\r", " ").replace("\t", " ")
    combined = remove_extra_spaces(combined)
    return combined


def extract_english_gh(doc, only_body=False):
    document_id = doc.findtext("docid")
    text = _find_all_and_concatenate(doc, "text")
    if only_body:
        return document_id, text
    document_title = doc.findtext("headline")
    full_text = _combine([document_title, text])
    return document_id, full_text


def extract_english_latimes(doc, only_body=False):
    # docid not matching IDs in qrels, hence docno
    document_id = doc.findtext("docno").strip()
    text = _find_all_and_concatenate(doc, "text/p")
    if only_body:
        return document_id, text
    document_title = _find_all_and_concatenate(doc, "headline/p")
    full_text = _combine([document_title, text])
    return document_id, full_text


def extract_german_derspiegel(doc, only_body=False):
    document_id = doc.findtext("docid")
    text = _find_all_and_concatenate(doc, "text")
    if only_body:
        return document_id, text
    lead = doc.findtext("lead")
    title = _find_all_and_concatenate(doc, "title")
    full_text = _combine([title, lead, text])
    return document_id, full_text


def extract_german_frrundschau(doc, only_body=False):
    document_id = doc.findtext("docid")
    text = doc.findtext("text")
    if only_body:
        return document_id, text
    title = _find_all_and_concatenate(doc, "title")
    full_text = _combine([title, text])
    return document_id, full_text

def extract_german_sda9495(doc, only_body=False):
    document_id = doc.findtext("docid")
    text = _find_all_and_concatenate(doc, "tx")
    if only_body:
        return document_id, text
    subject_terms = _find_all_and_concatenate(doc, "st")
    title = doc.findtext("ti")
    lead = doc.findtext("ld")
    full_text = _combine([title, lead, subject_terms, text])
    return document_id, full_text

def extract_russian(doc, only_body=False):
    document_id = doc.findtext("docid")
    text = doc.findtext("text")
    if only_body:
        return document_id, text
    title = doc.findtext("title")
    subject = doc.findtext("subject")
    full_text = _combine([text, title, subject])
    return document_id, full_text


def extract_dutch(doc, only_body=False):
    document_id = doc.findtext("docid")
    text = _find_all_and_concatenate(doc, "bodyy/te/p")
    if only_body:
        return document_id, text
    document_title = _find_all_and_concatenate(doc, "bodyy/ti/p")
    lead = _find_all_and_concatenate(doc, "bodyy/le/p")
    caption = _find_all_and_concatenate(doc, "bodyy/os/p")
    full_text = _combine([lead, text, document_title, caption])
    return document_id, full_text


def extract_italian_lastampa(doc, only_body=False):
    document_id = doc.findtext("docid")
    text = _find_all_and_concatenate(doc, "text")
    if only_body:
        return document_id, text
    document_title = _find_all_and_concatenate(doc, "title")
    full_text = _combine([text, document_title])
    return document_id, full_text


def extract_italian_sda9495(doc, only_body=False):
    document_id = doc.findtext("docid")
    text = _find_all_and_concatenate(doc, "tx")
    if only_body:
        return document_id, text
    title = _find_all_and_concatenate(doc, "ti")
    lead = _find_all_and_concatenate(doc, "ld")
    subject_terms = _find_all_and_concatenate(doc, "st")
    full_text = _combine([title, lead, subject_terms, text])
    return document_id, full_text


def extract_finish_aamuleth9495(doc, only_body=False):
    document_id = doc.findtext("docid")
    text = _find_all_and_concatenate(doc, "text")
    if only_body:
        return document_id, text
    text = _combine([text])
    return document_id, text


def extract_spanish_efe9495(doc, only_body=False):
    document_id = doc.findtext("docid")
    text = _find_all_and_concatenate(doc, "text")
    if only_body:
        return document_id, text
    title = _find_all_and_concatenate(doc, "title")
    full_text = _combine([title, text])
    return document_id, full_text


def extract_french_sda9495(doc, only_body=False):
    document_id = doc.findtext("docid")
    text = _find_all_and_concatenate(doc, "tx")
    if only_body:
        return document_id, text
    title = _find_all_and_concatenate(doc, "ti")
    lead = _find_all_and_concatenate(doc, "ld")
    subject_terms = _find_all_and_concatenate(doc, "st")
    full_text = _combine([title, lead, subject_terms, text])
    return document_id, full_text



def extract_french_lemonde(doc, only_body=False):
    document_id = doc.findtext("docid")
    text = _find_all_and_concatenate(doc, "text")
    if only_body:
        return document_id, text
    title = doc.findtext("title")
    lead = doc.findtext("lead1")
    full_text = _combine([title, lead, text])
    return document_id, full_text
