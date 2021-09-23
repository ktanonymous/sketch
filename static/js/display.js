var calendar = null;

document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: ['interaction', 'dayGrid', 'timeGrid', ],
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        locale: 'ja',
        businessHours: true,
        // timeZone: 'Asia/Tokyo',
        eventTimeFormat: {
            hour: 'numeric',
            minute: '2-digit'
        },
        defaultView: 'dayGridMonth',
        aspectRatio: 1.6,
        // height: auto,
        navLinks: true, // can click day/week names to navigate views
        selectable: false,
        selectMirror: true,
        editable: false,
        eventLimit: true, // allow "more" link when too many events
        events: [
            // {
            //     groupId: 999,
            //     title: 'Repeating Event',
            //     start: '2021-09-09T16:00:00'
            // },
        ],

        // eventClick: function (info) {
        //     isOK = confirm('削除していいですか？');
        //     if (isOK) {
        //         info.event.remove();
        //         initializeDateValue();
        //         setDateValue();
        //     }
        // },
    });

    let newEvent = [{
            title: '候補',
            start: data.date1_start,
            end: data.date1_end,
        },
        {
            title: '候補',
            start: data.date2_start,
            end: data.date2_end,
        },
        {
            title: '候補',
            start: data.date3_start,
            end: data.date3_end,
        },
        {
            title: '候補',
            start: data.date4_start,
            end: data.date4_end,
        },
        {
            title: '候補',
            start: data.date5_start,
            end: data.date5_end,
        },
    ]
    newEventLength = newEvent.length
    for (i = 0; i < newEventLength; i++) { //TODO:nullのままでいいか
        console.log(newEvent[i]);
        calendar.addEvent(newEvent[i]);
    }
    console.log(newEvent);
    calendar.render();

    function formatDate(dateString) {
        let date = new Date(dateString);
        let month = date.getMonth() + 1;
        let formatedDate = month + '月' + date.getDate() + '日(' + new String('日月火水木金土').charAt(date.getDay()) + ')';
        let formatedTime = date.getHours() + ':' + ('0' + date.getMinutes()).slice(-2);
        return formatedDate + formatedTime;
    }

    function formatDate2(dateString) {
        let date = new Date(dateString);
        let month = date.getMonth() + 1;
        let formatedDate = date.getFullYear() + '-' + ('0' + month).slice(-2) + '-' + ('0' + date.getDate()).slice(-2);
        let formatedTime = ('0' + date.getHours()).slice(-2) + ':' + ('0' + date.getMinutes()).slice(-2);
        return formatedDate + '-' + formatedTime;
    }
});