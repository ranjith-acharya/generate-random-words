document.getElementById("get-word-btn").addEventListener("click", function() {
    fetch("/get_word")
    .then(response => response.json())
    .then(data => {
        document.getElementById("word").textContent = data.word;
    });
});
