import React, {useState, useRef, useEffect} from 'react'
import { createRoot } from 'react-dom/client'
import { BarcodeScanner } from 'react-barcode-scanner'
// import 'react-barcode-scanner/polyfill'
import "barcode-detector/polyfill";

const Scanner = () => {
  const [selectedFormat, setSelectedFormat] = useState('any'); // Declare a state variable...
  const defaultFormats = ['ean_13', 'ean_8', 'upc_a', 'code_39', 'itf']
  const canvasRef = useRef(null);
  const scannerRef = useRef(null);
  console.log(selectedFormat)

  const handleCapture = (captured) => {
    if (captured.length > 0) {
       const barcode = captured[0]
      console.log(barcode)
      console.log("found")
  const element = scannerRef.current.firstChild;
    if (element) {
      canvasRef.current.width = element.videoWidth
      canvasRef.current.height = element.videoHeight
    }
       const context = canvasRef.current.getContext("2d");
              context.clearRect(0, 0, canvas.width, canvas.height);
              context.beginPath();
              context.fillStyle = "red";
              context.rect(barcode.boundingBox.x, barcode.boundingBox.y, barcode.boundingBox.width + 100, barcode.boundingBox.height + 100);
              context.fill();
              window.location.href = '/wine/scan/' + captured[0].rawValue
    }
  }

  return (
    <>    <div>
      <select
      value={selectedFormat}
      onChange={e => setSelectedFormat(e.target.value)} // ... and update the state variable on any change!
    >
      <option value="">Any</option>
			<option value="code_39">Code 39</option>
			<option value="code_93">Code 93</option>
			<option value="code_128">Code 128</option>
			<option value="ean_8">EAN-8</option>
			<option value="ean_13">EAN-13</option>
			<option value="itf">ITF</option>
			<option value="upc_a">UPC-A</option>
			<option value="upc_e">UPC-E</option>
      </select>
  </div>
    <div id="scanner" className="form__scanner" ref={scannerRef} >
      <BarcodeScanner onCapture={handleCapture} options={{formats: selectedFormat ? [selectedFormat]: defaultFormats }} />
      <canvas id="canvas" ref={canvasRef} style={{position: "absolute", top:0, width:"100%", height: "100%"}} />
    </div>
</>

  )
}

const initScanner = () => {
  const root = createRoot(document.getElementById('scanner'))
  root.render(<Scanner />)
}

document.addEventListener('DOMContentLoaded', initScanner, false)
