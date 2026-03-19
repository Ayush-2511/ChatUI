import './ai-msg.css'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
function AiMsg({text}) {
    return (
        <div className="aimsg">
            <ReactMarkdown remarkPlugins={[remarkGfm]}>
                {text}
            </ReactMarkdown>
        </div>
    )
}
export default AiMsg