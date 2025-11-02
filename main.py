import streamlit as st
import tensorflow as tf
import numpy as np

#Tensorflow model prediction
def model_prediction(test_image):
    model  = tf.keras.models.load_model('trained_model.keras')
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #Convert single image to a batch
    prediction = model.predict(input_arr)
    result_index = np.argmax(prediction)
    return result_index

#Sidebar
st.sidebar.title("Dashboard") 
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About","Disease Recognition"])

#Home page
if app_mode == "Home":
    st.header("PLANT DISEASE RECOGNITION SYSTEM")
    image_path = "Home_Image.jpg"
    st.image(image_path, use_container_width=True)
    st.markdown("""
    Welcome to the Plant Disease Recognition System! 🌿🔍
    
    Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

    ### How It Works
    1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of a plant with suspected diseases.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
    3. **Results:** View the results and recommendations for further action.

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the **Disease Recognition** page in the sidebar to upload an image and experience the power of our Plant Disease Recognition System!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page.
    """)

    #About Project
elif(app_mode=="About"):
    st.header("About")
    st.markdown("""
                #### About Dataset
                This dataset is recreated using offline augmentation from the original dataset.The original dataset can be found on this github repo.
                This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into 38 different classes.The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure.
                A new directory containing 33 test images is created later for prediction purpose.
                #### Content
                1. train (70295 images)
                2. test (33 images)
                3. validation (17572 images)

                ### 👨‍💻 Team Members
                1. **Amil Siddiqui** – Team Leader  
               📧 *amilsiddiqui9321@gmail.com*
                 2. **Ehtesham** – Team Member  
               📧 *ehtesham@example.com*
               3. **Shahid** – Team Member  
               📧 *shahid@example.com*
               4. **Uzair** – Team Member  
               📧 *uzair@example.com*
                
                 ### 📊 About the Dataset
                The dataset is a **recreated version** of the original *Plant Village Dataset*, augmented offline to improve model generalization.  
                It contains **RGB images of healthy and diseased plant leaves** belonging to **38 different classes**.

                **Dataset Details:**
                - **Total images:** ~87,000  
                - **Training set:** 70,295 images  
                - **Validation set:** 17,572 images  
                - **Test set:** 33 images (for final prediction testing)
                - **Image type:** RGB (color)
                - **Number of classes:** 38

                The data is divided in an **80/20 ratio** (training/validation) while maintaining the directory structure of each class.  
                A separate folder for **test images** is used during the final model evaluation and prediction stage.

                ---
                 ### 🌿 Note
                ⚠️ **Currently, our trained model can identify only the following 38 plant diseases and healthy categories:**

                - Apple: Apple Scab, Black Rot, Cedar Apple Rust, Healthy  
                - Blueberry: Healthy  
                - Cherry (including sour): Powdery Mildew, Healthy  
                - Corn (Maize): Cercospora Leaf Spot (Gray Leaf Spot), Common Rust, Northern Leaf Blight, Healthy  
                - Grape: Black Rot, Esca (Black Measles), Leaf Blight (Isariopsis Leaf Spot), Healthy  
                - Orange: Haunglongbing (Citrus Greening)  
                - Peach: Bacterial Spot, Healthy  
                - Pepper (Bell): Bacterial Spot, Healthy  
                - Potato: Early Blight, Late Blight, Healthy  
                - Raspberry: Healthy  
                - Soybean: Healthy  
                - Squash: Powdery Mildew  
                - Strawberry: Leaf Scorch, Healthy  
                - Tomato: Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites (Two-Spotted), Target Spot, Tomato Yellow Leaf Curl Virus, Tomato Mosaic Virus, Healthy  

                📝 *We plan to expand this dataset and retrain the model in the future to include more plant species and disease categories.*

                ### 🧩 Technologies Used
                - Python  
                - TensorFlow / Keras  
                - Streamlit  
                - Matplotlib, NumPy, Pandas, Seaborn  
                - Jupyter Notebook  
                - Anaconda Environment

                ---

                ### 🎯 Objective
                To design a reliable and efficient **AI-based tool** that can:
                - Detect plant leaf diseases automatically.  
                - Help farmers identify diseases early.  
                - Contribute towards smarter, sustainable agriculture.

                ---

                *Developed as part of the final year major project by students of Anjuman-I-Islam Kalsekar Technical Campus.*

                """)
    

    #Prediction Page
elif(app_mode=="Disease Recognition"):
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an image file", type=["jpg", "png","jpeg"])
    if(st.button("Show Image")):
        st.image(test_image,use_container_width=True)
    #Prediction button
    if(st.button("Predict")):
        with  st.spinner('Model is predicting...'):
            result_index = model_prediction(test_image)
        st.balloons()
        st.write("Our Prediction")
        result_index = model_prediction(test_image)
        #Define Class Names
        class_name = ['Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Blueberry___healthy',
    'Cherry_(including_sour)___Powdery_mildew',
    'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Peach___Bacterial_spot',
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Raspberry___healthy',
    'Soybean___healthy',
    'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch',
    'Strawberry___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy']
        st.success("Model is Predicting it's a {} ".format(class_name[result_index]))
        
