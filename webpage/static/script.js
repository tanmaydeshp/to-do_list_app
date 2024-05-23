function delete_task(taskID) {
    fetch("/delete_task/", {
      method: "POST",
      body: JSON.stringify({ taskID: taskID }),
    }).then((_res) => {
      window.location.href = "/todos";
    });
  }

function close(){
  fetch(window.location.href, {method: "GET"})
};
