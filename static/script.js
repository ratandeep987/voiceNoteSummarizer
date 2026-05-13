const form = document.getElementById("uploadForm");

const fileInput = document.getElementById("audioFile");

const filePreview = document.getElementById("filePreview");

const fileName = document.getElementById("fileName");

const loading = document.getElementById("loading");

const transcription = document.getElementById("transcription");

const summary = document.getElementById("summary");

const submitBtn = document.getElementById("submitBtn");


// SHOW FILE NAME

fileInput.addEventListener("change", () => {

    if(fileInput.files.length > 0){

        const file = fileInput.files[0];

        filePreview.classList.remove("hidden");

        fileName.innerText = file.name;

    }

});


// FORM SUBMIT

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    if(fileInput.files.length === 0){

        alert("Please upload an audio file");

        return;

    }

    loading.classList.remove("hidden");

    submitBtn.innerText = "Processing...";
    submitBtn.disabled = true;

    const formData = new FormData();

    formData.append("audio", fileInput.files[0]);

    try{

        const response = await fetch("/upload", {

            method:"POST",
            body:formData

        });

        const data = await response.json();

        transcription.innerText = data.transcription;

        summary.innerText = data.summary;

    }

    catch(error){

        alert("Something went wrong");

    }

    finally{

        loading.classList.add("hidden");

        submitBtn.innerText = "Generate Summary";

        submitBtn.disabled = false;

    }

});