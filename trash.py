model_path = "/content/keras_model.h5"
labels_path = "/content/labels.txt"
from google.colab import files
path = files.upload()
path = list(path.keys())[0]
image=Image.open(path)
image_path = path
clase = detect_bird(model_path, labels_path, image_path)

if clase[0] == "Organica":
  print("Esto es organico, con una probabilidad del {clase[1]*100}")
  print("La basura orgánica puede ser tratada mediante el compostaje o la digestión anaeróbica. Separar la basura orgánica de otros tipos de residuos ayuda a reducir la contaminación del agua y el suelo, y a frenar el cambio climático")

elif clase[0] == "Inorganica":
  print("Esto es inorganico, con una probabilidad del {clase[1]*100}")
  print("La basura inorgánica puede ser sólida, líquida o gaseosa. Para evitar que contamine el medio ambiente, es importante reciclarla o almacenarla en lugares especiales. ")

elif clase[0] == "Reciclable":
  print("Esto es algo reciclable, con una probabilidad del {clase[1]*100}")
  print("La basura reciclable es aquella que se puede volver a utilizar como materia prima para otros productos. Para reciclar correctamente, es importante separar los materiales secos de los húmedos y limpiarlos antes de depositarlos en los contenedores. ")

elif clase[0] == "No reciclable":
  print("Esto es algo no reciclable, con una probabilidad {clase[1]*100}")
  print("La basura no reciclable es aquella que no se puede procesar para reutilizarla o transformarla en nuevos productos. Esto puede deberse a su composición, contaminación o falta de tecnología adecuada")