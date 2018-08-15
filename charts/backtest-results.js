function drawCharts(data) {
  console.log(data)
}
d3.queue()
  .defer(d3.csv, 'results.csv')
  .await(function(error, data) {
    drawCharts(data)
  })
