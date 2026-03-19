import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Loading from './components/Loading'
import Main from './Pages/Main'
import './App.css'


function App() {

  const[loading,setLoading] = useState(true)
  useEffect(()=>{
    const res = fetch("http://localhost:5000/background")
    .then(res=>res.json())
    .then(data=>{
      document.body.style.backgroundImage = `url(${data.img_url})`
      document.body.style.backgroundSize = "cover"
      document.body.style.backgroundPosition = "center"
    })
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
