const jData = JSON.parse('{{ jsonData|escapejs }}');
const MODULE = "AccidentEmergency"

const patientsByIntervalData = jData.graphs[MODULE].interval["barline-1"]
const triageByIntervalData = jData.graphs[MODULE].triage["comparison-1"]
const triageByZoneData = jData.graphs[MODULE].Zone["barpie-1"]
const patientsByDoctorData = jData.graphs[MODULE].Doctor["barline-1"]
const doctorStats = jData.docstats

// function secondsToHHMM(seconds) {
//     const hours = Math.floor(seconds / 3600);
//     const minutes = Math.floor((seconds - (hours * 3600)) / 60);

//     const formattedHours = hours < 10 ? '0' + hours : hours;
//     const formattedMinutes = minutes < 10 ? '0' + minutes : minutes;

//     return formattedHours + ':' + formattedMinutes;
// }

function secondsToHHMM(seconds) {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}`;
}

function CreatePatientIntervalChart() {
    const labels = patientsByIntervalData.x;
    const columnData = patientsByIntervalData.y.find(obj => obj.type === 'column').data;
    const lineData = patientsByIntervalData.y.find(obj => obj.type === 'line').data;
    const formattedLineData = lineData.map(seconds => secondsToHHMM(seconds));

    const options = {
        series: [{
            name: 'Patients',
            type: 'column',
            data: columnData
        }, {
            name: 'Average Time',
            type: 'line',
            data: lineData
        }],
        chart: {
            height: 650,
            type: 'line',
            stacked: false,
        },
        stroke: {
            width: [0, 2],
            curve: 'smooth'
        },
        plotOptions: {
            bar: {
                columnWidth: '50%'
            }
        },
        fill: {
            opacity: [0.85, 1],
            gradient: {
                inverseColors: false,
                shade: 'light',
                type: "vertical",
                opacityFrom: 0.85,
                opacityTo: 0.55,
                stops: [0, 100, 100, 100]
            }
        },
        labels: labels,
        markers: {
            size: 0
        },
        xaxis: {
            type: 'category',
            categories: labels,
            title: {
                text: 'Intervals'
            }
        },
        yaxis: [
            {
                title: {
                    text: 'Count',
                },
                min: 0,
                seriesName: 'Total Visits',
                opposite: false
            },
            {
                title: {
                    text: 'Average Time (hh:mm)',
                },
                min: 0,
                seriesName: 'Average Time',
                opposite: true,
                labels: {
                    formatter: function (value) {
                        return secondsToHHMM(value);
                    }
                }
            }
        ],
        tooltip: {
            shared: true,
            intersect: false,
            y: {
                formatter: function (y, { seriesIndex }) {
                    if (typeof y !== "undefined") {
                        if (seriesIndex === 1) {
                            return secondsToHHMM(y);
                        }
                        return y.toFixed(0);
                    }
                    return y;
                }
            }
        }
    };

    const chart = new ApexCharts(document.querySelector("#patients_interval_chart"), options);
    return chart
}

function CreateTriageZoneChart() {
    const labels = triageByZoneData.bar.x;
    const columnData = triageByZoneData.bar.y[0].data;
    const lineData = triageByZoneData.bar.y[1].data;

    const formattedLineData = lineData.map(seconds => secondsToHHMM(seconds));

    const options = {
        chart: {
            height: 350,
            type: 'line',
            stacked: false
        },
        series: [
            {
                name: 'Total Visits',
                type: 'column',
                data: columnData
            },
            {
                name: 'Average Time',
                type: 'line',
                data: lineData
            }
        ],
        yaxis: [
            {
                title: {
                    text: 'Count',
                },
                min: 0,
                seriesName: 'Total Visits',
                opposite: false
            },
            {
                title: {
                    text: 'Average Time (hh:mm)',
                },
                min: 0,
                seriesName: 'Average Time',
                opposite: true,
                labels: {
                    formatter: function (value) {
                        console.log("in seconds", value)
                        const fmt = secondsToHHMM(value);
                        console.log("fmt", fmt)
                        return fmt
                    }
                }
            }
        ],
        xaxis: {
            type: 'category',
            categories: labels,
            title: {
                text: 'Zones'
            }
        },
    }
    const chart = new ApexCharts(document.querySelector("#triage_by_zone_chart"), options);
    chart.render();

}

function CreatePatientsByDoctorChart() {
    const labels = patientsByDoctorData.x;
    const columnData = patientsByDoctorData.y[0].data;
    const lineData = patientsByDoctorData.y[1].data;

    const formattedLineData = lineData.map(seconds => secondsToHHMM(seconds));

    const options = {
        chart: {
            height: 350,
            type: 'line',
            stacked: false
        },
        series: [
            {
                name: 'Total Visits',
                type: 'column',
                data: columnData
            },
            {
                name: 'Average Time',
                type: 'line',
                data: lineData
            }
        ],
        yaxis: [
            {
                title: {
                    text: 'Count',
                },
                min: 0,
                seriesName: 'Total Visits',
                opposite: false
            },
            {
                title: {
                    text: 'Average Time (hh:mm)',
                },
                min: 0,
                seriesName: 'Average Time',
                opposite: true,
                labels: {
                    formatter: function (value) {
                        return secondsToHHMM(value);
                    }
                }
            }
        ],
        xaxis: {
            type: 'category',
            categories: labels,
            title: {
                text: 'Doctor Names'
            }
        },
    }
    const chart = new ApexCharts(document.querySelector("#patients_by_doctor_chart"), options);
    chart.render();
}

function CreateTriageByIntervalChart() {
    const labels = triageByIntervalData.x;
    const columnDataTriageDone = triageByIntervalData.y[0].data;
    const lineDataTriageDone = triageByIntervalData.y[1].data;
    const columnDataTriageNotDone = triageByIntervalData.y[2].data;
    const lineDataTriageNotDone = triageByIntervalData.y[3].data;

    const options = {
        chart: {
            height: 350,
            type: 'line',
            stacked: false
        },
        series: [
            {
                name: 'Triage Done',
                type: 'column',
                data: columnDataTriageDone
            },
            {
                name: 'Triage Done (Avg Time)',
                type: 'line',
                data: lineDataTriageDone
            },
            {
                name: 'Triage Not Done',
                type: 'column',
                data: columnDataTriageNotDone
            },
            {
                name: 'Triage Not Done (Avg Time)',
                type: 'line',
                data: lineDataTriageNotDone
            }
        ],
        yaxis: [
            {
                seriesName: 'Triage Done',
                title: {
                    text: 'Triage Done',
                },
                min: 0,
                opposite: false,
                labels: {
                    formatter: function (value) {
                        return value;
                    }
                }
            },
            {
                seriesName: 'Triage Done (Avg Time)',
                title: {
                    text: 'Triage Done (Avg Time)',
                },
                min: 0,
                opposite: true,
                labels: {
                    formatter: function (value) {
                        return value;
                    }
                }
            },
            {
                seriesName: 'Triage Not Done',
                title: {
                    text: 'Triage Not Done',
                },
                min: 0,
                opposite: false,
                labels: {
                    formatter: function (value) {
                        return value;
                    }
                }

            },
            {
                seriesName: 'Triage Not Done (Avg Time)',
                title: {
                    text: 'Triage Not Done (Avg Time)',
                },
                min: 0,
                opposite: true,
                labels: {
                    formatter: function (value) {
                        return value;
                    }
                }
            }
        ],
        xaxis: {
            type: 'category',
            categories: labels,
            title: {
                text: 'Intervals'
            }
        },
        fill: {
            opacity: 0.7, // Adjust the opacity of the area component
            gradient: {
                enabled: false, // Set to true to apply a gradient effect to the area component
                shade: 'light', // Customize the shade of the gradient effect
                type: 'vertical' // Choose from horizontal, vertical, diagonal1, diagonal2
            }
        },
        stroke: {
            width: [2, 2, 0], // Customize the line and column stroke widths
            curve: 'smooth' // Apply smooth interpolation to the line component
        },
    }
    const chart = new ApexCharts(document.querySelector("#triage_by_interval_chart"), options);
    chart.render();
}

CreatePatientIntervalChart().render()
CreateTriageZoneChart()
CreatePatientsByDoctorChart()
CreateTriageByIntervalChart()


var table = $('#docstats-table').DataTable({
    data: doctorStats,
    columns: [
        { data: 'doc_name', title: 'Doctor Name' },
        { data: 'count', title: 'Count' },
        { data: 'avg_visit_tm', title: 'Average Visit Time' }
    ],
    pageLength: 4,
    lengthMenu: [4, 8, 12, 16],
    dom: '<"row"<"col-sm-12 col-md-6"l><"col-sm-12 col-md-6"f>>' +
        '<"row"<"col-sm-12"tr>>' +
        '<"row"<"col-sm-12 col-md-5"i><"col-sm-12 col-md-7"p>>',
    language: {
        search: "_INPUT_",
        searchPlaceholder: "Search...",
        lengthMenu: "_MENU_",
        paginate: {
            first: "First",
            last: "Last",
            next: "Next",
            previous: "Previous"
        }
    }
});

// Apply Bootstrap classes
$('#docstats-table_wrapper').addClass('my-4');
$('#docstats-table_filter input').addClass('form-control');
$('#docstats-table_length select').addClass('form-select');
$('#docstats-table_length label').addClass('fw-bold');
$('#docstats-table_paginate .paginate_button').addClass('btn btn-outline-primary mx-1');
$('#docstats-table_paginate .paginate_button.current').addClass('btn btn-primary mx-1');



