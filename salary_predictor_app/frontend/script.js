document.getElementById("predict-form").addEventListener("submit", async function (e) {
  e.preventDefault();

  const inputData = {
    age: parseInt(document.getElementById("age").value),
    education: document.getElementById("education").value,
    occupation: document.getElementById("occupation").value,
    fnlwgt: parseInt(document.getElementById("fnlwgt").value),
    workclass: document.getElementById("workclass").value,
    "marital-status": document.getElementById("marital-status").value,
    relationship: document.getElementById("relationship").value,
    gender: document.getElementById("gender").value,
    race: document.getElementById("race").value,
    "native-country": document.getElementById("native-country").value,
    "capital-gain": parseInt(document.getElementById("capital-gain").value),
    "capital-loss": parseInt(document.getElementById("capital-loss").value),
    "hours-per-week": parseInt(document.getElementById("hours-per-week").value),
    "educational-num": parseInt(document.getElementById("educational-num").value),
  };

  try {
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(inputData),
    });

  const result = await response.json();

    if (result.probability !== undefined && result.label) {
      document.getElementById("output").innerText =
        `🔮 ${result.label}\n💯 Percentage chance of salary > ₹50K: ${result.probability}%`;
    } else {
      document.getElementById("output").innerText = `⚠️ Error: ${result.error}`;
    }
  } catch (error) {
    document.getElementById("output").innerText = `⚠️ Request failed: ${error}`;
  }
});