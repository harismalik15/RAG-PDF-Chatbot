import pypdf

my_file = "customer_care.pdf"


def read_pdf(file_path):
    reader = pypdf.PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text = text + page.extract_text() + "\n"

    return text


final_text = read_pdf(my_file)
