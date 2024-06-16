import express from 'express';
import fetch from 'node-fetch';

const app = express();
const PORT = 3000;

app.use(express.json());

const PYTHON_API_URL = "http://localhost:5000/getQuestion";

app.post('/getQuestion', async (req, res) => {
    try {
        const response = await fetch(PYTHON_API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt: req.body.prompt }),
        });

        const data = await response.json();
        if (response.ok) {
            res.json({ question: data.question });
        } else {
            res.status(400).json({ error: data.error || 'Could not generate a question. Please try again.' });
        }
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});