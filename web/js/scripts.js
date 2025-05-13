const form = document.getElementById("loginForm");
const mensagem = document.getElementById("mensagem");

form.addEventListener("submit", function (e) {
  e.preventDefault();

  const user = document.getElementById("user").value;
  const pass = document.getElementById("password").value;

  fetch("http://localhost:5000/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: `user=${encodeURIComponent(user)}&password=${encodeURIComponent(
      pass
    )}`,
  })
    .then((res) => {
      if (res.ok) {
        alert("✅ Login enviado ao servidor!");
      } else {
        mensagem.style.display = "block";
        mensagem.textContent = "❌ Erro no login.";
      }
    })
    .catch((err) => {
      console.error(err);
      mensagem.style.display = "block";
      mensagem.textContent = "❌ Erro de rede.";
    });
});
