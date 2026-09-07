document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".alert-dismissible").forEach(function (alert) {
    setTimeout(function () {
      bootstrap.Alert.getOrCreateInstance(alert).close();
    }, 5000);
  });
});