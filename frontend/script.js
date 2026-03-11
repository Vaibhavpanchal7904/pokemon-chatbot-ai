async function sendMessage(){

const input = document.getElementById("message-input");
const chatBox = document.getElementById("chat-box");
const typing = document.getElementById("typing-indicator");

const message = input.value.trim();

if(message === ""){
alert("Please enter a message");
return;
}

/* USER MESSAGE */

const userDiv = document.createElement("div");
userDiv.className = "user-message";
userDiv.innerText = message;

chatBox.appendChild(userDiv);

input.value = "";

/* SHOW TYPING */

typing.classList.remove("d-none");

chatBox.scrollTop = chatBox.scrollHeight;

try{

const response = await fetch("http://127.0.0.1:8000/chat",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({message:message})
});

/* SERVER ERROR */

if(!response.ok){
throw new Error("Server error");
}

const data = await response.json();

/* HIDE TYPING */

typing.classList.add("d-none");

/* BOT MESSAGE */

const botDiv = document.createElement("div");
botDiv.className = "bot-message";
botDiv.innerText = data.reply || "No response received";

chatBox.appendChild(botDiv);

chatBox.scrollTop = chatBox.scrollHeight;

}catch(error){

typing.classList.add("d-none");

const errorDiv = document.createElement("div");
errorDiv.className = "bot-message";
errorDiv.style.background = "red";
errorDiv.innerText = "Error connecting to server";

chatBox.appendChild(errorDiv);

}

}

/* ENTER KEY SUPPORT */

function handleKey(event){
if(event.key === "Enter"){
sendMessage();
}
}