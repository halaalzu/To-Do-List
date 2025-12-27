function deleteTask(taskId){
    fetch('/delete-task', {
        method: 'POST', 
        body:JSON.stringify({ taskId: taskId})
    }).then((res) => {
        window.location.hreg = "/"
    });
}

function toggleTask(taskId) {
  fetch("/toggle-task", {
    method: "POST",
    body: JSON.stringify({ taskId: taskId }),
  }).then(() => {
    window.location.reload();
  });
}
