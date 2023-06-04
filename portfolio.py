import streamlit as st 
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from PIL import Image 
import glob 
from utils import *

image_paths = glob.glob("Images/*.jpg")  # Update the path to your image directory
image_paths.sort()  # Sort the images by name

# Create a list of PIL Image objects
images = [Image.open(path) for path in image_paths]

# Evaluate the total number of images
N_IMAGES = len(images)



st.set_page_config(page_title="Bald Polnareff", page_icon="🗿", layout="wide")


st.image("placeholder_logo.svg")


with st.sidebar:
    selected = option_menu("About me", ["CV", "3D Artwork", "Procedural Artwork"])

if selected == "CV":
    st.markdown("# Education")
    st.markdown("+ **MSc in Aerospace Engineering** (2019-2022) - \n"
                "Polytechnic University of Turin, Italy \n")
    st.markdown("+ **BSc in Aerospace Engineering** (2014-2019) - \n"
                "Polytechnic University of Turin, Italy \n")
    
    st.markdown("### Certifications")
    #st.markdown("+ **Deep Learning Specialization** (2023) \n"
#            "DeepLearning.AI \n")
    st.markdown("+ **Machine Learning Specialization** (2023) - \n"
                "DeepLearning.AI \n")
    st.markdown("+ **Certificate in Advanced English** (2014) - \n"
                "University of Cambridge \n")
    st.divider()
    
    st.markdown("# Publication")
    st.markdown("+ **Novel 3D Printable Bio-based and Biodegradable Poly(3-hydroxybutyrate-co-3- hy-droxyhexanoate) Microspheres for Selective Laser Sintering Applications** - \n"
                "Materials Today Sustainability, 2023 --- \n"
                "[Read here!](https://www.doi.org/10.1016/j.mtsust.2023.100379) \n")
    st.divider()
    
    st.markdown("# Work Experience")
    st.markdown("### Freelance")
    st.markdown("+ **3D Artist** (2020-Present) - \n"
                "I am a freelance 3D artist, I create 3D models and animations for clients. \n")
    st.divider()
    
    st.markdown("# Computer Skills")
    st.markdown("### Development")
    st.markdown("+ **Programming Languages:** Python, Matlab, GNU/Octave, Scheme, Racket, SQL, C \n")
    st.markdown("+ **Markup Languages:** HTML, CSS, Markdown, LaTeX \n")
    st.markdown("+ **Operating Systems:** Linux, MacOS, Windows, FreeBSD \n")
    st.markdown("+ **Platforms and Workflows:** Git, GitHub, Jupyter Notebook, Streamlit, Vscode, Kubernetes")
    st.markdown("+ **Data Science Libraries:** Pandas, Numpy, Matplotlib, Seaborn, Plotly, Scipy \n")
    st.markdown("+ **Machine Learning Frameworks:** Scikit-learn, TensorFlow, Keras, PyTorch, XGBoost \n")

    st.markdown("### Graphics and Multimedia")
    st.markdown("+ **3D Graphics:** Blender")
    st.markdown("+ **CAD:** Solidworks, FreeCAD")
    st.markdown("+ **Raster Graphics:** GIMP, Krita, Affinity Photo, Adobe Photoshop, Pixelmator Pro, ImageMagick")
    st.markdown("+ **Vector Graphics:** Inkscape, Affinity Designer, Adobe Illustrator")
    st.markdown("+ **Video Editing:** DaVinci Resolve, Kdenlive, ffmpeg")
    st.markdown("+ **Audio Editing:** Audacity, Ardour")
    st.divider()

    st.markdown("# Languages")
    st.markdown("+ **Italian:** Native \n")
    st.markdown("+ **English:** C1 \n")
    st.markdown("+ **French:** A2 \n")
    st.divider()

    st.markdown("# Volunteering")
    st.markdown("+ **Tutor** (2018-2021) - \n"
                "I was a tutor for self-coordinated study groups at the Polytechnic University of Turin. \n")
    st.markdown("+ **Blender Teacher** (2021-Present) - \n"
                "I occasionally give free online Blender lectures to people who want to learn 3D modeling. \n") 
    st.divider()
    

    st.markdown("# Hobbies and Interests")
    st.markdown("+ **3D Graphics:** I love creating 3D models and animations, I am a Blender enthusiast. \n")
    st.markdown("+ **Music:** I play the guitar and I love listening to music. \n")
    st.markdown("+ **3D Printing:** I am interested in all Additive Manufacturing technologies. \n")
    st.markdown("+ **Food Science:** I love the engineering of 3D printed food. \n")
    
    
    


elif selected == "3D Artwork":
    st.header('My Blender 3D Artwork')
    st.write("Pick a number of columns for a grid layout, then click on the expand button to see the images in full size.")
    with st.sidebar:
        st.subheader("Number of columns")
        n_cols = int(st.number_input("Enter a number", min_value=1, max_value=5, value=3, step=1))

    n_rows = int(1 + N_IMAGES // n_cols)
    rows = [st.container() for i in range(n_rows)]
    cols = [column for row in rows for column in row.columns(n_cols)]

    for col, image in zip(cols, images):
        with col:
            st.image(image, use_column_width=True)

elif selected == "Procedural Artwork": 
    st.header('My Procedural Artwork')
    st.write("Procedural Artwork is a form of generative art, where the artist creates an algorithm that generates the artwork. \n"
             "These shaders are written in GLSL, a C-like language that is used to write shaders for OpenGL and WebGL. \n")
    components.iframe("https://www.shadertoy.com/embed/dtcXWX?gui=false&t=10&paused=false&muted=false", height=300, scrolling=True)
    components.iframe("https://www.shadertoy.com/embed/mtdXDs?gui=false&t=10&paused=false&muted=false", height=300, scrolling=True)
    components.iframe("https://www.shadertoy.com/embed/DlGXzz?gui=false&t=10&paused=false&muted=false", height=300, scrolling=True)
    components.iframe("https://www.shadertoy.com/embed/dtyXRR?gui=false&t=10&paused=false&muted=false", height=300, scrolling=True)
    components.iframe("https://www.shadertoy.com/embed/dlySzR?gui=false&t=10&paused=false&muted=false", height=300, scrolling=True)


st.sidebar.markdown("### Contact me")
st.sidebar.markdown("+ [**Email**](mailto:detranegiorgio@gmail.com) \n")
st.sidebar.markdown("+ [**LinkedIn**](https://www.linkedin.com/in/giorgiodetrane/) \n")
st.sidebar.markdown("+ [**GitHub**](https://www.github.com/BaldPolnareff) \n")

