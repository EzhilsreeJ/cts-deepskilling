import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-course-card',
  standalone: false,
  templateUrl: './course-card.html',
  styleUrls: ['./course-card.css']
})
export class CourseCard {

  @Input() name!: string;

  @Input() code!: string;

  @Input() credits!: number;

  @Input() grade!: string;

}