import { ApplicationConfig, provideBrowserGlobalErrorListeners } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';

import { provideStore } from '@ngrx/store';
import { provideEffects } from '@ngrx/effects';
import { provideStoreDevtools } from '@ngrx/store-devtools';
import { ErrorHandler } from '@angular/core';

import { GlobalErrorHandler } from './global-error-handler';
import { routes } from './app.routes';

import { courseReducer } from './store/reducers/course.reducer';
import { CourseEffects } from './store/effects/course.effects';
export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(),
    provideRouter(routes),
    provideStore({
        courses: courseReducer
    }),
    provideEffects([
      CourseEffects
    ]),
    // provideStoreDevtools({ maxAge: 25, logOnly: !isDevMode() }),
    provideStoreDevtools({
      maxAge: 25,
      logOnly: false,
    }),
    provideHttpClient(),
    {
      provide: ErrorHandler,
      useClass: GlobalErrorHandler
    },
  ],
};
