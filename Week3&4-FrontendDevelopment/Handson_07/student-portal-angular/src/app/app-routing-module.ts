import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { CourseList } from './course-list/course-list';
import { Profile } from './profile/profile';

const routes: Routes = [
  { path: '', component: CourseList },
  { path: 'profile', component: Profile }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}