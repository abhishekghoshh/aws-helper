

<!-- ## Cloud Practitioner

![Cloud Practitioner](./slides/Cloud-Practitioner/AWS%20Certified%20Cloud%20Practitioner%20Slides%20v26.pdf){ type=application/pdf style="min-height:100vh;width:100%" }


## Developer Associate

![Developer Associate](./slides/Developer-Associate/AWS%20Certified%20Developer%20Slides%20v4.9.3.pdf){ type=application/pdf style="min-height:100vh;width:100%" }


## Solutions Architect

![Solutions Architect](./slides/Solutions-Architect/AWS-Certified-Solutions-Architect-Slides.pdf){ type=application/pdf style="min-height:100vh;width:100%" }

 -->


<style>
    body {
        font-family: Arial, sans-serif;
        text-align: center;
    }
    label {
        font-size: 16px;
        font-weight: bold;
    }
    select {
        padding: 10px;
        font-size: 16px;
        margin: 10px 0;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: #f8f8f8;
        cursor: pointer;
    }
    iframe {
        border: 1px solid #ddd;
        border-radius: 5px;
        width: 100%;
        height: 600px;
        display: none;
    }
    button {
        margin-top: 10px;
        padding: 10px 15px;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        background-color: #007BFF;
        color: white;
        cursor: pointer;
    }
    button:hover {
        background-color: #0056b3;
    }
</style>

<label for="pdf-selector">Select a PDF:</label>
<select id="pdf-selector" onchange="showPDF()">
    <option value="">--Select a PDF--</option>
    <option value="./Cloud-Practitioner/AWS%20Certified%20Cloud%20Practitioner%20Slides%20v26.pdf">Cloud Practitioner</option>
    <option value="./Developer-Associate/AWS%20Certified%20Developer%20Slides%20v4.9.3.pdf">Developer Associate</option>
    <option value="./Solutions-Architect/AWS-Certified-Solutions-Architect-Slides.pdf">Solutions Architect</option>
</select>
<button onclick="openFullScreen()">Full Screen</button>

<iframe id="pdf-frame" allowfullscreen></iframe>

<script>
    function showPDF() {
        var pdfFrame = document.getElementById("pdf-frame");
        var selector = document.getElementById("pdf-selector");
        var selectedPDF = selector.value;
        
        if (selectedPDF) {
            pdfFrame.src = selectedPDF;
            pdfFrame.style.display = "block";
        } else {
            pdfFrame.style.display = "none";
        }
    }
    
    function openFullScreen() {
        var pdfFrame = document.getElementById("pdf-frame");
        if (pdfFrame.style.display !== "none") {
            if (pdfFrame.requestFullscreen) {
                pdfFrame.requestFullscreen();
            } else if (pdfFrame.mozRequestFullScreen) { /* Firefox */
                pdfFrame.mozRequestFullScreen();
            } else if (pdfFrame.webkitRequestFullscreen) { /* Chrome, Safari & Opera */
                pdfFrame.webkitRequestFullscreen();
            } else if (pdfFrame.msRequestFullscreen) { /* IE/Edge */
                pdfFrame.msRequestFullscreen();
            }
        }
    }
</script>