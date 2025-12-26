function deleteTask(taskId) {
  fetch('/delete-task', {
    method: 'POST',
    body: JSON.stringify({ taskId: taskId }),
    headers: {
      'Content-Type': 'application/json'
    }
  }).then(() => {
    window.location.href = "/";
  });
}
