document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.querySelector("canvas");
    const context = canvas.getContext("2d");
    const video = document.querySelector('#myVidPlayer');
    
    let w, h;
    
    function snapshot() {
        context.clearRect(0, 0, w, h);
        context.drawImage(video, 0, 0, w, h);
        canvas.style.display = "block";
        
        let ctx = canvas.getContext('2d');
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        
        let image = canvas.toDataURL('image/jpeg');
        
        try {
            localStorage.setItem("elephant", image);
        } catch (e) {
            console.log("Storage failed: " + e);
        }
    }
    
    window.navigator.mediaDevices.getUserMedia({ video: true, audio: true })
        .then(stream => {
            video.srcObject = stream;
            video.onloadedmetadata = (e) => {
                video.play();
                
                w = video.videoWidth;
                h = video.videoHeight;
                
                canvas.width = w;
                canvas.height = h;
            };
        })
        .catch(error => {
            alert('You have to enable the mic and the camera');
        });

    // Attach the snapshot function to the button click event
    document.querySelector("button").addEventListener("click", snapshot);
});
