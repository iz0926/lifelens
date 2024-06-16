# lifelens ![Alt text](logo.png)

LifeLens is an app designed for users to capture and reflect on personal moments through media and AI-generated introspective questions. It provides a space for personal growth and self-discovery by combining technology and introspection. The app allows users to upload photos and videos, generate introspective questions based on AI prompts, and reflect on their entries by adding descriptions.

# About
The front-end of LifeLens is built using React Native, while the back-end leverages Appwrite for robust data management and user authentication. For AI processing, Python Flask is used to generate introspective questions, and Node.js serves API requests. Media selection is made seamless through the integration of expo-image-picker and expo-document-picker, allowing users to select images and videos from their devices.

User authentication and session management: During user registration, a new account is created in Appwrite, and the user is automatically signed in. A document containing the user's details (email, username, avatar) is created in the users' collection. The signIn function checks for an existing session and creates a new one if none exists. Users can log out by deleting the current session through the signOut function.

Creating and managing entries: Users provide a title, prompt, question, description, and media (image or video). The uploadFile function uploads the media to Appwrite Storage and returns the file URL. The createEntryPost function then creates a new document in the entries collection with the entry details, including the media URL. Users can fetch their specific entries from the entries collection using the getUserEntries function.

The AI-generated prompts in LifeLens are designed to incite self-reflection. For this, the app uses a pre-trained natural language processing (NLP) model, specifically Google's T5 Flan, which is known for its strong text generation capabilities. This model is integrated into the app using a Flask server to handle the AI processing. Users make a POST request to the Flask server with their input prompt. The server tokenizes the input prompt before passing it to the T5 Flan model to generate an introspective question.

The front-end components, 'Create' and 'Profile', are essential to the user experience. The 'Create' component allows users to create a new entry by providing all necessary details and selecting media from their device. The 'Profile' component displays the entries uploaded by the user, fetching user-specific entries from the entries collection.

LifeLens seamlessly integrates user authentication, session management, and database operations using Appwrite. The authentication flow handles user registration, login, and logout, ensuring secure access to user-specific data. The database management involves creating and retrieving entries, with media uploads handled efficiently. The frontend components like 'Create' and 'Profile' interact with these backend functionalities to provide a cohesive user experience, promoting personal growth and self-reflection through technology.
