import Chatbox from "../components/chatbox";
import MsgBox from "../components/Msgbox";
import "./main.css"
import { useEffect, useState } from "react";
function Main(){
    const [sent, setSent] = useState(false)
    const [message, setMessage] = useState([])
    const [loading, setLoading] = useState(false)

    useEffect(()=>{
        fetch("http://localhost:5000/history")
        .then(res=>res.json())
        .then(data=>{
            if(data.messages.length > 0){
                setMessage(data.messages)
                setSent(true)
            }
        })
    }, [])


    async function sendMessage(input){
        setSent(true)
        setMessage(prev=>[...prev, {role: "user", content: input}])
        setLoading(true)
        const response = await fetch("http://localhost:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: input })
        })
        const data = await response.json()
        setMessage(prev=>[...prev, {role: "ai", content: data.response}])
        setLoading(false)

    }
    return(
        <div className="main">
            <MsgBox messages={message} send={sent} loading={loading} />
            <div className={`Heading ${sent ? "Heading-hidden": "Heading-visible"}`}>Hello, Ayush!</div>
            
            <Chatbox sent={sent} setSent={setSent} sendMessage={sendMessage} />
        </div>
    )
}
export default Main