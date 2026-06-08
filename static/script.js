function goToMainPage(){

    window.location.href = "/main";
}

function changeLanguage(language){

    if(language === "hindi"){

        document.getElementById("welcomeText").innerHTML =
            `
            कृषिमित्र में आपका स्वागत है,
            जहाँ आप यह जान सकते हैं
            कि कौन सी फसल उगानी चाहिए।
            `;

        document.getElementById("nextBtn").innerHTML =
            "आगे बढ़ें";
    }

    else{

        document.getElementById("welcomeText").innerHTML =
            `
            Welcome to KrishiMitra,
            where you can take guidance
            on which crop to grow.
            `;

        document.getElementById("nextBtn").innerHTML =
            "Next";
    }
}

function predictCrop(){

    let nitrogen =
        document.getElementById("nitrogen").value;

    let crop;

    if(nitrogen > 80){
        crop = "Rice";
    }

    else{
        crop = "Chickpea";
    }

    document.getElementById("result").innerHTML =
        "Recommended Crop: " + crop;
}

function changeInputMode(){

    let selectedMode =
        document.querySelector(
            'input[name="inputMode"]:checked'
        ).value;

    let numberInputs =
        document.querySelectorAll(".numberInput");

    let sliderInputs =
        document.querySelectorAll(".sliderInput");

    if(selectedMode === "slider"){

        numberInputs.forEach(input => {
            input.style.display = "none";
        });

        sliderInputs.forEach(input => {
            input.style.display = "block";
        });
    }

    else{

        numberInputs.forEach(input => {
            input.style.display = "block";
        });

        sliderInputs.forEach(input => {
            input.style.display = "none";
        });
    }
}