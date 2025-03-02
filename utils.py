import psycopg2
import boto3
from werkzeug.utils import secure_filename
import os
from dotenv import load_dotenv

load_dotenv()

# PostgreSQL Configuration
DB_PARAMS = {
    'dbname': 'flask_app',   # Make sure this matches your DB name
    'user': 'postgres',        # Your Postgres username
    'password': 'password', # Your Postgres password
    'host': 'localhost',
    'port': '5432'
}

# AWS S3 Configuration (optional - only if you want real S3 image uploads)
S3_BUCKET = os.getenv("S3_BUCKET", "default")
S3_REGION = os.getenv("S3_REGION", "default")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY", "default")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY", "default")

s3 = boto3.client(
    's3',
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY
)

def get_db_connection():
    """
    Connects to PostgreSQL using the above DB_PARAMS.
    """
    return psycopg2.connect(**DB_PARAMS)

def upload_image(image):
    """
    Uploads the image to S3 (currently commented out).
    Returns an image_url. Right now, we just return a placeholder.
    """
    filename = secure_filename(image.filename)

    # If you want to upload to S3 for real, uncomment:
    # s3.upload_fileobj(image, S3_BUCKET, filename)
    # image_url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{filename}"

    # For now, returning a placeholder image (for testing):
    placeholder_url = "https://images.pexels.com/photos/1054666/pexels-photo-1054666.jpeg"
    return placeholder_url
