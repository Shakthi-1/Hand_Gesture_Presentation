import clr
clr.AddReference('Aspose.Slides')
clr.AddReference('System.Drawing')
from Aspose.Slides import Presentation
from System.Drawing.Imaging import ImageFormat

presentation = Presentation("hand gesture.pptx")

for sld in presentation.Slides:
	bmp = sld.GetThumbnail(1, 1)
	bmp.Save("Slide_"+str(sld.SlideNumber)+".jpg", ImageFormat.Jpeg)