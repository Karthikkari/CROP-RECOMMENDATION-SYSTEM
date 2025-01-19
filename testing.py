from joblib import load
def cropSystem(n, p, k, temp, h, ph, rf):
   model = load("C:/Users/Kari Karthik/OneDrive/Documents/crop_project/crop_model.joblib")
   cropName = ['rice', 'maize', 'chickpea', 'kidneybeans','pigeonpeas', 'mothbeans',   
 'mungbean', 'blackgram', 'lentil', 'pomegranate', 'banana', 'mango', 'grapes',
 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']

   value = []
   value.append(float(n))
   value.append(float(p))
   value.append(float(k))
   value.append(float(temp))
   value.append(float(h))
   value.append(float(ph))
   value.append(float(rf))
   return cropName[model.predict([value])[0]]
# print(cropSystem(10,10,10,10,10,10,10))
