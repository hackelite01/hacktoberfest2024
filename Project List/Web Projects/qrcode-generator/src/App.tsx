import { useState } from 'react'
import QRCode from "react-qr-code";
import './App.css'

function App() {
  const [value, setValue] = useState('')
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
      setValue(event.target.value)
  }
  return (
    <>
      <div style={{display:'flex',width:'100vh', justifyContent:'space-around'}}>
        <div >
          <h2>Please enter any string or Url</h2>
          <input onChange={handleChange} placeholder='' value={value}  style={{width:'100%'}}/>
        </div>
        <div>
          <div style={{ height: "auto", margin: "0 auto", width: "100%" }}>
            <QRCode
              size={256}
              style={{ height: "auto", maxWidth: "100%", width: "100%" }}
              value={value}
              viewBox={`0 0 256 256`}
            />
          </div>
        </div>
      </div>

    </>
  )
}

export default App