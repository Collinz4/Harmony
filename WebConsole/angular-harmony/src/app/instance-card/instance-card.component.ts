import { Component, OnInit, Input } from '@angular/core';

import { CollectorService } from '../collector.service'

@Component({
  selector: 'app-instance-card',
  templateUrl: './instance-card.component.html',
  styleUrls: ['./instance-card.component.css']
})
export class InstanceCardComponent implements OnInit {

  @Input() instanceName: string = "";
  intervalID?: any;

  public chartOptions = {
    scaleShowVerticalLines: false,
    responsive: true,
    animation: {
      duration: 0,
    },
    scales:{
      xAxes: [{
          display: false
      }],
      yAxes: [{
        ticks: {
            beginAtZero: true,
            suggestedMin: 0,
            suggestedMax: 100
        }
    }]
    },
  };
  public chartType = 'line';
  public chartLegend = true;


  public cpu_xAxisTimeline: Date[] = [];
  public cpu_chartData: {data: number[], label: string}[] = [
    { data: [], label: 'CPU Usage' },
  ];

  public memory_xAxisTimeline: Date[] = [];
  public memory_chartData: {data: number[], label: string}[] = [
    { data: [], label: 'Memory Usage' },
  ];


  constructor(
    private collectorService: CollectorService,
  ) { }

  ngOnInit(): void {
    this.getTimeline();
    this.intervalID = setInterval(() => this.getTimeline(), 30000);
  }

  ngOnDestroy() {
    if (this.intervalID) {
      clearInterval(this.intervalID);
    }
  }

  getTimeline(): void {
    this.collectorService.getInstanceMetrics(this.instanceName).subscribe(
      metrics => {

        // reset chart data sources
        this.cpu_xAxisTimeline = [];
        this.cpu_chartData[0].data = [];
        this.memory_xAxisTimeline = [];
        this.memory_chartData[0].data = [];
        metrics.timeline.forEach(datapoint => {
          this.cpu_xAxisTimeline.push(new Date(datapoint.timestamp));
          this.cpu_chartData[0].data.push(datapoint.cpu_percentage);

          this.memory_xAxisTimeline.push(new Date(datapoint.memory_percentage));
          this.memory_chartData[0].data.push(datapoint.memory_percentage);
        });
      }
    );
  }
}
