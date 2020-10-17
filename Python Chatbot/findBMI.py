def findBMI(height, weight):
    try:
        return round((weight*100*100)/(height*height),2)
    except Exception as e:
        print(str(e))
