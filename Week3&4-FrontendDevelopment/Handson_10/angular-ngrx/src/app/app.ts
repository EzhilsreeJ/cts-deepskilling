// import { Component, signal } from '@angular/core';
// import { RouterOutlet } from '@angular/router';

// @Component({
//   selector: 'app-root',
//   imports: [RouterOutlet],
//   templateUrl: './app.html',
//   styleUrl: './app.css'
// })
// export class App {
//   protected readonly title = signal('angular-ngrx');
// }
import { Component, inject } from '@angular/core';

import { CommonModule } from '@angular/common';

import { Store } from '@ngrx/store';

import * as CourseActions from './store/actions/course.actions';

import {
  selectCourses,
  selectLoading,
  selectError
} from './store/selectors/course.selectors';

@Component({
  selector: 'app-root',

  standalone: true,

  imports: [CommonModule],

  templateUrl: './app.html',

  styleUrl: './app.css'
})

export class App {

  private store = inject(Store);

  courses$ = this.store.select(selectCourses);

  loading$ = this.store.select(selectLoading);

  error$ = this.store.select(selectError);

  constructor() {

    this.store.dispatch(
      CourseActions.loadCourses()
    );

  }

}