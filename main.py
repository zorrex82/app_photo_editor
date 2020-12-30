import streamlit as st
import numpy as np
import cv2
from PIL import Image, ImageEnhance

OUTPUT_IMAGE = 500


def main():
    st.sidebar.header("Photo Editor")
    st.sidebar.info("100% build with Python")
    st.sidebar.markdown("App for apply filters on pictures, using the library OpenCV.")

    our_image = Image.open('empty.jpg')

    # Menu with options
    options_menu = ['Filters', 'About']
    choice = st.sidebar.selectbox("Choose a option:", options_menu)

    if choice == "Filters":
        st.title("First Project using Streamlit and OpenCV")
        st.text("by Edinor Junior: Machine Learning Engineer")
        st.markdown(f"""
                        ℹ️ Project built in a Masterclass about Computer Vision from Carlos Melo (Sigmoidal). 
                        to Know more about the Masterclass, access [this page](https://pay.hotmart.com/K44730436X?checkoutMode=10&bid=1608039415553).
                        """)

        # load and show image

        st.subheader("Upload the image file here")
        # Initial Image
        image_file = st.file_uploader("Load image", type=['jpg', 'jpeg', 'png'])

        if image_file is not None:
            our_image = Image.open(image_file)
            st.sidebar.text("Original Image")
            st.sidebar.image(our_image, width=150)

        col1, col2 = st.beta_columns(2)

        # list of filters
        filters = st.sidebar.radio("Filters", ["Original", "Grayscale", "Draw", "Sepia", "Blur", "Canny", "Contrast"])

        if filters == "Grayscale":
            converted_image = np.array(our_image.convert('RGB'))
            gray_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2GRAY)

            col1.header("Original")
            col1.image(our_image, use_column_width=True)
            col2.header("Grayscale")
            col2.image(gray_image, use_column_width=True)

        elif filters == "Draw":
            converted_image = np.array(our_image.convert("RGB"))
            gray_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2GRAY)
            inv_gray_image = 255 - gray_image
            blur_image = cv2.GaussianBlur(inv_gray_image, (21, 21), 0, 0)
            sketch_image = cv2.divide(gray_image, 255 - blur_image, scale=256)

            col1.header("Original")
            col1.image(our_image, use_column_width=True)
            col2.header("Desenho")
            col2.image(sketch_image, use_column_width=True)

        elif filters == "Sepia":
            converted_image = np.array(our_image.convert("RGB"))
            converted_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2BGR)
            kernel = np.array([[0.272, 0.534, 0.131],
                               [0.349, 0.686, 0.168],
                               [0.393, 0.769, 0.189]])
            sepia_image = cv2.filter2D(converted_image, -1, kernel)

            col1.header("Original")
            col1.image(our_image, use_column_width=True)
            col2.header("Sepia")
            col2.image(sepia_image, channels="BGR", use_column_width=True)

        elif filters == "Blur":
            b_amount = st.sidebar.slider("Kernel (n x n)", 3, 81, 9, step=2)
            converted_image = np.array(our_image.convert("RGB"))
            converted_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2BGR)
            blur_image = cv2.GaussianBlur(converted_image, (b_amount, b_amount), 0, 0)

            col1.header("Original")
            col1.image(our_image, use_column_width=True)
            col2.header("Blur")
            col2.image(blur_image, channels="BGR", use_column_width=True)

        elif filters == "Canny":
            converted_image = np.array(our_image.convert("RGB"))
            converted_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2BGR)
            blur_image = cv2.GaussianBlur(converted_image, (11, 11), 0, 0)
            canny = cv2.Canny(blur_image, 100, 150)

            col1.header("Original")
            col1.image(our_image, use_column_width=True)
            col2.header("Canny Edge Detection")
            col2.image(canny, use_column_width=True)

        elif filters == 'Contrast':
            c_amount = st.sidebar.slider("Contrast", 0.0, 2.0, 1.0)
            enhancer = ImageEnhance.Contrast(our_image)
            contrast_image = enhancer.enhance(c_amount)

            col1.header("Original")
            col1.image(our_image, use_column_width=True)
            col2.header("Contrast")
            col2.image(contrast_image, use_column_width=True)

        elif filters == "Original":
            st.image(our_image, width=OUTPUT_IMAGE)
        else:
            st.image(our_image, width=OUTPUT_IMAGE)

    elif choice == "About":
        st.subheader("This is a project from Masterclass about Computer Vision.")
        st.markdown("To know more, access [this link.](https://sigmoidal.ai)")
        st.text("Edinor Junior")
        st.video("https://www.youtube.com/watch?v=JhkhbTTxlQg")

if __name__ == '__main__':
    main()
