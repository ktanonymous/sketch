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
            isCountOK = checkCountEvent(5);
            if(isCountOK){
                isOK = confirm('追加していいですか？');
                if (isOK) {
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
            }else{
                alert("選択数を減らしてください");
            }
            setDateValue();
            calendar.unselect()
        },
        editable: true,
        eventLimit: true, // allow "more" link when too many events
        events: [
            // {
            //     groupId: 999,
            //     title: 'Repeating Event',
            //     start: '2019-08-09T16:00:00'
            // },
            // './getEvents.php',
        ],
    });

    calendar.render();
    
    function setDateValue(){
        var events = calendar.getEvents();
        for (let i = 0; i < events.length; i++ ){
            let element = document.getElementById(i+1);
            element.value = events[i];
            date_table.rows[i].cells[1].innerText = events[i].start + events[i].end + events[i].allDay;

        }    
    }
    
    function checkCountEvent(num){
        let count = 0;
        var events = calendar.getEvents();

        for (var i = 0; i < events.length; i++) {
            count++;
            if (count == num) {
                return false;
            }
        }
        return true;
    }

});
