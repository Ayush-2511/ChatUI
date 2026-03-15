import './msgbox.css'

function MsgBox({messages, send}){
    return (
        <div className={`msgbox ${send ? "msgbox-visible": "msgbox-hidden"}`}>

        </div>
    )
}
export default MsgBox