filename = "csv/planets.csv

imgScaledArray = []

for k in planetDict['Scale']:
    print (planetDict['Scale'][k])
    print (planetDict['Image'][k])
    print ('pics/'+planetDict['Image'][k])
    # tempvar = ('pics/'+planetDict['Image'][k])
    # print(type(tempvar))
    scaleImage (planetDict['Image'][k], planetDict['Scale'][k])
    # imgScaled.save(img.filename.replace(".","_scaled."))
    image_path = "pics/tmp"
    print (f"{image_path}/{planetDict['Image'][k]}")
    imgScaled = img.save(f"{image_path}/{planetDict['Image'][k]}").filename.replace(".","_scaled.")
    imgScaledArray.append(imgScaled)


for i in imgScaledArray:
    print(i)