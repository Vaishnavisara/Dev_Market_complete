from app import app
import os
from dotenv import load_dotenv
load_dotenv() 


# ✅ Set the secret key before running the app
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback_secret_key')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
from dotenv import load_dotenv  # Import dotenv


