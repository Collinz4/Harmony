import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable, of } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';

import { Timeline, DataPoint } from './timeline';

@Injectable({
  providedIn: 'root'
})
export class CollectorService {

  httpOptions = {
    headers: new HttpHeaders({ 
      'Content-Type': 'application/json',
    })
  }

  constructor(
    private http: HttpClient,
  ) { }

  getInstanceNames(): Observable<string[]> {
    return this.http.get<string[]>('http://localhost:5000/instances', this.httpOptions).pipe(
      tap(_ => console.log('Successfully fetched instance names.')),
      catchError(this.recoverError<string[]>('getInstanceNames'))
    );
  }

  getInstanceMetrics(instanceName: string): Observable<Timeline> {
    return this.http.get<Timeline>(`http://localhost:5000/timeline/${instanceName}`, this.httpOptions).pipe(
      tap(_ => console.log(`Successfully fetched timeline for ${instanceName}.`)),
      catchError(this.recoverError<Timeline>('getInstanceMetrics'))
    );
  }

  getInstanceLatestDataPoint(instanceName: string): Observable<DataPoint> {
    return this.http.get<DataPoint>(`http://localhost:5000/timeline/${instanceName}/latest`, this.httpOptions).pipe(
      tap(_ => console.log(`Successfully fetched latest data point for ${instanceName}`)),
      catchError(this.recoverError<DataPoint>('getInstanceLatestMetric'))
    );
  }

  /**
   * Handle Http request failures and returns a 'default' result.
   * 
   * @param operation - name of the method that failed
   * @param result - optional value to return as the observable result
   */
  private recoverError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.log(`${operation} failed: ${error.message}`);
      return of(result as T);
    };
  }
}
