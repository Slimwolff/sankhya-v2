const express = require("express");

const app = express();
const port = 5555 || process.env.SERVER_PORT;

let globalConfig = {}

// Adicionar os cabeçalhos Access-Control-Allow-Origin
app.use((req, res, next) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.header(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept"
  );
  next();
});

app.post("/setConfig", async (req, res) => {
  res.json("Hello");
  data = await req.body
  console.log(data);
  
});

app.get("/getConfig", (req, res) => {
  res.json("Hello");
});

app.listen(port, () => console.log(`Listening on port ${port}`));