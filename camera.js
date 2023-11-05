import React, { useState, useRef } from 'react';
import Webcam from "react-webcam";

function App() {
  const webcamRef = useRef(null);

  const capture = () => {
    const imageSrc = webcamRef.current.getScreenshot();
    // Convert the base64 image data to a Blob
  const blob = dataURItoBlob(imageSrc);

  // Create a download link for the image
  const url = URL.createObjectURL(blob);

  // Create an anchor element for downloading
  const a = document.createElement('a');
  a.href = url;
  a.download = 'webcam-screenshot.jpg';
  a.click();
  };
  function dataURItoBlob(dataURI) {
    const byteString = atob(dataURI.split(',')[1]);
    const ab = new ArrayBuffer(byteString.length);
    const ia = new Uint8Array(ab);
    for (let i = 0; i < byteString.length; i++) {
      ia[i] = byteString.charCodeAt(i);
    }
    return new Blob([ab], { type: 'image/jpeg' });
  }
  return (
    <div className="App">
      <header className="App-header">
        <h1>Live Webcam Feed</h1>
        <Webcam
          audio={false}
          ref={webcamRef}
          screenshotFormat="image/jpeg"
        />
        <button onClick={capture}>Capture Photo</button>
      </header>
    </div>
  );
}

export default App;