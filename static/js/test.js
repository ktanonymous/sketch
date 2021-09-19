var calendar = null;

document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: ['interaction', 'dayGrid', 'timeGrid', 'list', 'moment'],
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
        },
        locale: 'ja',
        businessHours: true,
        // timeZone: 'Asia/Tokyo',
        eventTimeFormat: { hour: 'numeric', minute: '2-digit' },
        defaultView: 'dayGridMonth',
        navLinks: true, // can click day/week names to navigate views
        selectable: true,
        selectMirror: true,
        select: function (arg) {
            isCountOK = checkEventNum(5);
            if (isCountOK) {
                const title = '候補';
                if (title) {
                    calendar.addEvent({
                        title: title,
                        start: arg.start,
                        end: arg.end,
                        allDay: arg.allDay
                    })
                }
            } else {
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

        eventDrop: function (info) {
            setDateValue();
        },
        eventResize: function (info) {
            setDateValue();
        },
        eventClick: function (info) {
            isOK = confirm('削除していいですか？');
            if (isOK) {
                info.event.remove();
                initializeDateValue();
                setDateValue();
            }
        },
    });

    calendar.render();

    function initializeDateValue() {
        for (let i = 0; i < 5; i++) {
            let element = document.getElementById(i + 1);
            date_table.rows[i].cells[1].innerText = '';
            element.removeAttribute('value');
        }
    }

    function setDateValue() {
        let events = calendar.getEvents();
        const eventsLength = events.length;
        for (let i = 0; i < eventsLength; i++) {
            let element = document.getElementById(i + 1);
            startDateString = events[i].start.toString();
            endDateString = events[i].end.toString();
            startDate = formatDate(startDateString);
            endDate = formatDate(endDateString);
            date_table.rows[i].cells[1].innerText = startDate + '〜' + endDate;
            element.value = startDate + '〜' + endDate;
        }
    }
    function formatDate(dateString) {
        let date = new Date(dateString);
        let formatedDate = date.getMonth() + '月' + date.getDate() + '日(' + new String('日月火水木金土').charAt(date.getDay()) + ')';
        let formatedTime = date.getHours() + ':' + ('0' + date.getMinutes()).slice(-2);
        return formatedDate + formatedTime;
    }

    function checkEventNum(num) {
        let count = 0;
        let events = calendar.getEvents();

        for (let i = 0; i < events.length; i++) {
            count++;
            if (count == num) {
                return false;
            }
        }
        return true;
    }
});
