import React, { useEffect, useState } from 'react';
import './App.css';
import { GoogleGenerativeAI } from "@google/generative-ai"

function App() {
  const [messages, setMessages] = useState([]);
  
  const genAI = new GoogleGenerativeAI(process.env.REACT_APP_API_KEY);
  const model = genAI.getGenerativeModel({model:"gemini-1.5-flash"})
  // const prompt = "What is your name"
  const buttonClick = async () => {
    const messageInput = document.getElementById("message");
    const userMessage = messageInput.value.trim(); 
  
    if (userMessage) {
      const newMessage = { value: userMessage, user: "user" };
      console.log(newMessage);
  
      setMessages((prevMessages) => {
        const updatedMessages = [...prevMessages, newMessage];
        console.log(updatedMessages);
        return updatedMessages;
      });
  
      messageInput.value = ""; 
  
      try {
        const result = await model.generateContent([{ text: userMessage }]); 
        const shown = result.response.text(); 
        console.log(shown);
  
        setMessages((prevMessages) => [
          ...prevMessages,
          { value: shown, user: "bot" }
        ]);
      } catch (error) {
        console.error("Error generating content:", error);
      }
    }
  };
  

  useEffect(() => {
    // console.log(process.env.REACT_APP_API_KEY )
  }, [messages]); 

  return (
    <div className="App">
      <header className='App-header'>Chatbot</header>
      <main>
        <div className='MessageSection'>
        {messages.map((message, index) => (
            <div key={index} className={message.user}>{message.value}</div>
          ))}
        </div>
        <div className='InputSection'>
          <input type="text" placeholder="Enter your message" id="message" required />
          <button id="submit" onClick={buttonClick}>Submit</button>
        </div>
      </main>
    </div>
  );
}

export default App;
