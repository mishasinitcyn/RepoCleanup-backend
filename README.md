# RepoCleanup backend

## Getting Started
1. Clone the repository
2. Make sure you have python installed
3. Create a virtual environment in the project folder using `python -m venv venv`
4. Activate the environment using `source venv/bin/activate` (on Windows, use `venv\Scripts\activate` instead)
5. Install the required packages using `pip install -r requirements.txt`

You should now be able to open the notebooks (`.ipynb` files) and run the code.

## Running the server
1. Make sure you have the virtual environment activated (see step 4 above)
2. Navigate to the `Server` folder
3. Run the FastAPI server using `uvicorn main:app --reload`
