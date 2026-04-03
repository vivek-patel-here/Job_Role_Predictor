FROM python:3.11-slim
WORKDIR /app

# Copy all files
COPY app.py .
COPY requirements_prod.txt .
COPY model/model.pkl model/model.pkl
COPY data/processed/label_encoder.pkl data/processed/label_encoder.pkl
COPY data/processed/tfidf_vectorizer.pkl data/processed/tfidf_vectorizer.pkl


# Install dependencies
RUN pip install --no-cache-dir -r requirements_prod.txt

# Expose port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]