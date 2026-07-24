import { Component, OnInit } from '@angular/core';
import { Course } from '../course';
import { ChangeDetectorRef } from '@angular/core';
@Component({
  selector: 'app-course-list',
  standalone: false,
  templateUrl: './course-list.html',
  styleUrls: ['./course-list.css']
})
export class CourseList implements OnInit  {
  constructor(
  private courseService: Course,
  private cdr: ChangeDetectorRef
) {}
  courses: any[] = [];
  loading = false;
  searchTerm = "";
  ngOnInit(): void {
  // console.log("ngOnInit started");

  this.loading = true;

  this.courseService.getCourses().subscribe({
    next: (data) => {
      // console.log("next", data);

      this.courses = data.map((post: any, index: number) => ({
        id: post.id,
        name: post.title,
        code: `ANG10${index + 1}`,
        credits: 3 + (index % 2),
        grade: 'A'
      }));

      // console.log("loading false");
      this.loading = false;
      this.cdr.detectChanges();
    },
    error: (err) => {
      // console.error("error", err);
      this.loading = false;
    },
    complete: () => {
      // console.log("complete");
    }
  });
}
  get filteredCourses() {
    return this.courses.filter(course =>
      course.name.toLowerCase().includes(this.searchTerm.toLowerCase())
    );
  }

}