
from face_rec import Facerec

#Encodes faces from the folder
sfr = Facerec()
sfr.load_encoding_images("images/")
sfr.run_camera(text_size = 5)