import { memo } from 'react'
import './user-msg.css'

const UserMsg = memo(function UserMsg({text}) {
    return (
        <div className="usermsg">
            {text}
        </div>
    )
})
export default UserMsg