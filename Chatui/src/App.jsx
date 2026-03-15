import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Loading from './components/Loading'
import Main from './Pages/Main'
import './App.css'


function App() {
  const[loading,setLoading] = useState(true)
  useEffect(()=>{
    setTimeout(()=>{
      setLoading(false)
    },7500)
  },[])

  if(loading){
    return <Loading />
  }
  return(<div>
    <Main />
  </div>)
}

export default App
