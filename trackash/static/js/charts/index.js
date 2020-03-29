
const chart_monthtly = async () => {
    const { default: Chart } = await import( 
        /* webpackChunkName: "chart.js" */'chart.js'
    );
    const { default: pattern } = await import( 
        /* webpackChunkName: "patternomaly" */ 'patternomaly'
    );

    const ctx = document.getElementById('myChart').getContext('2d');


    const myChart = new Chart(ctx, {
        type: 'bar',
        labels: ["Incomes", "Expenses"],
        data: {
            labels: [
                'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
            ],
            datasets: [{
                label: 'Income',
                data: [
                    1500000, 1400000, 2500000, 1600000,
                    2800000, 2300000, 1500000, 2700000,
                    1400000, 2200000, 2600000, 2300000,
                ],
                backgroundColor: [
                    pattern.draw('zigzag-horizontal', '#34dee0'),
                    pattern.draw('zigzag-horizontal', '#34dee0'),
                    pattern.draw('zigzag-horizontal', '#34dee0'),
                    pattern.draw('zigzag-horizontal', '#34dee0'),
                    pattern.draw('zigzag-horizontal', '#34dee0'),
                    pattern.draw('zigzag-horizontal', '#34dee0'),
                    pattern.draw('zigzag-horizontal', '#34dee0'),
                    pattern.draw('zigzag-horizontal', '#34dee0'),
                    pattern.draw('zigzag-horizontal', '#34dee0'),
                    pattern.draw('zigzag-horizontal', '#34dee0'),
                    pattern.draw('zigzag-horizontal', '#34dee0'),
                    pattern.draw('zigzag-horizontal', '#34dee0'),
                ],
                borderColor: [
                    '#34dee0', '#34dee0', '#34dee0', '#34dee0', 
                    '#34dee0', '#34dee0', '#34dee0', '#34dee0', 
                    '#34dee0', '#34dee0', '#34dee0', '#34dee0',
                ],
                borderWidth: 2
            },
            {
                label: "Expense",
                data: [
                    800000,  400000, 1600000, 1500000,
                    1000000, 990000, 1400000, 1100000,
                    960000,  980000, 1800000, 1500000,
                ],
                backgroundColor: [
                    '#346be0', '#346be0', '#346be0', '#346be0',
                    '#346be0', '#346be0', '#346be0', '#346be0',
                    '#346be0', '#346be0', '#346be0', '#346be0',
                ],
                borderColor: [
                    '#346be0', '#346be0', '#346be0', '#346be0',
                    '#346be0', '#346be0', '#346be0', '#346be0',
                    '#346be0', '#346be0', '#346be0', '#346be0',
                ],
                borderWidth: 2
            }]
        },
        options: {
            legend: {
                labels: {
                    fontColor: '#8232f2',
                    fontFamily: `
                        'Helvetica Neue', 'Helvetica',
                        'Arial', sans-serif"
                    `,
                    fontSize: 18
                }
            },
            scales: {
                yAxes: [{
                    stacked: false,
                    ticks: {
                        min: 100000,
                        max: 3000000
                    }
                }],
                xAxes: [{
                    statcked: false
                }]
            }
        }
    });
}

export default chart_monthtly;
