from flask import Flask, request, jsonify
from transformers import T5Tokenizer, T5ForConditionalGeneration

app = Flask(__name__)

# load the pre-trained model and tokenizer
model_name = 'google/flan-t5-base'
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

@app.route('/getQuestion', methods=['POST'])
def get_question():
    try:
        data = request.json
        prompt = data.get('prompt')
        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400

        # generate question
        input_text = f"Generate an open-ended and get-to-know-you question based on the words: {prompt}."
        input_ids = tokenizer.encode(input_text, return_tensors='pt')
        output = model.generate(input_ids, max_length=50, num_return_sequences=1)
        question = tokenizer.decode(output[0], skip_special_tokens=True)

        return jsonify({"question": question})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)