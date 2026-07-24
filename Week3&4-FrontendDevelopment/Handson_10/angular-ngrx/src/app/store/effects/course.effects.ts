import { Injectable, inject } from '@angular/core';

import { Actions, createEffect, ofType } from '@ngrx/effects';

import * as CourseActions from '../actions/course.actions';

import { CourseService } from '../../services/course.service';

import { catchError, map, mergeMap, of } from 'rxjs';

@Injectable()
export class CourseEffects {

  private actions$ = inject(Actions);

  private courseService = inject(CourseService);

  loadCourses$ = createEffect(() =>

    this.actions$.pipe(

      ofType(CourseActions.loadCourses),

      mergeMap(() =>

        this.courseService.getCourses().pipe(

          map(courses =>
            CourseActions.loadCoursesSuccess({ courses })
          ),

          catchError(error =>
            of(CourseActions.loadCoursesFailure({ error }))
          )

        )

      )

    )

  );

}