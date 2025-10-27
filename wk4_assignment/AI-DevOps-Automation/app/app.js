document.getElementById("loginButton").addEventListener("click", function() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const message = document.getElementById("message");

  if (username === "admin" && password === "12345") {
    message.style.color = "green";
    message.textContent = "✅ Login successful!";
  } else {
    message.style.color = "red";
    message.textContent = "❌ Invalid credentials!";
  }
});
