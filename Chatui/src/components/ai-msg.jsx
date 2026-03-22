import './ai-msg.css'
import remarkGfm from 'remark-gfm'
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter'
import { oneDark } from 'react-syntax-highlighter/dist/esm/styles/prism'
import { memo, lazy, Suspense } from 'react'
const ReactMarkdown = lazy(() => import('react-markdown'))
const AiMsg = memo(function AiMsg({text}) {
    return (
        <div className="aimsg">
            <Suspense fallback={<div className='markdown-placeholder'>Loading...</div>}>
            <ReactMarkdown remarkPlugins={[remarkGfm]} components={{
                code({node, inline, className, children, ...props}) {
                    const match = /language-(\w+)/.exec(className || '');
                    return !inline && match ? (
                        <SyntaxHighlighter style={oneDark} language={match[1]} PreTag="div" {...props}>
                            {String(children).replace(/\n$/, '')}
                        </SyntaxHighlighter>
                    ) : (
                        <code className={className} {...props}>
                            {children}
                        </code>
                    );
                }
            }}>
                {text}
            </ReactMarkdown>
            </Suspense>
        </div>
    )
})
export default AiMsg