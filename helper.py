import ollama

def get_model_list():
    models_data = ollama.list()
    models = [model['model'] for model in models_data.get('models', [])]
    return models
