function drawCharts() {
  const svgWidth = 960, svgHeight = 500
  const margin = {top: 20, right: 20, bottom: 110, left: 40}
  margin2 = {top: 430, right: 20, bottom: 30, left: 40}

  const width = svgWidth - margin.left - margin.right,
    height = svgHeight - margin.top - margin.bottom,
    height2 = svgHeight - margin2.top - margin2.bottom


  const svg = d3.select('body').append('svg')
    .attr('width', svgWidth)
    .attr('height', svgHeight)

  const x = d3.scaleTime().range([0, width]),
    x2 = d3.scaleTime().range([0, width]),
    y = d3.scaleLinear().range([height, 0]),
    y2 = d3.scaleLinear().range([height2, 0])

  function make_y_gridlines() {return d3.axisLeft(y)}
  function make_x_gridlines() {return d3.axisBottom(x)}

  const xAxis = d3.axisBottom(x),
    xAxis2 = d3.axisBottom(x2),
    yAxis = d3.axisLeft(y)

  const brush = d3.brushX()
    .extent([[0, 0], [width, height2]])
    .on('brush end', brushed);

  const zoom = d3.zoom()
    .scaleExtent([1, Infinity])
    .translateExtent([[0, 0], [width, height]])
    .extent([[0, 0], [width, height]])
    .on('zoom', zoomed)

  const investmentLine = d3.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.investment); });

  const priceLine = d3.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.price); });

  const line2 = d3.line()
    .x(function(d) { return x2(d.date); })
    .y(function(d) { return y2(d.investment); });

  svg.append('defs').append('clipPath')
    .attr('id', 'clip')
    .append('rect')
    .attr('width', width)
    .attr('height', height)

  const focus = svg.append('g')
    .attr('class', 'focus')
    .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')
  const context = svg.append('g')
    .attr('class', 'context')
    .attr('transform', 'translate(' + margin2.left + ',' + margin2.top + ')');

  d3.csv('results.csv', type, function(error, csv) {
    if (error) throw error

    const data = csv.filter(function(key) {
      return key != 'Time' && key != 'Transaction' && key != 'Data'
    }) 

    x.domain(d3.extent(data, function(d) { return d.date }))
    const priceDomain = d3.extent(data, function(d) { return d.price })
    const investDomain = d3.extent(data, function(d) { return d.investment })
    y.domain([
      Math.min(priceDomain[0], investDomain[0]),
      Math.max(priceDomain[1], investDomain[1])
    ])
    x2.domain(x.domain())
    y2.domain(y.domain())

    focus.append('path')
      .datum(data)
      .attr('class', 'line investment')
      .attr('d', investmentLine)

    focus.append('path')
      .datum(data)
      .attr('class', 'line price')
      .attr('d', priceLine)

    focus.append('g')
      .attr('class', 'axis axis--x')
      .attr('transform', 'translate(0,' + height + ')')
      .call(xAxis)

    focus.append('g')
      .attr('class', 'axis axis--y')
      .call(yAxis)

    context.append('path')
      .datum(data)
      .attr('class', 'line')
      .attr('d', line2)

    context.append('g')
      .attr('class', 'axis axis--x')
      .attr('transform', 'translate(0,' + height2 + ')')
      .call(xAxis2)

    context.append('g')
      .attr('class', 'brush')
      .call(brush)
      .call(brush.move, x.range())

    svg.append('rect')
      .attr('class', 'zoom')
      .attr('width', width)
      .attr('height', height)
      .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')
      .call(zoom)

      focus.append('g')
      .attr('class', 'grid')
      .call(make_y_gridlines()
          .tickSize(-width)
          .tickFormat('')
      )

    focus.append('g')
      .attr('class', 'grid')
      .attr('transform', 'translate(0,' + height + ')')
      .call(make_x_gridlines()
        .tickSize(-height)
        .tickFormat('')
      )
  })

  function brushed() {
    if (d3.event.sourceEvent && d3.event.sourceEvent.type === 'zoom') return; // ignore brush-by-zoom
    const s = d3.event.selection || x2.range();
    x.domain(s.map(x2.invert, x2));
    focus.select('.line.investment').attr('d', investmentLine);
    focus.select('.line.price').attr('d', priceLine);
    focus.select('.axis--x').call(xAxis);
    svg.select('.zoom').call(zoom.transform, d3.zoomIdentity
      .scale(width / (s[1] - s[0]))
      .translate(-s[0], 0));
  }

  function zoomed() {
    if (d3.event.sourceEvent && d3.event.sourceEvent.type === 'brush') return; // ignore zoom-by-brush
    const t = d3.event.transform;
    x.domain(t.rescaleX(x2).domain());
    focus.select('.line.investment').attr('d', investmentLine);
    focus.select('.line.price').attr('d', priceLine);
    focus.select('.axis--x').call(xAxis);
    context.select('.brush').call(brush.move, x.range().map(t.invertX, t));
  }
  const parseDate = d3.utcParse('%Y-%m-%dT%H:%M:%SZ')

  function type(d) {
    return {
      date: parseDate(d.Time),
      price: +d.Data,
      investment: +d.Transaction * +d.Data
    }
  }
}

drawCharts()
