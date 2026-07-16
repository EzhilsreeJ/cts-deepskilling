import { Injectable, inject } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';

import { Course } from '../models/course.model';

@Injectable({
  providedIn: 'root'
})

export class CourseService {

  private http = inject(HttpClient);

  private api =
  'https://jsonplaceholder.typicode.com/posts';

  getCourses():Observable<Course[]>{

    return this.http.get<Course[]>(this.api);

  }

}