import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AttendanceComponent } from './attendance/attendance.component';
import { FaceRecognisedComponent } from './face-recognised/face-recognised.component';
import { FaceNotRecognisedComponent } from './face-not-recognised/face-not-recognised.component';
import { PopupComponent } from './popup/popup.component';
import { LoginComponent } from './login/login.component';
import { UserComponent } from './user/user.component';

const routes: Routes = [
  { path: '', redirectTo: '/attendance', pathMatch: 'full' },
  {path: 'attendance', component: AttendanceComponent},
  {path: 'face-recognised',component:FaceRecognisedComponent},
  {path: 'face-not-recognised',component:FaceNotRecognisedComponent},
  {path:'popup',component:PopupComponent},
  {path:'loginn',component:LoginComponent},
  {path:'user',component:UserComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
