import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InstanceCardComponent } from './instance-card.component';

describe('InstanceCardComponent', () => {
  let component: InstanceCardComponent;
  let fixture: ComponentFixture<InstanceCardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InstanceCardComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(InstanceCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
