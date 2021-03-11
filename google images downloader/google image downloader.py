from google_images_download import google_images_download   #importing the library
response = google_images_download.googleimagesdownload()   #class instantiation
arguments = {"keywords":"","limit":1,"format":"jpg"}
paths = response.download(arguments)