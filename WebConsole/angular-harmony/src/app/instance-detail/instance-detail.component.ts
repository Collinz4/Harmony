import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CollectorService } from '../collector.service';

import { Timeline } from '../timeline';

@Component({
  selector: 'app-instance-detail',
  templateUrl: './instance-detail.component.html',
  styleUrls: ['./instance-detail.component.css']
})
export class InstanceDetailComponent implements OnInit {

  name?: string;
  timeline?: Timeline;

  constructor(
    private route: ActivatedRoute,
    private collectorService: CollectorService
  ) { }

  ngOnInit(): void {
    this.getInstanceTimeline();
  }

  getInstanceTimeline() {
    const name = this.route.snapshot.paramMap.get('name');
    this.name = name || "";
    this.collectorService.getInstanceMetrics(this.name).subscribe(
      timeline => this.timeline = timeline
    );
  }
}
