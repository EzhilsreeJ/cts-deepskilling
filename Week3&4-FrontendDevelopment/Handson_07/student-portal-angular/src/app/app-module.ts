import { NgModule, provideBrowserGlobalErrorListeners } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing-module';
import { App } from './app';
import { Header } from './header/header';
import { CourseList } from './course-list/course-list';
import { CourseCard } from './course-card/course-card';
import { StudentProfile } from './student-profile/student-profile';
import { HttpClientModule } from '@angular/common/http';
import { Profile } from './profile/profile';
import { RouterModule } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';
@NgModule({
  declarations: [App, Header, CourseList, CourseCard, StudentProfile, Profile],
  imports: [BrowserModule, AppRoutingModule, FormsModule, HttpClientModule,RouterModule,ReactiveFormsModule],
  providers: [provideBrowserGlobalErrorListeners()],
  bootstrap: [App],
})
export class AppModule {}
