import SentimentAnalysis
import cgi, smtplib

form = cgi.FieldStorage()

text = form.getvalue("text")
sentiment = SentimentAnalysis