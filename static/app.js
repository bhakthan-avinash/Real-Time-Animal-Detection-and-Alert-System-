function startAlarm() {
    let alarm = document.getElementById("alarm");
    alarm.play();
}

function stopAlarm() {
    let alarm = document.getElementById("alarm");
    alarm.pause();
    alarm.currentTime = 0;
}