import Chatbox from "../components/chatbox";
import MsgBox from "../components/Msgbox";
import "./main.css"
import { useState } from "react";
function Main(){
    const [sent, setSent] = useState(false)
    return(
        <div className="main">
            <MsgBox messages={""} send={sent} />
            <div className={`Heading ${sent ? "Heading-hidden": "Heading-visible"}`}>Hello, Ayush!</div>
            
            <Chatbox sent={sent} setSent={setSent}/>
        </div>
    )
}
export default Main