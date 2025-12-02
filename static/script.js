function lesson(topic) {
    fetch("/lesson", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({topic: topic})
    })
    .then(res => res.json())
    .then(data => {
        let html = `<h2>${data.title}</h2>
            <p><b>What is it?</b> ${data.definition}</p>
            <p><b>Analogy:</b> ${data.analogy}</p>
            <hr>
            <h3>Interactive Console:</h3>
            <div>`;

        if (data.title === "Stack") {
            html += `<input id="stack-ele" placeholder="Enter element">
                <button onclick="push()">PUSH</button>
                <button onclick="pop()">POP</button>`;
        }
        else {
            html += `<input id="queue-ele" placeholder="Enter value">
                <button onclick="enqueue()">ENQUEUE</button>
                <button onclick="dequeue()">DEQUEUE</button>`;
        }
        html += `
            </div>
            <div id="display">Current: [ ${data.data} ]</div>
        `;

        document.getElementById("content").innerHTML = html;
    });
}
function push() {
    let value = document.getElementById("stack-ele").value;
    fetch("/push", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({value: value})
    })
    .then(res => res.json())
    .then(data => display(data.data));
}

function pop() {
    fetch("/pop", {
        method: "POST"
    })
    .then(res => res.json())
    .then(data => display(data.data));
}
