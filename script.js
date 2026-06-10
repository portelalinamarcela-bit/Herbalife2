fetch("https://TU-APP.up.railway.app/api/login", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    correo: "algo@correo.com",
    contrasena: "1234"
  })
})
.then(res => res.json())
.then(data => console.log(data));