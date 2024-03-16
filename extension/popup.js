const btn = document.getElementById("translate");
const inputText = document.getElementById("englishText");
const audioPlayer = document.getElementById("audioPlayer");

btn.addEventListener("click", function() {
    btn.disabled = true;
    btn.innerHTML = "Translating and getting audio...";
    btn.style.boxShadow = 'None';

    const text = inputText.value;
    const xhr = new XMLHttpRequest();

    xhr.open("GET", "http://127.0.0.1:5000/answer?url=" + encodeURIComponent(text), true);

    xhr.onload = function() {
        const response = JSON.parse(xhr.responseText);
        const audioUrl = response.audio_url;
        audioPlayer.src = audioUrl;
        audioPlayer.style.display = "block";
        audioPlayer.play();
        
        btn.disabled = false;
        btn.innerHTML = "Translate to Hindi and Get Audio";
        btn.style.boxShadow = '5px 5px 5px rgba(0, 0, 0, 0.3)';
    };

    xhr.send();
});
