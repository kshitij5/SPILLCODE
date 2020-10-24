import pyttsx3
import PyPDF3
book = open('holmes.pdf', 'rb')
pdfReader = PyPDF3.PdfFileReader(book)
mytext = ""
for pageNum in range(pdfReader.numPages):
    pages = pdfReader.getPage(0)
    mytext += pages.extractText()
speaker = pyttsx3.init()
speaker.save_to_file(mytext, 'holmes-audio.mp3')
print("Done")
speaker.runAndWait()
