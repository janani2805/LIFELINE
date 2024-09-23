// JavaScript file: chatbot.js

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const chatBox = document.getElementById('chat-box');
    
    // Display user's message
    chatBox.innerHTML += `<p>You: ${userInput}</p>`;
    
    // Bot response
    const botResponse = getBotResponse(userInput);
    chatBox.innerHTML += `<p>Bot: ${botResponse}</p>`;
    
    // Clear input field after sending the message
    document.getElementById('user-input').value = '';

    // Scroll to the bottom of the chat box
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Function to generate bot response based on user input
function getBotResponse(input) {
    input = input.toLowerCase();

    // Responses based on symptoms including fever, cramps, cold, and trauma
    if (input.includes("fever")) {
        return "A fever is usually a sign of infection. Here are some tips:\n\n" +
               "1. Rest and stay hydrated.\n" +
               "2. Use over-the-counter medication to reduce fever, such as acetaminophen.\n" +
               "3. Seek medical advice if the fever is above 103°F or lasts longer than three days.";
    } else if (input.includes("cramps")) {
        return "Cramps can be caused by various factors, including menstrual pain or muscle strain. Here’s what you can do:\n\n" +
               "1. Stretch gently and massage the affected area.\n" +
               "2. Apply heat using a heating pad or warm bath.\n" +
               "3. If cramps persist or worsen, seek medical attention.";
    } else if (input.includes("cold")) {
        return "A common cold can cause sneezing, runny nose, and sore throat. To manage cold symptoms:\n\n" +
               "1. Stay hydrated by drinking water and clear fluids.\n" +
               "2. Rest and avoid stress.\n" +
               "3. Use over-the-counter medications for symptom relief.";
    } else if (input.includes("trauma")) {
        return "Trauma can refer to physical injuries or emotional stress. Here are a few steps to handle physical trauma:\n\n" +
               "1. Seek immediate medical care for severe injuries.\n" +
               "2. Apply ice to reduce swelling for minor injuries.\n" +
               "3. For emotional trauma, consider speaking with a mental health professional.";
    } else {
        return "I'm sorry, I don't have information on that. Please consult a healthcare provider for more detailed advice.";
    }
}
