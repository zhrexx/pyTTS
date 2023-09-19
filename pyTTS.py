
def __init__(self):
  self.rate = 66000
  self.duration = 0.1
  self.stop = 3.00
  self.generation = True


def load(model_file_name):
  with open(model_file_name,"rb") as md:
    md.read()
    
      

def text(text):
  with open("textogen.txt","w") as tx:
    tx.write(text)
  
   

def generate_speech(self):
  pass


def error(self):
  self.generation = False
  
