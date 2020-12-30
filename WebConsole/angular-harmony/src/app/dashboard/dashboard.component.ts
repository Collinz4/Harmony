import { Component, OnInit } from '@angular/core';
import { CollectorService } from '../collector.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  instances?: string[];

  constructor(
    private collectorService: CollectorService,
  ) { }

  ngOnInit(): void {
    this.getInstanceNames()
  }

  getInstanceNames(): void {
    this.collectorService.getInstanceNames().subscribe(
      instanceNames => this.instances = instanceNames
    );
  }
}
