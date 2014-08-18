# This programm helps to determine correct exposure time during long time exposures.
# Read more about Reciprocity failure here:
# http://en.wikipedia.org/wiki/Reciprocity_(photography)#Reciprocity_failure
# Here are charts for illford HP5 and Kodak Tri-X 400 films:
# http://www.ilfordphoto.com/Webfiles/20106281054152313.pdf
# http://www.kodak.com/global/en/professional/support/techPubs/f4017/f4017.pdf


import math
import datetime

class Photo:
  def __init__(self, mTime, ndStops):
    self.mTime = mTime
    self.ndStops = ndStops

  def ndFilter(self):
    """Corrects for use of ND filter with ndStops stop exposure reduction"""
    eTimes = [('500', 1/500), ('250', 1/250), ('125',1/125), ('60',1/60), ('30',1/30), ('15',1/15), ('8',1/8), ('4',1/4), ('2',1/2), ('1s',1), ('2s',2), ('4s',4), ('8s',8), ('15s', 15), ('30s', 30), ('60s',60), ('120s',120), ('240s',240), ('480s',480), ('960s',960), ('1920s',1920), ('3840s',3840), ('7680',7680), ('15360s',15360), ('30720s',30720), ('61440s',61440)]
    for i, v in enumerate(eTimes):
      if v[0] == self.mTime:
        ndTime = eTimes[i + self.ndStops][1]
        result = ndTime
        return result

  def triX(self):
    """Calculating exposure time corrected for reciprocity failure for film Kodak Tri-X"""
    correctedTime = ((7.5*self.ndFilter())**1.42)/10
    result =  str(datetime.timedelta(seconds=(math.floor(correctedTime))))
    return result

  def hp5(self):
    """Calculating exposure time corrected for reciprocity failure for film illford HP5"""
    correctedTime = 0.105*(self.ndFilter()**2) + 2.007*self.ndFilter() + 0.821
    result =  str(datetime.timedelta(seconds=(math.floor(correctedTime))))
    return result

while True:
  print ("---------")
  print ("Available exposure times are: 1/500, 1/250, 1/125, 1/60, 1/30, 1/15, 1/8, 1/4, 1/2, 1, 2, 4, 8, 15 ,30 ,60.")
  mTime = str(input("Enter measured exposure time (in format 500 for 1/500 of sec (minumum), 60s for 60 seconds (maximum): "))
  ndStops = int(input("Enter ND filter (use 0 if you shoot without filter): "))
  myPhoto = Photo (mTime, ndStops)
  print("Exposure with", ndStops, "ND filter is:", str(datetime.timedelta(seconds=myPhoto.ndFilter())))
  print("With", ndStops, "ND filter and correction for Tri-X is:", myPhoto.triX())
  print("With", ndStops, "ND filter and correction for Illford HP5 is:", myPhoto.hp5())

