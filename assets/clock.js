document.addEventListener('DOMContentLoaded', function() {
function updateClock() {const clock=document.getElementById('local-clock');
    if (clock) {
        clock.textContent=new Date().toLocaleTimeString(undefined,
            {
                hour:'2-digit',
                minute:'2-digit',
                second:'2-digit',
            }
        );
    }
}

    updateClock();
    setInterval(updateClock, 1000)
});    