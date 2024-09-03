# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 11:39:56 2021

@author: user
"""
import pyttsx3
import PyPDF2

class PDF_to_Speech:
    def __init__(self,pdf):
        self.pdf = pdf
        # Initialize the text-to-speech engine
        self.speaker = pyttsx3.init()          
    def read_pdf(self):
        try:
            # Read the PDF file
            with open(self.pdf, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                text = ''
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    # Extract text from each page
                    text += page.extract_text()
                return text
        except Exception as e:
            # Handle errors during PDF reading
            print(f"Error reading PDF: {e}")
            return None
        
    def clean(self,text):
        # Clean up the extracted text
        return text.strip().replace('\n',' ')
    
    def audio(self,text):
        self.speaker.say(text)
        self.speaker.runAndWait()
        
    def save_audio(self,text):
            # Save the speech as an audio file
            audio_file = self.pdf.replace('.pdf', '.mp3')
            self.speaker.save_to_file(text,audio_file)
            self.speaker.runAndWait()
        
    def process_pdf(self):
        text = self.read_pdf()
        if text:
            text = self.clean(text)
            # Uncomment if you want to directly speak the text while executing code
            # text = self.audio(text)  
            text = self.save_audio(text)
            
    def stop_speaker(self):
        self.speaker.stop()   
        
if __name__ == '__main__':
    pdf = 'Pratiksha.pdf'
    obj =  PDF_to_Speech(pdf)  
    obj.process_pdf()
    # Stop the text-to-speech engin
    obj.stop_speaker()      
        
   



