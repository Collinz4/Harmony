import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DashboardComponent } from './dashboard/dashboard.component';
import { InstanceDetailComponent } from './instance-detail/instance-detail.component';

const routes: Routes = [
  { path: '', component: DashboardComponent },
  { path: 'instance/:name', component: InstanceDetailComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
