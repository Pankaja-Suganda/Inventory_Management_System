'use strict';

var ctx_invoice = document.getElementById('chart-invoice').getContext('2d');
var ctx_po = document.getElementById('chart-purchase').getContext('2d');
var ctx_sales = document.getElementById('chart-sales').getContext('2d');
var ctx_stock = document.getElementById('chart-stock').getContext('2d');
var ctx_material = document.getElementById('chart-material').getContext('2d');


var chart_invoice = new Chart(ctx_invoice, {
    type: 'line',
    data: {
        datasets: [{
                label: 'Total Price (Rs.)',
                pointRadius: 1,
                pointHoverRadius: 6,
                borderWidth: 3,
                tension: 0.1
            },
            {
                label: 'Invoice Count',
                pointRadius: 1,
                pointHoverRadius: 6,
                borderWidth: 3,
                tension: 0.1
            }
        ]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        },
        interaction: {
            mode: 'index',
        }
    }
});

var chart_purchase = new Chart(ctx_po, {
    type: 'line',
    data: {
        datasets: [{
                label: 'Total Price (Rs.)',
                borderWidth: 3,
                tension: 0.1
            },
            {
                label: 'Invoice Count',
                borderWidth: 3,
                tension: 0.1
            }
        ]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        },
        interaction: {
            mode: 'index',
        }
    }
});

var chart_sales = new Chart(ctx_sales, {
    type: 'line',
    data: {
        datasets: [{
                label: 'Total Price (Rs.)',
                borderWidth: 3,
                tension: 0.1
            },
            {
                label: 'Invoice Count',
                borderWidth: 3,
                tension: 0.1
            }
        ]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        },
        interaction: {
            mode: 'index',
        }
    }
});

var chart_stock = new Chart(ctx_stock, {
    type: 'bar',
    data: {
        datasets: [{
                label: 'Quantity',
                borderWidth: 3,
                tension: 0.1
            },
            {
                label: 'Stock Margin',
                borderWidth: 3,
                tension: 0.1
            }
        ]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        },
        interaction: {
            mode: 'index',
        }
    }
});

var chart_material = new Chart(ctx_material, {
    type: 'bar',
    data: {
        datasets: [{
                label: 'Quantity',
                borderWidth: 3,
                tension: 0.1
            },
            {
                label: 'Stock Margin',
                tension: 0.1
            }
        ]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        },
        interaction: {
            mode: 'index',
        }
    }
});

var dynamicColors = function(length, alpha_1, alpha_2) {
    var colors = [];
    var color_arr_1 = [];
    var color_arr_2 = [];
    for (var i = 0; i < length; i++) {

        var r = Math.floor(Math.random() * 255);
        var g = Math.floor(Math.random() * 255);
        var b = Math.floor(Math.random() * 255);

        color_arr_1.push('rgb(' + r + ',' + g + ',' + b + ',' + alpha_1 + ')');
        color_arr_2.push('rgb(' + r + ',' + g + ',' + b + ',' + alpha_2 + ')');
    }

    colors.push(color_arr_1);
    colors.push(color_arr_2);

    return colors;
};


function invoice_chart(dataset) {
    var colors = dynamicColors(dataset['labels'].length, 0.9, 0.3);

    chart_invoice.data.labels = dataset['labels'];
    chart_invoice.data.datasets[0].data = dataset['total_price_sum'];
    chart_invoice.data.datasets[0].borderColor = colors[0];
    chart_invoice.data.datasets[0].backgroundColor = colors[1];
    chart_invoice.data.datasets[1].data = dataset['object_count'];
    chart_invoice.data.datasets[1].borderColor = colors[1];
    chart_invoice.data.datasets[1].backgroundColor = colors[1];

    chart_invoice.options.scales.x.title.display = true;
    chart_invoice.options.scales.x.title.text = dataset['frequency'];

    chart_invoice.options.scales.y.title.display = true;
    chart_invoice.options.scales.y.title.text = 'Total Price (Rs.)';
    chart_invoice.update();
}


function purchase_chart(dataset) {
    var colors = dynamicColors(dataset['labels'].length, 0.9, 0.3);

    chart_purchase.data.labels = dataset['labels'];
    chart_purchase.data.datasets[0].data = dataset['total_price_sum'];
    chart_purchase.data.datasets[0].borderColor = colors[0];
    chart_purchase.data.datasets[0].backgroundColor = colors[1];
    chart_purchase.data.datasets[1].data = dataset['object_count'];
    chart_purchase.data.datasets[1].borderColor = colors[1];
    chart_purchase.data.datasets[1].backgroundColor = colors[1];

    chart_purchase.options.scales.x.title.display = true;
    chart_purchase.options.scales.x.title.text = dataset['frequency'];

    chart_purchase.options.scales.y.title.display = true;
    chart_purchase.options.scales.y.title.text = 'Total Price (Rs.)';
    chart_purchase.update();
}

function sales_chart(dataset) {
    var colors = dynamicColors(dataset['labels'].length, 0.9, 0.3);

    chart_sales.data.labels = dataset['labels'];
    chart_sales.data.datasets[0].data = dataset['total_price_sum'];
    chart_sales.data.datasets[0].borderColor = colors[0];
    chart_sales.data.datasets[0].backgroundColor = colors[1];
    chart_sales.data.datasets[1].data = dataset['object_count'];
    chart_sales.data.datasets[1].borderColor = colors[1];
    chart_sales.data.datasets[1].backgroundColor = colors[1];

    chart_sales.options.scales.x.title.display = true;
    chart_sales.options.scales.x.title.text = dataset['frequency'];

    chart_sales.options.scales.y.title.display = true;
    chart_sales.options.scales.y.title.text = 'Total Price (Rs.)';
    chart_sales.update();
}

function stock_chart(dataset) {
    var colors = dynamicColors(dataset['Label'].length, 0.9, 0.3);

    chart_stock.data.labels = dataset['Label'];
    chart_stock.data.datasets[0].data = dataset['Quantity'];
    chart_stock.data.datasets[0].backgroundColor = colors[0];
    chart_stock.data.datasets[1].data = dataset['Stock Margin'];
    chart_stock.data.datasets[1].backgroundColor = colors[1];

    chart_stock.options.scales.x.title.display = true;
    chart_stock.options.scales.x.title.text = 'Stocks';

    chart_stock.options.scales.y.title.display = true;
    chart_stock.options.scales.y.title.text = 'Quantity';
    chart_stock.update();
}

function material_chart(dataset) {
    var colors = dynamicColors(dataset['Label'].length, 0.9, 0.3);

    chart_material.data.labels = dataset['Label'];
    chart_material.data.datasets[0].data = dataset['Quantity'];
    chart_material.data.datasets[0].backgroundColor = colors[0];
    chart_material.data.datasets[1].data = dataset['Stock Margin'];
    chart_material.data.datasets[1].backgroundColor = colors[1];

    chart_material.options.scales.x.title.display = true;
    chart_material.options.scales.x.title.text = 'Materials';

    chart_material.options.scales.y.title.display = true;
    chart_material.options.scales.y.title.text = 'Quantity';
    chart_material.update();
}

$(document).ready(function() {
    setTimeout(function() {
        $.ajax({
            url: "/stock_material_dataset/",
            type: 'GET',
            dataType: "json",
            success: function(res) {
                console.log(res);
                stock_chart(res[0]['data_stock']);
                material_chart(res[0]['data_material']);
            }
        });
    }, 100);
});