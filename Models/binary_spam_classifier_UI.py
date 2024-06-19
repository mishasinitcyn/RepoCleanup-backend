import os
import joblib
import gradio as gr

# Load the model
RUN_ID = '0579ea92a6c7494e9bfdf42813fe3867'
MODEL_NAME = 'nn'
EXPERIMENT_NAME = '2'
MODEL_URI = os.path.join('mlartifacts', EXPERIMENT_NAME, RUN_ID, 'artifacts', MODEL_NAME, 'model.pkl')
binary_classifier = joblib.load(MODEL_URI)

# Define the prediction function
def classify_text(text):
    prediction = binary_classifier.predict([text])[0]
    return prediction

# Create the Gradio interface
iface = gr.Interface(
    fn=classify_text,
    inputs=gr.Textbox(lines=2, placeholder="Enter text here..."),
    outputs=gr.Textbox(),
    title="Spam GitHub Issues classifier",
    description="Enter concatenated issue title and issue body"
)

# Launch the interface
iface.launch()