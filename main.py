from tkinter import *
from tkinter import filedialog
import tkinter as tk
import os
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2
# Загрузка модели
try:
    model = load_model('Gender_and_Age.keras')
except Exception as e:
    print(f"Ошибка загрузки модели: {e}")
    exit()

# Загрузка предварительно обученного классификатора Haar Cascade для детектирования лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def preprocess_image(image):
    # Конвертировать изображение в оттенки серого
    image = image.convert('L')
    # Изменить размер изображения до 128x128 пикселей
    image = image.resize((128, 128))
    # Преобразовать в numpy массив и нормализовать
    image = np.array(image) / 255.0
    # Добавить размерность пакета
    image = np.expand_dims(image, axis=0)
    return image


def predict_age(image):
    try:
        processed_image = preprocess_image(image)
        predictions = model.predict(processed_image)
        age = int(predictions[0][0])
        return age
    except Exception as e:
        print(f"Ошибка при предсказании возраста: {e}")
        return None


def showImg():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Выберите изображение с лицом",
                                          filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png")))
    if not filename:
        # Если файл не выбран, не делаем ничего
        return

    try:
        # Открыть и преобразовать изображение для отображения
        display_img = Image.open(filename).convert('L')
        display_img = display_img.resize((400, 400), Image.LANCZOS)
        display_img = ImageTk.PhotoImage(display_img)
        lbl.configure(image=display_img)
        lbl.image = display_img

        # Загрузить и преобразовать изображение для обработки
        image = cv2.imread(filename)
        if image is None:
            age_label.config(text="Изображение не найдено.")
            return

        # Преобразовать изображение в оттенки серого для детектирования лиц
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Обнаружить лица на изображении
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) == 0:
            age_label.config(text="Лицо не обнаружено.")
            return

        # Если лица обнаружены, предсказать возраст
        pil_image = Image.open(filename).convert('L')
        age = predict_age(pil_image)
        if age is not None:
            age_label.config(text=f"Возраст: {age}")
        else:
            age_label.config(text="Не удалось предсказать возраст.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        age_label.config(text="Произошла ошибка при обработке изображения.")


root = Tk()

fram = Frame(root)
fram.pack(side=BOTTOM, padx=15, pady=15)

lbl = Label(root)
lbl.pack()

btn = Button(fram, text="Выбрать картинку", command=showImg)
btn.pack(side=tk.LEFT)

age_label = Label(root, text="Возраст: ")
age_label.pack()

root.title("Курсвая")
root.geometry("600x700")
root.mainloop()