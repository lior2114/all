from flask import Blueprint, send_from_directory
import os

upload_bp = Blueprint('upload', __name__)

# הוספת route לשרת תמונות שהועלו
@upload_bp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

# הוספת route לשרת תמונות פרופיל
@upload_bp.route('/uploads/profile_images/<filename>')
def profile_image_file(filename):
    return send_from_directory('uploads/profile_images', filename)
