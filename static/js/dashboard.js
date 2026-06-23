document.addEventListener("DOMContentLoaded", () => {

    const alertsChart =
        document.getElementById("alertsChart");

    if(alertsChart){

        new Chart(alertsChart,{

            type:"doughnut",

            data:{

                labels:[
                    "Critical",
                    "Medium"
                ],

                datasets:[{

                    data:[1,3],

                    backgroundColor:[
                        "#ef4444",
                        "#facc15"
                    ]

                }]
            }
        });
    }

    const logsChart =
        document.getElementById("logsChart");

    if(logsChart){

        new Chart(logsChart,{

            type:"line",

            data:{

                labels:[
                    "Mon",
                    "Tue",
                    "Wed",
                    "Thu",
                    "Fri"
                ],

                datasets:[{

                    label:"Logs",

                    data:[
                        12,
                        19,
                        8,
                        15,
                        25
                    ],

                    borderColor:"#38bdf8",

                    fill:false
                }]
            }
        });
    }

});