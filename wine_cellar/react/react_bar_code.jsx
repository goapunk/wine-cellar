import React from "react"
import { createRoot } from 'react-dom/client';
import { BarcodeScanner } from 'react-barcode-scanner'
import "react-barcode-scanner/polyfill"

const Scanner = () => {
    const handleCapture = (captured) => {
        console.log("capt")
        console.log(captured)
    }

  return <BarcodeScanner onCapture={handleCapture} options={{ formats: ['ean_13', 'ean_8', "upc_a"] }} />
}

const init_scanner = () => {
console.log(document.getElementById('scanner'))
const root = createRoot(document.getElementById('scanner'));
root.render(<Scanner />);
}

document.addEventListener('DOMContentLoaded', init_scanner, false)