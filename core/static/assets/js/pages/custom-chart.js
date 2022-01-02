'use strict';
var chart_invoice;
var chart_stock;
var chart_material;
var chart_purchase;
var chart_sales;
var data;

$(document).ready(function() {
    setTimeout(function() {
        $.ajax({
            url: "/stock_material_dataset/",
            type: 'GET',
            dataType: "json",
            success: function(res) {
                console.log("res : ", res);
                chart_stock = Morris.Bar({
                    element: 'chart-stock',
                    data: res[0]['data_stock'],
                    parseTime: false,
                    xkey: 'Label',
                    barSizeRatio: 0.70,
                    barGap: 3,
                    redraw: true,
                    resize: true,
                    axes: true,
                    responsive: true,
                    ykeys: ['Quantity', 'Stock Margin'],
                    labels: ['Quantity', 'Stock Margin'],
                    barColors: ["0-#1de9b6-#1dc4e9", "#bd0013"]
                });
                chart_stock.redraw();

                chart_material = Morris.Bar({
                    element: 'chart-material',
                    data: res[0]['data_material'],
                    parseTime: false,
                    xkey: 'Label',
                    barSizeRatio: 0.70,
                    barGap: 3,
                    redraw: true,
                    resize: true,
                    responsive: true,
                    ykeys: ['Quantity', 'Stock Margin'],
                    labels: ['Quantity', 'Stock Margin'],
                    barColors: ["0-#1de9b6-#1dc4e9", "#bd0013"]
                });
                chart_material.redraw();
            }
        });
    }, 700);

    chart_purchase = Morris.Line({
        element: 'chart-purchase',
        // data: dataset,
        parseTime: false,
        xkey: 'y',
        redraw: true,
        resize: true,
        ykeys: ['a', 'b'],
        hideHover: 'auto',
        responsive: true,
        labels: ['Total Price (Rs.)', 'PO Count'],
        lineColors: ['#1de9b6', '#A389D4']
    });

    chart_invoice = Morris.Line({
        element: 'chart-invoice',
        // data: dataset,
        parseTime: false,
        xkey: 'y',
        redraw: true,
        resize: true,
        ykeys: ['a', 'b'],
        hideHover: 'auto',
        responsive: true,
        labels: ['Total Price (Rs.)', 'Invoice Count'],
        lineColors: ['#1de9b6', '#A389D4']
    });

    chart_sales = Morris.Line({
        element: 'chart-sales',
        // data: dataset,
        parseTime: false,
        xkey: 'y',
        redraw: true,
        resize: true,
        ykeys: ['a', 'b'],
        hideHover: 'auto',
        responsive: true,
        labels: ['Total Price (Rs.)', 'SO Count'],
        lineColors: ['#1de9b6', '#A389D4']
    });

});


function invoice_chart(dataset) {
    console.log("json : ", dataset);
    chart_invoice.setData(dataset);
    chart_invoice.redraw();
}

function purchase_chart(dataset) {
    console.log("json : ", dataset);
    chart_purchase.setData(dataset);
    chart_purchase.redraw();
}

function sales_chart(dataset) {
    console.log("json : ", dataset);
    chart_sales.setData(dataset);
    cart_sales.redraw();
}