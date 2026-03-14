const chatBox = document.getElementById("chat-box");
const input = document.getElementById("message-input");
const typingIndicator = document.getElementById("typing-indicator");


// ENTER KEY SEND
function handleKey(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}


// SEND MESSAGE
async function sendMessage() {

    const message = input.value.trim();

    if (!message) return;

    // USER MESSAGE
    const userMessage = document.createElement("div");
    userMessage.className = "user-message";
    userMessage.innerText = message;

    chatBox.appendChild(userMessage);

    input.value = "";

    scrollToBottom();

    // SHOW TYPING
    typingIndicator.classList.remove("d-none");

    try {

        const response = await fetch("http://localhost:8000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        // HIDE TYPING
        typingIndicator.classList.add("d-none");

        // BOT MESSAGE CONTAINER
        const botMessage = document.createElement("div");
        botMessage.className = "bot-message";

        chatBox.appendChild(botMessage);

        // TYPE TEXT LIKE AI
        typeMessage(botMessage, data.reply);

        scrollToBottom();

    } catch (error) {

        typingIndicator.classList.add("d-none");

        const errorMessage = document.createElement("div");
        errorMessage.className = "bot-message";
        errorMessage.innerText = "⚠️ Server error. Please try again.";

        chatBox.appendChild(errorMessage);

        scrollToBottom();
    }
}


// AI TYPING EFFECT
function typeMessage(element, text, speed = 15) {

    let i = 0;

    function typing() {

        if (i < text.length) {

            element.innerHTML += text.charAt(i);

            i++;

            scrollToBottom();

            setTimeout(typing, speed);
        }
    }

    typing();
}


// AUTO SCROLL
function scrollToBottom() {
    chatBox.scrollTop = chatBox.scrollHeight;
}