import './chatbox.css'
import { useState } from 'react';
function Chatbox({sent, setSent, sendMessage}){
    const [input, setInput] = useState("");
    
    function HandleChange(e) {
        setInput(e.target.value);
        e.target.style.height = "auto";
        e.target.style.height = (e.target.scrollHeight+1.5) + "px";

        if (e.target.scrollHeight > 225) {
            e.target.style.overflowY = "scroll";
        } else {
            e.target.style.overflowY = "hidden";
        }
    }
    function changeInput() {
        if (!input.trim()) return;
        sendMessage(input);
        setInput("");
        document.querySelector(".input").style.height = "50px";
    }

    function handleKeyDown(e) {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            changeInput();
        }
    }
    return (
        <div className={`chatbox ${sent ? "chatbox-anim": "chatbox-static"}`}>
            <textarea type="text"
                value={input}
                onChange={HandleChange}
                onKeyDown={handleKeyDown}
                rows={1}
                className="input"/>
            <button className="send" onClick={changeInput}></button>
        </div>
    )
}
export default Chatbox


// --legacy--
{/* <div className="chatarea">
            <div className={`chatbox ${sent ? "chatbox-anim": "chatbox-static"}`}>
        <textarea type="text"
                value={input}
                onChange={HandleChange}
                rows={1}
                className="input"/>
            <button className="send" onClick={changeInput}></button>
            </div>
        </div> */}