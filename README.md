
# PDF Text to Speech Converter 📚

This project is designed to convert text from a PDF document into spoken words, leveraging the pyttsx3 library for text-to-speech conversion. Additionally, the class provides functionality to clean the extracted text and save the spoken text as an audio file (MP3 format).

## Features
- Read PDF: Extract text from each page of a PDF document

- Clean Text: Removeunnecessary spaces and newlines from the extracted text.

- Text to Speech: Convert the cleaned text into speech.

- Save to Audio: Save the spoken text as an MP3 audio file.

- Stop Speaker: Gracefully stop the text-to-speech engine.

## Prerequisites
1. Python Environment
Python Version: Ensure that Python 3.6 or higher is installed on your system. The project is compatible with Python 3 and uses modern libraries and features.

2. Required libraries.
You need to install specific Python libraries for handling PDF files, text-to-speech conversion, and other functionalities. Install these libraries using pip:

* pyttsx3: A library for text-to-speech conversion.
* PyPDF2: A library for reading and extracting text from PDF files.

3. Prepare PDF File:
Ensure you have a PDF file ready for processing. Place it in the directory where you plan to run the script or specify the correct file path.
## How It Works

* Initialization: Instantiate the PDFTextToSpeech class with the path to your PDF file and optionally, the path where you want the audio file saved.

* Processing: Call the process_pdf_to_speech() method to:
    
    a. Read and extract text from the PDF.

    b. Clean the extracted text by removing unnecessary whitespace and newlines.
    
    c. Convert the cleaned text to speech.

    d.Save the spoken text as an audio file.

* Stopping the Speaker: Use stop_speaker() to ensure the text-to-speech engine stops any ongoing processes.
## Used By

- Students and researchers

    Use Case: Students and researchers who need to consume large volumes of text can use the tool to listen to academic papers, articles, or study materials while multitasking or commuting.

- Content creators

    Use Case: Authors and content creators can convert written content, such as ebooks or reports, into audio format for wider distribution, including audiobooks or podcasts.

- Legal and medical professionals

    Use Case: Legal and medical professionals can convert lengthy case files, legal documents, or medical records into audio format to review them more efficiently.

- Personal Use

    Use Case: Individuals who prefer listening to content rather than reading it can use the tool to convert personal documents, such as novels or personal notes, into audio format for easier consumption.## Future scope

* Support for Multiple File Formats: Extend functionality to support additional document formats, such as DOCX, EPUB, or HTML, to provide a more comprehensive text-to-speech solution.

* User Interface Development: Develop a graphical user interface (GUI) for easier interaction, allowing users to select files, customize settings, and play or save audio files through a user-friendly interface.

##  Conclusion 🚀

The PDFTextToSpeech project provides a valuable solution for converting textual content from PDF documents into spoken words. By leveraging text-to-speech technology, this project offers significant benefits, including increased accessibility for individuals with visual impairments, enhanced convenience for professionals and students, and new formats for content consumption.
## Support

For support, email pratikshagarkar871999@gmail.com



[![Medium](https://img.shields.io/badge/Medium-000?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@pratiksha.garkar)


[![Kaggle](https://img.shields.io/badge/Kaggle-000?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/pratikshagarkar)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pratiksha-garkar-110a9a171/)


