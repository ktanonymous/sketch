var calendar = null;

document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
    plugins: ['interaction', 'dayGrid', 'timeGrid', 'list'],
    header: {
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
    },
    locale: 'ja',
    businessHours: true,
    timeZone: 'Asia/Tokyo',
    eventTimeFormat: { hour: 'numeric', minute: '2-digit' },
    defaultView: 'dayGridMonth', // プラグインが必要そう
    navLinks: true, // can click day/week names to navigate views
    selectable: true,
    selectMirror: true,
    select: function (arg) {
        isOK = confirm('追加していいですか？');
        if(isOK){
            var title = '候補';
                if (title) {
                calendar.addEvent({
                    title: title,
                    start: arg.start,
                    end: arg.end,
                    allDay: arg.allDay
                })
            }
        }
        calendar.unselect()
    },
    editable: true,
    eventLimit: true, // allow "more" link when too many events
    events: [
        {
        groupId: 999,
        title: 'Repeating Event',
        start: '2019-08-09T16:00:00'
        },
        // './getEvents.php',
    ],
    });

    calendar.render();
    var events = calendar.getEvents();
    let c = 0
    for(var i=0; i<events.length; i++){
    c++;
    console.log(events[i]);
    }
    if(c>5){
        alert("数を減らしてください");
    }
});

