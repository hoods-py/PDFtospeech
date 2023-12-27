import PyPDF2
from gtts import gTTS

# PDF file of your choosing, this is a sample inside the project directory
pdfFile = open('test.pdf', 'rb')

# Create a PDF reader object
pdfReader = PyPDF2.PdfReader(pdfFile)

# Get total number of pages
pages = len(pdfReader.pages)

# Initialize a string to store the extracted text
extracted_text = ""

# Loop through all the pages
for page in pdfReader.pages:
    # Extract the text from each page
    extracted_text += page.extract_text()

# Close the file
pdfFile.close()

# Convert the text to speech using google's text to speech API
speech = gTTS(text = extracted_text, lang = 'en', slow = False)

# Save the speech audio file
speech.save("test.mp3")