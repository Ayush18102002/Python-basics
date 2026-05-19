
# pip install transformers
from transformers import pipeline

# Load a pre-trained Transformer model for a specific task (e.g., sentiment analysis)
classifier = pipeline("sentiment-analysis")

# Pass text into the model
result = classifier("The 'Attention Is All You Need' paper is incredibly fascinating!")

print(result)
# Output: [{'label': 'POSITIVE', 'score': 0.9998}]