function addTask() {
    let taskName = document.getElementById("taskInput").value.trim();

    if (taskName === "") {
        alert("Task name cannot be empty!");
        return;
    }

    fetch("/add_task", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ title: taskName })
    })
    .then(response => response.json())
    .then(data => {
        let list = document.getElementById("taskList");
        let li = document.createElement("li");
        li.className = "task-item";
        li.innerHTML = "<strong>" + data.title + "</strong> - " + data.status;
        list.appendChild(li);
        document.getElementById("taskInput").value = "";
    });
}
