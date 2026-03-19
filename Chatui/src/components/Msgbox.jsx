import AiMsg from './ai-msg'
import './msgbox.css'
import UserMsg from './user-msg'
import { useEffect, useRef } from 'react'

function MsgBox({messages, send}){
    const bottomref = useRef(null);
    useEffect(() => {
        if(bottomref.current){
            bottomref.current.scrollIntoView({behavior: "smooth"});
        }
    }, [messages])
    return (
        <div className={`msgbox ${send ? "msgbox-visible": "msgbox-hidden"}`}>
            {messages.map((msg, i) => (
                msg.role === "user" 
                ? <UserMsg key={i} text={msg.content} className="user-msg" />
                : <AiMsg key={i} text={msg.content} className="ai-msg" />
            ))}
            <div ref={bottomref} className='ref'/>
        </div>
    )
}
export default MsgBox