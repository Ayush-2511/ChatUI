import AiMsg from './ai-msg'
import './msgbox.css'
import UserMsg from './user-msg'

function MsgBox({messages, send}){
    return (
        <div className={`msgbox ${send ? "msgbox-visible": "msgbox-hidden"}`}>
            {messages.map((msg, i) => (
                msg.role === "user" 
                ? <UserMsg key={i} text={msg.content} className="user-msg" />
                : <AiMsg key={i} text={msg.content} className="ai-msg" />
            ))}
        </div>
    )
}
export default MsgBox