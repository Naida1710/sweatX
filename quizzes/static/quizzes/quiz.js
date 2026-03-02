function checkAnswer(correct) {
    const resultDiv = document.getElementById("result");
    const selected = event.target.innerText;
  
    if (parseInt(selected) === correct) {
      resultDiv.innerText = "Correct! 🎉";
      resultDiv.style.color = "green";
    } else {
      resultDiv.innerText = "Wrong! Try again.";
      resultDiv.style.color = "red";
    }
  }
  